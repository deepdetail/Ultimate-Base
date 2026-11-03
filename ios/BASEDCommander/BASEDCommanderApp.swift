import SwiftUI
import UIKit

// BASED Commander for iPhone. The whole game is the web build in the Web folder,
// shown full screen by GameView. Rebuild that folder with tools/build_exports.py.
@main
struct BASEDCommanderApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) private var appDelegate

    var body: some Scene {
        WindowGroup {
            GameView()
                .ignoresSafeArea()
                .background(Color("LaunchBackground").ignoresSafeArea())
        }
    }
}

/// The app may turn sideways (Info.plist lists landscape), but it only does so during flight and driving missions.
/// iOS asks this every time it decides which way the screen may face.
final class AppDelegate: NSObject, UIApplicationDelegate {
    func application(_ application: UIApplication, supportedInterfaceOrientationsFor window: UIWindow?) -> UIInterfaceOrientationMask {
        ScreenTurn.allowed
    }
}

/// Turns the screen: the game asks for landscape when a mission starts and portrait when it ends.
enum ScreenTurn {
    static var allowed: UIInterfaceOrientationMask = .portrait

    static func set(landscape: Bool, in view: UIView?) {
        let mask: UIInterfaceOrientationMask = landscape ? .landscape : .portrait
        guard mask != allowed else { return }
        allowed = mask
        guard let scene = view?.window?.windowScene else { return }
        // Tell the screen's controller the allowed directions changed, then ask iOS to turn now.
        // (This works even with Rotation Lock on, because the app no longer allows the other way.)
        for window in scene.windows { window.rootViewController?.setNeedsUpdateOfSupportedInterfaceOrientations() }
        scene.requestGeometryUpdate(.iOS(interfaceOrientations: mask)) { _ in }
    }
}
