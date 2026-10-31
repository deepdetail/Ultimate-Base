# BASED Commander for iPhone (Xcode project)

A small native iPhone app (SwiftUI and WKWebView) that runs the game bundled inside it from the `BASEDCommander/Web` folder. It plays offline, keeps saves on the phone, and runs in portrait on iPhone, iOS 16 or newer.

## 1. Run it on your own iPhone (free, no $99 needed)
1. Unzip, then double-click `BASEDCommander.xcodeproj` to open it in Xcode.
2. Xcode > Settings > Accounts > the + button > Apple ID, and sign in.
3. In the left sidebar click the blue **BASEDCommander** project, pick the **BASEDCommander** target, then the **Signing & Capabilities** tab. Keep "Automatically manage signing" on and set **Team** to your name (Personal Team).
4. If Xcode says the bundle identifier is not available, change it to something unique, such as `com.yourname.basedcommander`.
5. Plug the iPhone in with a cable, unlock it and tap Trust. Pick the iPhone in the device menu at the top of the Xcode window.
6. On the iPhone, turn on Settings > Privacy & Security > Developer Mode (the phone restarts).
7. Press the Run button (the triangle). The first time, the iPhone may block the app as an untrusted developer: Settings > General > VPN & Device Management > your Apple ID > Trust, then open it again.

With a free Apple ID the app stops opening after 7 days. Plug in and press Run again to refresh it. A free account can keep up to 3 apps like this on one device.

## 2. TestFlight and the App Store (needs the Apple Developer Program, $99 a year)
1. Enroll at developer.apple.com/programs. Enrolling as an organization needs your D-U-N-S number; enrolling as an individual does not.
2. In Xcode, set **Team** to the paid team.
3. In App Store Connect (appstoreconnect.apple.com) > Apps > + > New App: name it, choose the same bundle ID as in Xcode, and type any SKU.
4. In Xcode pick **Any iOS Device (arm64)** as the destination, then Product > Archive. When the Organizer window opens: Distribute App > App Store Connect > Upload.
5. When processing finishes, the build shows up under TestFlight in App Store Connect. People on your App Store Connect team can install it with the TestFlight app right away; outside testers need a short beta review first.
6. For the App Store: add screenshots, a description, the age rating questionnaire and App Privacy ("Data Not Collected"), pick the build, then Submit for Review.

Every upload needs a higher build number: raise **Build** in the target's General tab (it starts at 1, version 2.0).

## Kids and privacy
- No ads, no analytics, no sign-in, and nothing leaves the phone. Saves stay in the app on the device.
- The app opens one outside link: the privacy policy on basedcommander.com, in Safari, and only after a grown-ups question (a parental gate) under Settings, PRIVACY AND HELP. Apple requires the privacy policy to be reachable inside the app (guideline 5.1.1), and the Kids Category requires a parental gate before outside links or purchases and does not allow third-party ads or analytics (guideline 1.3). This app has no purchases, ads or analytics.
- `ITSAppUsesNonExemptEncryption` is set to NO in `Info.plist`, so uploads skip the encryption question (the app does no encryption of its own).

## Moving a base into the app
Saves in a web browser and saves in the app are separate. In the browser: Settings (the gear) > SAVE CODE, copy it. In the app: Settings > LOAD CODE, paste.

## Updating the game inside the app
The game lives in `BASEDCommander/Web`. After the game changes, run `python3 tools/build_exports.py` from the repository (or ask Claude to), then build again in Xcode.

## Settings at a glance
| Setting | Value | Where to change it |
|---|---|---|
| Bundle ID | `com.deepdetail.basedcommander` | Target > Signing & Capabilities |
| Name under the icon | BASED | Target > General > Display Name |
| Version / build | 2.0 / 1 | Target > General |
| Devices | iPhone, portrait | Target > General > Supported Destinations |
| Minimum iOS | 16.0 | Target > General > Minimum Deployments |

Code: `BASEDCommanderApp.swift` starts the app; `GameView.swift` holds the web view and the small file server that hands it the `Web` folder at `based://game/`.
