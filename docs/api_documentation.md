# 📑 Motivacijski Citati API Dokumentacija

## Osnove
- Osnova URL-ja (local): `http://localhost:8000`

---

## `GET /quote`
📌 Pridobi naključni motivacijski citat iz zunanjega API-ja.

**Primer odgovora:**
```json
{
  "quote": "Be yourself; everyone else is already taken.",
  "author": "Oscar Wilde"
}
```

---

## `POST /favorites`
💾 Shrani citat v seznam priljubljenih.

**Body (JSON):**
```json
{
  "quote": "Be yourself; everyone else is already taken.",
  "author": "Oscar Wilde"
}
```

**Odziv:**
```json
{
  "message": "Saved"
}
```

---

## `GET /favorites`
📄 Pridobi vse shranjene priljubljene citate.

**Odziv:**
```json
[
  {
    "id": 1,
    "quote": "Do one thing every day that scares you.",
    "author": "Eleanor Roosevelt"
  }
]
```

---

## `DELETE /favorites/{id}`
🗑️ Izbriši citat s podanim `id` iz baze.

**Odziv:**
```json
{
  "message": "Deleted"
}
```

---

## ℹ️ Napake
- `500 Internal Server Error`: težave s povezavo do zunanjega API-ja ali baze.
- `404 Not Found`: če ni citatov ali napačen ID pri brisanju.
