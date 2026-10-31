# basedcommander.com: put it online, then get ready for the App Store

Build it with `python3 tools/build_exports.py`. That makes `dist/basedcommander.com.zip`, a flat zip of the whole site (this file stays out of it).

## What the site has

| Address | What it is |
|---|---|
| `/` | Landing page with **LAUNCH IN BROWSER** and **DOWNLOAD APP** |
| `/play/` | The game itself (everything bundled, no outside requests) |
| `/privacy/` | Privacy policy. Use it as the App Store **Privacy Policy URL** |
| `/support/` | Help and contact. Use it as the App Store **Support URL** |
| `/manifest.webmanifest`, `/sw.js` | Install as an app, and offline play after the first visit |
| `/.htaccess` | File types, compression and caching for Apache (cPanel) |
| `/robots.txt`, `/sitemap.xml` | For search engines |

## Put it online with cPanel (Spaceship hosting)

1. Open Spaceship, then Hosting Manager, then cPanel for basedcommander.com. (Never paste a cPanel address into a chat or email: it carries your logged-in session.)
2. In cPanel open **File Manager**, then **public_html**. Under **Settings** (top right) tick **Show Hidden Files (dotfiles)**, so you can see `.htaccess`.
3. Delete any placeholder page the host put there (for example `index.html` or `default.html`). Leave `cgi-bin` and `.well-known` alone.
4. Click **Upload**, choose `basedcommander.com.zip`, wait for 100%, then go back to public_html.
5. Right-click the zip, choose **Extract**, keep the path `/public_html`, and extract. Then delete the zip.
6. Check that `index.html`, `play`, `privacy`, `support` and `.htaccess` now sit directly inside public_html, not inside another folder.
7. HTTPS: in cPanel open **SSL/TLS Status** and run **AutoSSL** if basedcommander.com does not show a valid certificate yet. A new domain can take a while to get one.
8. Once the certificate is valid, open **Domains** and turn on **Force HTTPS Redirect** for basedcommander.com.
9. Email: create `support@basedcommander.com` under **Email Accounts**, or forward it to your own inbox under **Forwarders**. Send it a test email. The site, the privacy policy and the game all point people there.
10. Test on your phone: open https://basedcommander.com, tap **LAUNCH IN BROWSER**, then the gear, **PRIVACY AND HELP**. Back on the landing page, try **DOWNLOAD APP**.

If the domain does not load at all, check in Spaceship that basedcommander.com is connected to this hosting plan.

**Updating later:** rebuild, then upload and extract the new zip over the old files (say yes to overwrite). Players get the new version on their next visit while online; offline they keep the last one they loaded.

## Let people try it as an app now

- **Android, Windows, Chromebook, Mac (Chrome or Edge):** DOWNLOAD APP opens the browser's own install window.
- **iPhone and iPad:** DOWNLOAD APP shows the Add to Home Screen steps. It opens full screen with its own icon and plays offline.
- **When TestFlight or the App Store link exists:** put it in `APP_STORE_URL` at the top of `export/site/assets/site.js`, rebuild and upload. iPhone visitors then go straight there.

## App Store checklist

Apple's rules this is built around (checked October 31, 2026):

- Guideline 5.1.1(i): "All apps must include a link to their privacy policy in the App Store Connect metadata field and within the app in an easily accessible manner." In the game: the gear, then **PRIVACY AND HELP**, which shows the policy summary and opens the full policy.
- Guideline 1.3 (Kids Category): no links out "unless reserved for a designated area behind a parental gate", and no third-party analytics or advertising. The full-policy link sits behind a grown-ups math question, and the app has no ads, analytics or purchases.
- Apple's Kids page describes parental gates as "adult-level tasks", with a math task as its example.

Sources: https://developer.apple.com/app-store/review/guidelines/ , https://developer.apple.com/app-store/kids-apps/ , https://developer.apple.com/testflight/

In App Store Connect:

1. **App Information:** Privacy Policy URL `https://basedcommander.com/privacy/`. Category: Games. Kids Category is optional; the app already meets its rules.
2. **Version page:** Support URL `https://basedcommander.com/support/`, Marketing URL `https://basedcommander.com/`, description, keywords, screenshots.
3. **App Privacy:** Data Not Collected. The app collects nothing and has no third-party code.
4. **Age rating:** answer the questionnaire. The battles are cartoon-style stun fights where nobody gets hurt.
5. **Build:** follow `ios/README.md` (Archive in Xcode, then upload).
6. **TestFlight first:** your App Store Connect team can test right away. For everyone else, add an external group and turn on its public link: up to 10,000 testers, after the first build passes a beta review, and each build lasts 90 days.
7. Then submit the version for review.
