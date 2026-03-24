# JARVIS OPS HUB — Project Context for Claude

## What This Is
A unified operations hub deployed at `truebruiser.github.io/jarvis-ops/` via GitHub Pages. Single-page application with a D3 orthographic globe hero, sidebar navigation, and module panels for intelligence, financial, security, and systems tools.

## Architecture
- **Single index.html** — all CSS, HTML, and JS in one file (~640 lines)
- **Subpages** — standalone HTML files iframed or linked from the hub:
  - `worldview.html` — Leaflet flat map with live USGS/OpenSky/ISS feeds
  - `worldview-live.html` — CesiumJS 3D globe with CAMS + satellite tracking
  - `screener.html` — MERIDIAN Russell 3000 stock screener with MACD
  - `buffett-screener.html` — Buffett Moat screener (130+ companies)
  - `long-term-screener.html` — Long-term dividend growth screener

## Tech Stack
- **Fonts**: Orbitron (headings), Rajdhani (body), IBM Plex Mono (data)
- **Globe**: D3.js v7 + TopoJSON (orthographic projection, auto-rotating, draggable)
- **Maps**: Leaflet 1.9.4 (worldview panel, dark-inverted tiles)
- **No build tools** — everything is vanilla HTML/CSS/JS, no npm, no bundler
- **Deployment**: git push to main → GitHub Pages auto-rebuilds in ~60 seconds

## Live Data Feeds (all free, no API keys)
| Feed | API | TTL | Updates |
|------|-----|-----|---------|
| Seismic | earthquake.usgs.gov | 5m | M2.5+ last 24h |
| Flights | opensky-network.org | 2m | N. America ADS-B count |
| Crypto | api.coingecko.com | 2m | BTC/ETH/SOL prices + 24h change |
| Fear/Greed | api.alternative.me | 10m | Crypto fear & greed index |
| ISS | api.wheretheiss.at | 30s | Position + altitude |
| Weather | api.weather.gov | 15m | Charlotte, NC (GSP/116,76) |
| Space Wx | services.swpc.noaa.gov | 10m | Kp planetary index |
| Events | eonet.gsfc.nasa.gov | 10m | Active natural events |
| Headlines | hacker-news.firebaseio.com | 5m | Top stories for ticker |

## Security Rules
- CSP is strict: `default-src 'none'` with explicit allowlists
- `frame-src 'self'` — subpages can be iframed from same origin
- All external string data MUST be escaped with `esc()` before innerHTML
- `esc()` covers: & < > " '
- NEVER put API keys, tokens, or credentials in the codebase
- All data sources are unauthenticated public APIs
- Local service refs (localhost:3000, 172.16.42.1:1471) are display text only

## Browser Compatibility
- Designed for **Brave** browser
- All navigation uses `<div role="button">` with onclick/onkeydown — NEVER `<a href="#">`
- Brave Shields intercepts anchor navigation intent; div buttons avoid this

## Module Panels (in index.html)
| Panel ID | Type | Notes |
|----------|------|-------|
| p-globe | D3 globe hero | Auto-rotating, draggable, quake/ISS/EONET markers |
| p-overview | Card grid | Links to all other panels |
| p-brief | Live data | Pulls from all feeds, formats as SITREP |
| p-worldview | iframe | Loads worldview.html inline |
| p-meridian | iframe | Loads screener.html, switchable to buffett/long-term |
| p-eclipse | Service detect | Shows OFFLINE when localhost:3000 unreachable |
| p-sentinel | Interactive | Device filter, payload actions, engagement log |
| p-pinecon | Service detect | Shows OFFLINE when 172.16.42.1:1471 unreachable |
| p-mesh | Info panel | HERMES-MESH LoRa bridge documentation |
| p-soal | Info panel | SOAL Industries practice overview |

## Conventions
- CSS variables are in `:root` — use them, never hardcode colors
- Color shortcuts: --g (green), --r (red), --o (orange), --b (blue), --p (purple), --c (cyan), --y (yellow)
- Dim variants: --gd, --rd, --od, --bd (15% opacity for backgrounds)
- Font shortcuts: --orb (Orbitron), --raj (Rajdhani), --mono (IBM Plex Mono)
- IndexedDB cache layer: `cached(url, ttlMs)` wraps all API fetches
- Feed health tracking: `feedOK(id)` lights up status dots in the statusbar

## Deployment
```powershell
cd C:\Users\jackg\jarvis-ops
git add -A
git commit -m "description of changes"
git push origin main
# GitHub Pages rebuilds in ~60 seconds
```

## Local Services (only work on home network)
- JARVIS Core: localhost:3000 (FastAPI backend, Docker)
- WORLDVIEW Engine: localhost:5055 (Flask OSINT server)
- Home Assistant: 192.168.65.3:8123
- WiFi Pineapple: 172.16.42.1:1471
- MQTT Broker: localhost:1883

## Owner
Jack (GitHub: TrueBruiser) — IT Helpdesk at Spencer Products, building SOAL Industries as an intelligence infrastructure practice. Based in Matthews, NC.
