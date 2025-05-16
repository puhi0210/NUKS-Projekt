# Motivacijski Citati App

Enostavna aplikacija za pridobivanje, shranjevanje in pregled motivacijskih citatov. Backend je zgrajen z FastAPI, frontend je preprost HTML/JS, celoten projekt pa teče z Docker Compose.

## Tehnologije
- Python 3.10 + FastAPI
- SQLite
- HTML/CSS/JavaScript (vanilla)
- Docker + Docker Compose

## Funkcionalnosti
- Pridobi naključni motivacijski citat (zunanji API)
- Shrani priljubljene citate v lokalno bazo
- Prikaži vse shranjene citate
- Izbriši citate iz seznama priljubljenih

## Zagon aplikacije

1. Kloniraj repozitorij:
   ```bash
   git clone https://github.com/tvoje-ime/motivacijski-citati-app.git
   ```

2. Zaženi aplikacijo z Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Odpri brskalnik:
   - Frontend: [http://localhost:8080](http://localhost:8080)
   - Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)

## API dokumentacija
Glej `docs/api_documentation.md` ali obišči `/docs` endpoint na backendu.
