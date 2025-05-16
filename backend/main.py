from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from database import init_db, save_quote, get_all_quotes, delete_quote

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.get("/quote")
def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random")
        data = res.json()[0]
        return {"quote": data['q'], "author": data['a']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/favorites")
def add_favorite(quote: dict):
    return save_quote(quote['quote'], quote['author'])

@app.get("/favorites")
def list_favorites():
    return get_all_quotes()

@app.delete("/favorites/{quote_id}")
def remove_favorite(quote_id: int):
    return delete_quote(quote_id)