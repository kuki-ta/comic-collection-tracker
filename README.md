# Comic Collection Tracker

SQL database to track and analyze a Batman comic book collection, built with SQLite and populated via the Comic Vine API. Used Claude to generate and troubleshoot the Python API script, then manually modified the data and wrote all SQL queries independently.

Preferred to call real data instead of making it up and populating it all manually, with the exception of the comic's estimated value in USD and publisher's founded year which aren't naturally part of the set, and the comic's condition and read status which I randomized with SQL CASE statements to help make query outputs a bit more interesting.

Writing out all clauses and arguments in full instead of using aliases since I'm still getting comfortable with shorthand, but wanted the queries readable!

```
        __.--'\     \.__./     /'--.__
    _.-'       '.__.'    '.__.'       '-._
  .'                                      '.
 /                                          \
|                                            |
|                                            |
 \         .---.              .---.         /
  '._    .'     '.''.    .''.'     '.    _.'
     '-./            \  /            \.-'
                      ''
```

## Files
- `comics.db` — SQLite database
- `queries.sql` — SQL queries with comments
- `fetch_comics.py` — Python script to fetch data from the Comic Vine API
