import sqlite3

def init_db():
    conn = sqlite3.connect("quotes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, quote TEXT, author TEXT)''')
    conn.commit()
    conn.close()

def save_quote(quote, author):
    conn = sqlite3.connect("quotes.db")
    c = conn.cursor()
    c.execute("INSERT INTO quotes (quote, author) VALUES (?, ?)", (quote, author))
    conn.commit()
    conn.close()
    return {"message": "Saved"}

def get_all_quotes():
    conn = sqlite3.connect("quotes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM quotes")
    rows = c.fetchall()
    conn.close()
    return [{"id": row[0], "quote": row[1], "author": row[2]} for row in rows]

def delete_quote(quote_id):
    conn = sqlite3.connect("quotes.db")
    c = conn.cursor()
    c.execute("DELETE FROM quotes WHERE id=?", (quote_id,))
    conn.commit()
    conn.close()
    return {"message": "Deleted"}