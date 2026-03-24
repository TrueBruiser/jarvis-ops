# Security Policy — JARVIS COMMAND

## Threat Model

Static site served via GitHub Pages. Primary attack surfaces:

1. **XSS via injected API responses** — mitigated by `esc()` sanitization on all external string data
2. **Exfiltration via CSP bypass** — mitigated by strict `connect-src` allowlist
3. **Clickjacking** — mitigated by `frame-src 'none'`
4. **MIME confusion** — mitigated by `X-Content-Type-Options: nosniff`

## What Is NOT in This Codebase

- API keys or tokens (all data sources are unauthenticated public APIs)
- Passwords or credentials
- Personal email addresses
- File system paths to local machines
- GitHub personal access tokens

## Local Service References

Display text only — no connection attempts from static deployment:

| Reference | Context | Risk |
|-----------|---------|------|
| `localhost:3000` | JARVIS Core backend | Display only |
| `localhost:1883` | MQTT broker | Display text |
| `172.16.42.1:1471` | WiFi Pineapple API | Display text |

## CSP Audit

Every domain in `connect-src` maps to a specific JS `fetch()` call:

| Domain | Feed | Verified |
|--------|------|----------|
| earthquake.usgs.gov | Seismic data | Yes |
| opensky-network.org | ADS-B flight data | Yes |
| api.alternative.me | Crypto Fear and Greed | Yes |
| api.coingecko.com | Crypto prices | Yes |
| api.wheretheiss.at | ISS position | Yes |
| api.weather.gov | NWS forecast | Yes |
| services.swpc.noaa.gov | Space weather Kp index | Yes |
| eonet.gsfc.nasa.gov | Natural events | Yes |
| hacker-news.firebaseio.com | Headlines for ticker/brief | Yes |

No unused domains. No wildcard sources.

## Reporting

Private project. Contact the repository owner.
