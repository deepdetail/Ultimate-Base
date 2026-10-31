import SwiftUI
import UIKit
import WebKit

/// A full-screen web view that runs the game from the app's own Web folder through a private
/// `based://` address. Everything is inside the app, so it plays offline, and saves
/// (localStorage) stay on the device.
struct GameView: UIViewRepresentable {
    func makeCoordinator() -> Coordinator { Coordinator() }

    func makeUIView(context: Context) -> WKWebView {
        let config = WKWebViewConfiguration()
        config.setURLSchemeHandler(context.coordinator.files, forURLScheme: BundleFiles.scheme)
        config.websiteDataStore = .default()
        config.allowsInlineMediaPlayback = true
        config.mediaTypesRequiringUserActionForPlayback = []

        // Feel like an app, not a web page: no long-press menus, no text selection outside
        // text boxes, no gray flash on tap.
        let css = "html,body{-webkit-touch-callout:none;-webkit-user-select:none;user-select:none;-webkit-tap-highlight-color:transparent}input,textarea{-webkit-user-select:text;user-select:text}"
        let js = "(function(){var s=document.createElement('style');s.textContent='\(css)';document.documentElement.appendChild(s);})();"
        config.userContentController.addUserScript(
            WKUserScript(source: js, injectionTime: .atDocumentEnd, forMainFrameOnly: true))

        let web = WKWebView(frame: .zero, configuration: config)
        let background = UIColor(named: "LaunchBackground") ?? .black
        web.isOpaque = false
        web.backgroundColor = background
        web.scrollView.backgroundColor = background
        // The game pads itself for the notch and home bar (viewport-fit=cover).
        web.scrollView.contentInsetAdjustmentBehavior = .never
        web.scrollView.bounces = false
        web.allowsBackForwardNavigationGestures = false
        web.allowsLinkPreview = false
        web.navigationDelegate = context.coordinator
        web.uiDelegate = context.coordinator
        #if DEBUG
        // Lets Safari's Develop menu on the Mac inspect the game while testing.
        if #available(iOS 16.4, *) { web.isInspectable = true }
        #endif
        web.load(URLRequest(url: BundleFiles.startURL))
        return web
    }

    func updateUIView(_ uiView: WKWebView, context: Context) {}

    final class Coordinator: NSObject, WKNavigationDelegate, WKUIDelegate {
        let files = BundleFiles()

        // The game never leaves the app: only its own pages load. (A kids app must not open
        // outside links without a parent gate, and this game has none to open.)
        func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction,
                     decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
            let scheme = navigationAction.request.url?.scheme ?? ""
            let inApp = scheme == BundleFiles.scheme || scheme == "about" || scheme == "blob" || scheme == "data"
            decisionHandler(inApp ? .allow : .cancel)
        }

        // iOS can stop the web view's process when memory runs low. Reload; the game saves itself.
        func webViewWebContentProcessDidTerminate(_ webView: WKWebView) {
            webView.load(URLRequest(url: BundleFiles.startURL))
        }

        // window.alert and window.confirm show as normal iOS alerts.
        func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String,
                     initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
            let alert = UIAlertController(title: nil, message: message, preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in completionHandler() })
            present(alert, over: webView, orElse: completionHandler)
        }

        func webView(_ webView: WKWebView, runJavaScriptConfirmPanelWithMessage message: String,
                     initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping (Bool) -> Void) {
            let alert = UIAlertController(title: nil, message: message, preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "Cancel", style: .cancel) { _ in completionHandler(false) })
            alert.addAction(UIAlertAction(title: "OK", style: .default) { _ in completionHandler(true) })
            present(alert, over: webView, orElse: { completionHandler(false) })
        }

        private func present(_ alert: UIAlertController, over view: UIView, orElse fallback: () -> Void) {
            guard var top = view.window?.rootViewController else { return fallback() }
            while let next = top.presentedViewController { top = next }
            top.present(alert, animated: true)
        }
    }
}

/// Serves the files in the app bundle's Web folder at based://game/...
final class BundleFiles: NSObject, WKURLSchemeHandler {
    static let scheme = "based"
    static let startURL = URL(string: "based://game/index.html")!

    private let root = Bundle.main.bundleURL.appendingPathComponent("Web", isDirectory: true).standardizedFileURL

    func webView(_ webView: WKWebView, start urlSchemeTask: WKURLSchemeTask) {
        guard let url = urlSchemeTask.request.url else { return }
        var path = url.path
        if path.isEmpty || path == "/" { path = "/index.html" }
        let file = root.appendingPathComponent(String(path.dropFirst())).standardizedFileURL

        // Only files inside the Web folder, never anything else on the phone.
        guard file.path.hasPrefix(root.path + "/"), let data = try? Data(contentsOf: file) else {
            let missing = HTTPURLResponse(url: url, statusCode: 404, httpVersion: "HTTP/1.1",
                                          headerFields: ["Content-Type": "text/plain"])!
            urlSchemeTask.didReceive(missing)
            urlSchemeTask.didReceive(Data())
            urlSchemeTask.didFinish()
            return
        }
        let found = HTTPURLResponse(url: url, statusCode: 200, httpVersion: "HTTP/1.1", headerFields: [
            "Content-Type": Self.mimeType(for: file.pathExtension),
            "Content-Length": String(data.count),
            "Cache-Control": "no-cache",
        ])!
        urlSchemeTask.didReceive(found)
        urlSchemeTask.didReceive(data)
        urlSchemeTask.didFinish()
    }

    func webView(_ webView: WKWebView, stop urlSchemeTask: WKURLSchemeTask) {}

    static func mimeType(for ext: String) -> String {
        switch ext.lowercased() {
        case "html", "htm": return "text/html; charset=utf-8"
        case "js": return "text/javascript; charset=utf-8"
        case "css": return "text/css; charset=utf-8"
        case "json", "webmanifest": return "application/json"
        case "png": return "image/png"
        case "jpg", "jpeg": return "image/jpeg"
        case "webp": return "image/webp"
        case "gif": return "image/gif"
        case "svg": return "image/svg+xml"
        case "woff2": return "font/woff2"
        case "woff": return "font/woff"
        case "txt", "md": return "text/plain; charset=utf-8"
        default: return "application/octet-stream"
        }
    }
}
