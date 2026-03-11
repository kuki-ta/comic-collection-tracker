import urllib.request
import json
import sqlite3

API_KEY = "ed87929a5218553aae5f8512065793443dbc7f01"
BASE_URL = "https://comicvine.gamespot.com/api"
HEADERS = {"User-Agent": "comic-collection-tracker"}

def fetch(endpoint, params=""):
    url = f"{BASE_URL}/{endpoint}/?api_key={API_KEY}&format=json&limit=20{params}"
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["results"]

conn = sqlite3.connect("comics.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS comics;
DROP TABLE IF EXISTS publishers;

CREATE TABLE publishers (
    publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT,
    founded_year INTEGER
);

CREATE TABLE comics (
    comic_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    issue_number INTEGER,
    publisher_id INTEGER,
    genre TEXT,
    release_year INTEGER,
    condition TEXT,
    estimated_value_usd REAL,
    read_status TEXT
);

CREATE TABLE characters (
    character_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    comic_id INTEGER,
    hero_or_villain TEXT
);
""")

publishers = fetch("publishers")
for p in publishers:
    name = p.get("name", "Unknown")
    founded = p.get("start_year") or 0
    cur.execute(
        "INSERT INTO publishers (name, country, founded_year) VALUES (?, ?, ?)",
        (name, "USA", founded)
    )

issues = fetch("issues", "&filter=name:Batman")
for i in issues:
    title = i.get("volume", {}).get("name", "Unknown")
    issue_num = i.get("issue_number") or 0
    try:
        issue_num = int(issue_num)
    except:
        issue_num = 0
    year = 0
    cover_date = i.get("cover_date") or ""
    if cover_date:
        try:
            year = int(cover_date[:4])
        except:
            year = 0
    cur.execute(
        """INSERT INTO comics 
           (title, issue_number, publisher_id, genre, release_year, condition, estimated_value_usd, read_status)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (title, issue_num, 1, "Superhero", year, "Good", 0.00, "Unread")
    )

characters = fetch("characters", "&filter=name:Batman")
for idx, ch in enumerate(characters):
    name = ch.get("name", "Unknown")
    cur.execute(
        "INSERT INTO characters (name, comic_id, hero_or_villain) VALUES (?, ?, ?)",
        (name, (idx % 20) + 1, "Hero")
    )

conn.commit()
conn.close()
print("Done!")