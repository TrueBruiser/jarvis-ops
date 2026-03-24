# Changelog

## [2.0.0] — 2026-03-24

### Architecture
- Complete rebuild from portal model to unified command surface
- Sidebar navigation replaces top nav tabs — all modules as first-class panels
- Persistent topbar with system status pills, weather, UTC clock
- Persistent statusbar with per-feed health indicators
- Scrolling ticker with live seismic + headline data
- IndexedDB caching layer with configurable TTLs per feed
- Feed health tracking (count, cache size, session uptime)

### Modules Added as Inline Panels
- Overview — live stats grid + full card inventory
- Daily Brief — SITREP-format intelligence
- WORLDVIEW — inline Leaflet map with quake markers + ISS tracking
- ECLIPSE — local service connection panel
- MERIDIAN — live crypto prices + screener launch buttons
- SENTINEL — full hardware module inventory
- PINECON — WiFi intelligence engine overview
- HERMES-MESH — LoRa bridge architecture + MQTT topic reference
- SOAL — practice overview with certifications

### Security
- CSP tightened: removed 6 unused domains from connect-src
- XSS sanitization hardened: esc() now escapes quotes
- Leaflet popup content now escaped
- No secrets, tokens, or credentials in codebase
- All navigation uses div[role=button] — Brave compatible

### Responsive
- 3-tier breakpoints: desktop (full sidebar), tablet (icon-only sidebar), mobile (no sidebar)
- Card grid auto-fills from 280px minimum
- Stats grid collapses: 6-col to 3-col to 2-col

### Preserved
- All existing subpages unchanged (worldview.html, screener.html, buffett-screener.html, long-term-screener.html, worldview-live.html)
- Subpages accessible via panel header launch buttons
