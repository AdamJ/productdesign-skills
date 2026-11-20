---
name: app-store-readiness
description: >
  Prepare an iOS, iPadOS, or macOS app's App Store assets and metadata for submission. Use whenever Adam says he's getting an app ready for the App Store, wants to submit or resubmit a build, is prepping screenshots, app previews, the app icon, or the product page, or asks "am I ready to submit?" Also trigger for App Store Connect asset questions (screenshot sizes, app preview specs, creative assets) and for pre-submission checklist reviews on Brimfield Labs apps or any other iOS project. Covers Apple's official asset best practices plus exact pixel specs for every device class, so Claude doesn't have to guess or rely on stale training data.
---

# App Store Readiness

A checklist-driven skill for taking an iOS/iPadOS/macOS app from "built" to "submitted," based on Apple's official App Store asset best practices and App Store Connect screenshot/app preview specifications.

This skill is a reference, not a generator. Use it to review what Adam has, flag gaps, and produce exact specs he can hand to a design tool or Xcode. Don't fabricate screenshot content or app copy on his behalf without asking.

## When to go deeper vs. stay quick

For a quick "what size do I need" question, just answer from the tables below. For a full pre-submission pass, work through every section under **Submission checklist** in order and report back gaps as a punch list, not a wall of text.

## Core principles from Apple's guidance

These come from Apple's [App Store asset best practices](https://developer.apple.com/app-store/asset-best-practices/) and hold for every asset type below.

- **Stay evergreen.** No pricing, discounts, URLs, or copyright symbols in screenshots or creative assets. No unverified award claims. No Apple-designated recognition badges (Editor's Choice, App of the Day, Design Award) even if the app has received them elsewhere.
- **4+ rating floor.** Every asset shown on the App Store must be appropriate for a 4+ audience, regardless of the app's actual age rating.
- **Real UI only.** Screenshots and previews should reflect the actual in-use app or gameplay, not marketing-only mockups. Captions, device frames, and backgrounds are fine. The UI inside the frame must be the real shipped UI, and a caption must not promise anything the build does not do.
- **Design for a global, all-ages audience.** Inclusive imagery, localized text where the app is localized.
- **Legibility over density.** One clear idea per asset. Key elements and text inside the safe area, focal point centered to survive cropping across placements.

## App icon

Use [Icon Composer](https://developer.apple.com/icon-composer/) to build a layered icon from a single design that covers iPhone, iPad, Mac, and Apple Watch, including the Liquid Glass treatment. Check legibility at every size the icon actually appears: App Store listing, Spotlight, Home Screen. For Brimfield Labs apps, this is the point to sanity-check the icon against Brimfield Sans and the brand palette before locking it in.

## Screenshots

Apple accepts 1–10 screenshots per device class per localization, JPEG/JPG/PNG, **no alpha channel or transparency**. Practical range is 5–7 well-sequenced images; the first three are what show up in search results, so lead with the strongest feature.

### iPhone

App Store Connect decides which iPhone class is required, and it has changed over time. Before building anything, open App Store Connect's screenshot section and note which iPhone and iPad classes it asks for. Then check the sizes against the specification page. Do not assume 6.9".

| Display class | Required?                                                          | Portrait sizes (px)               |
| ------------- | ------------------------------------------------------------------ | --------------------------------- |
| 6.9"          | Required if App Store Connect asks for it                          | 1260×2736 · 1290×2796 · 1320×2868 |
| 6.5"          | Required only if 6.9" isn't provided                               | 1284×2778 · 1242×2688             |
| 6.3"          | Required if App Store Connect asks for the 6.1"/6.3" class         | 1206×2622 · 1179×2556             |
| 6.1"          | Same class as 6.3"                                                 | 1170×2532 · 1125×2436 · 1080×2340 |
| 5.5"          | Optional (falls back to 6.1")                                      | 1242×2208                         |

Landscape is the reverse of each portrait pair. Where App Store Connect scales down from a larger set, export the largest class once and let it scale. Only build device-specific sets if the UI genuinely looks different per size, or if legibility breaks on scale-down (small body text is the usual failure point).

A 6.3" set can be scaled from a 6.9" capture: the aspect ratios differ by under 0.1%, so nothing distorts. Say in the hand-off that the images are scaled, not native captures.

### iPad

| Display class | Required?                    | Portrait sizes (px)                           |
| ------------- | ---------------------------- | --------------------------------------------- |
| 13"           | Required if app runs on iPad | 2064×2752 · 2048×2732                         |
| 11"           | Optional (falls back to 13") | 1488×2266 · 1668×2420 · 1668×2388 · 1640×2360 |

Landscape sizes are the portrait pairs reversed (for example 2752×2064). Use landscape when the app's iPad layout is built for landscape.

### Mac / Apple TV / Vision Pro / Watch

