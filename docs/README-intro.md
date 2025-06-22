# 📓 Greger – Tekniska anteckningar

## Arkitekturell översikt

- Projektet är modulärt (src/)
- CI-flöde ligger under `.github/`
- Nyckelbaserad datakoppling sköts via `src/datakopplingar/`

## TODO för teknisk setup:
- [ ] Koppla GitHub till lokal dev-miljö
- [ ] Skapa sandbox-miljö för strategi-A/B-test
- [ ] Sätta upp `.env` för test-API-nycklar
- [ ] Koppla CI till GitHub Actions

## Möjliga förbättringar / idéer:
- [ ] Docker-container för hela miljön
- [ ] Grafisk loggning med Dash / Streamlit
- [ ] Automatiserad edge-benchmarking mot top 10-robotar
