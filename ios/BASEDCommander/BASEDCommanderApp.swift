import SwiftUI

// BASED Commander for iPhone. The whole game is the web build in the Web folder,
// shown full screen by GameView. Rebuild that folder with tools/build_exports.py.
@main
struct BASEDCommanderApp: App {
    var body: some Scene {
        WindowGroup {
            GameView()
                .ignoresSafeArea()
                .background(Color("LaunchBackground").ignoresSafeArea())
        }
    }
}