| Platform         | Required?                  | Sizes (px)                                                                                                                                                                     |
| ---------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Mac              | Required for Mac apps      | 1280×800 · 1440×900 · 2560×1600 · 2880×1800 (16:10)                                                                                                                            |
| Apple TV         | Required for tvOS apps     | 1920×1080 · 3840×2160                                                                                                                                                          |
| Apple Vision Pro | Required for visionOS apps | 3840×2160                                                                                                                                                                      |
| Apple Watch      | Required for watchOS apps  | Varies by Watch generation; must be consistent across all localizations — check current sizes in App Store Connect before export, since new Watch models add classes over time |

For Brimfield Vault (Mac Catalyst), that means a real Mac screenshot set at 16:10, not an upscaled iPad shot.

## App previews (optional videos)

Up to three per product page, up to three surfaced in search results. Must show real UI or gameplay. Pick a poster frame that reads on its own since it's what people see before tapping play. Lead with the strongest feature in the first few seconds, avoid fast cuts, and design the loop to be seamless since previews autoplay muted and repeat. If using audio, treat it as ambient brand texture, not narration.

## Product page header, search results, and In-App Events (creative assets)

These are separate from screenshots and appear across the App Store (product page, search, featuring) starting in iOS/iPadOS 27. Not required for a first submission, but worth flagging if the goal is to compete for featuring or build brand recognition beyond the product page:

- **Header** (product page): 5244×2950, 16:9. One clear idea for a first-time visitor. A universal asset can double as the search results asset for consistency.
- **Search results:** 3840×2560. The app's purpose must be obvious at a glance since people are already searching for something specific.
- Keep the app name, headline, and focal content inside the centre. Devices may bleed off an edge, but never crop text or the key control.
- No alpha channel. No prices, URLs, awards, or copyright marks.
- Confirm sizes against App Store Connect before uploading; Apple adds and changes them.
- **In-App Events:** need both a 16:9 event card and a 9:16 detail-page asset, visually tied together, that complement (not duplicate) the event's badge type.

Apple provides Figma, Photoshop, and Pixelmator templates for these; link is in the asset best practices page if Adam wants the templates.

## Producing the assets

Steps for generating screenshot and creative assets from a simulator build. Skip any step the user has already handled.

1. **Seed realistic, fictional data.** Never use real people or a real team. A demo team, roster, schedule, and history can often be loaded through the app's own backup import, so no app code changes.
2. **Set a clean status bar** (`xcrun simctl status_bar <device> override --time "9:41" ...`) and clear it afterward (`xcrun simctl status_bar <device> clear`).
3. **Capture** with `xcrun simctl io <device> screenshot`. The result has an alpha channel.
4. **Flatten** with `sips -s format jpeg -s formatOptions 100 in.png --out out.jpg`.
5. **Verify** with `sips -g pixelWidth -g pixelHeight -g hasAlpha` that every file has the exact pixel size and `hasAlpha: no`.
6. **Caption and frame** from HTML rendered by headless Chrome at the exact output size. Keep one script that rebuilds everything, so a retake is one command.
7. **Keep generated files clean.** Use relative paths in generated HTML and git-ignore it, so no local username or folder path is committed.
8. **Look at every image** before delivering. Check that text is not clipped by a device frame, that no personal data from the capture machine is visible, and that captions are true.

## Metadata and review-readiness (not visual assets, but part of "ready to submit")

- Re-read [App Review Guidelines §2.3](https://developer.apple.com/app-store/review/guidelines/#metadata) (Accurate Metadata) against the current app description and screenshots — this is the most common rejection category for indie apps.
- Confirm the app's actual age rating in App Store Connect matches what the content supports, separate from the 4+ floor on assets themselves.
- For local-first, no-account apps like Brimfield Soccer, double check the privacy nutrition label reflects "no data collected" accurately — it's an easy miss if a dependency (e.g., a crash reporter) collects anything.

## Submission checklist

Work through in this order and report gaps as a short punch list:

1. App icon: Icon Composer source, legible at Home Screen size, matches current brand.
2. iPhone screenshots: the class App Store Connect asks for (6.1"/6.3" or 6.9"), 5–7 images, first three carry the story, no pricing/URLs/copyright marks, no alpha channel.
3. iPad screenshots (if app runs on iPad): 13" set present, same rules as above.
3a. Header (5244×2950) and Search (3840×2560) assets, if competing for featuring or brand reach.
4. Mac/TV/Watch/Vision Pro screenshots if the app targets those platforms.
5. App preview video (optional): poster frame chosen, loops cleanly, works muted.
6. Product page copy: description, keywords, and screenshots all say the same thing; nothing unverifiable.
7. Privacy nutrition label matches actual data behavior.
8. Age rating matches content.
9. TestFlight build already validated on at least one physical device per platform being submitted.
10. Generated asset files contain no local paths or personal data.

## Reference

Source pages (fetch fresh if a submission is more than a few months out, since Apple revises device classes and sizes):

- Apple asset best practices: [https://developer.apple.com/app-store/asset-best-practices/](https://developer.apple.com/app-store/asset-best-practices/)
- App Store Connect screenshot specifications: [https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/)
- App Review Guidelines: [https://developer.apple.com/app-store/review/guidelines/](https://developer.apple.com/app-store/review/guidelines/)
