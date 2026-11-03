# Labels

Each screenshot gets exactly **one** label: the main thing the screen is showing.

## Games

Suggested set (swap any for games you know better):

| Game | Genre | Good for |
| --- | --- | --- |
| Brawl Stars | Arena shooter | Brawl Pass, shop offers, events |
| Clash Royale | Strategy | Pass Royale, tournaments, special offers |
| Royal Match | Puzzle | Limited-time events, sale popups, leaderboards |
| PUBG Mobile | Battle royale | Royale Pass, ranked screens, offers |
| Genshin Impact | RPG | Limited-time event banners, Battle Pass |

## Label definitions

| Label | Definition | Typical signs |
| --- | --- | --- |
| `sale_offer` | A screen whose main purpose is selling something: a discounted bundle, special offer or shop deal. | Prices, "% OFF", "Best value", "Buy", bundle contents, a countdown on an offer |
| `battle_pass` | A season pass screen showing a reward track with free and premium tiers. | Tier numbers, two reward rows (free / paid), progress bar, "Season X" |
| `limited_time_event` | A screen announcing or showing a time-limited event or game mode (not a pass, not mainly a sale). | Event banner or hub, "Ends in 3d", special event missions or rewards, themed art |
| `leaderboard` | A ranking or tournament screen comparing players or teams. | Ranked list of names with scores, your rank, tournament brackets, trophies |
| `none` | Normal gameplay, main menu, settings or any screen that is not one of the above. | Players in a match, a level being played, home screen without an event popup |

## Rules for unclear cases

1. **Pick the main purpose of the screen.** Ask: "What is this screen mainly trying to get the player to do?"
2. **Event screen with a buy button:** if most of the screen is about the event (missions, rewards, story), label `limited_time_event`. If it is mainly a priced bundle, label `sale_offer`.
3. **Battle pass purchase popup** ("Unlock premium pass for $9.99"): label `battle_pass`, because the pass is the product.
4. **Event leaderboard** (ranking inside an event): label `leaderboard`.
5. **Home screen with a small event icon:** label `none`. A label only counts if it is the main content.
6. **Too blurry, cropped or unreadable:** do not include the image in the dataset.
7. **Still unsure after these rules:** pick the closest label and write the reason in the `notes` column of `labels.csv`.

## Targets

- 60–100 images in total
- At least 10 images per label
- Spread each label across at least 3 different games, so the model learns the concept and not one game's art style
