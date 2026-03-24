# J.A.R.V.I.S. COMMAND — Unified Operations Hub

> Unified command surface for the JARVIS ecosystem. Every module, one shell.

**Live:** [truebruiser.github.io/jarvis-ops](https://truebruiser.github.io/jarvis-ops/)

## Architecture

Single-page application with sidebar navigation and swappable module panels. Static-first design deployed on GitHub Pages — every data seam is ready for dynamic backend migration.

### Data Flow

All external API calls route through a caching layer (`cached()` → IndexedDB) with configurable TTLs. Feed health is tracked per-source with status indicators in the sidebar and statusbar.

**Current (static):** Direct fetch to public APIs
**Future (dynamic):** Swap URLs to `localhost:3000/api/feeds/*` endpoints — caching layer, panels, and status tracking remain unchanged.

## Modules

| Module | Panel | Data Sources | Status |
|--------|-------|-------------|--------|
| **Overview** | Live stats + card grid | All feeds | Live |
| **Daily Brief** | SITREP-format intelligence | USGS, NOAA SWPC, NASA EONET, NWS, HN | Live |
| **WORLDVIEW** | Leaflet map + live overlays | USGS, OpenSky, ISS API | Live |
| **ECLIPSE** | OSINT/SIGINT workbench | Requires JARVIS backend | Local only |
| **MERIDIAN** | Financial terminal | CoinGecko + subpage links | Live |
| **SENTINEL** | Penetration testing inventory | Static inventory | Ready |
| **PINECON** | WiFi intelligence engine | Requires Pineapple | Local only |
| **HERMES-MESH** | LoRa mesh bridge | Requires MQTT/serial | Local only |
| **SOAL** | Practice overview | Static | Ready |

## Subpages

| Page | Description |
|------|-------------|
| `worldview.html` | Full Leaflet flat map with live feeds |
| `worldview-live.html` | CesiumJS globe with CAMS + satellite tracking |
| `screener.html` | MERIDIAN stock screener — Russell 3000, MACD |
| `buffett-screener.html` | Buffett Moat screener — 130+ companies |
| `long-term-screener.html` | Long-term dividend growth screener |

## Security

See [SECURITY.md](SECURITY.md) for full threat model and CSP audit.

## Refresh Intervals

| Feed | Interval | TTL |
|------|----------|-----|
| ISS Position | 30s | 30s |
| OpenSky ADS-B | 2m | 2m |
| CoinGecko Crypto | 2m | 2m |
| USGS Seismic | 5m | 5m |
| NASA EONET | 10m | 10m |
| NOAA SWPC | 10m | 10m |
| NWS Weather | 15m | 15m |

## Browser Compatibility

Designed for Brave browser. All navigation uses `div[role="button"]` — no `<a href="#">` patterns that trigger Brave Shields interference.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Private repository. Not for redistribution.
