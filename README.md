# Cricbuzz LiveStats

Cricbuzz LiveStats is a Streamlit dashboard for live cricket scores, player performance, SQL analytics, and SQLite-based CRUD operations.

## Features

- Browse live matches, scores, teams, venues, toss information, and scorecards.
- Review batting and bowling summaries from the local database.
- Run 25 categorized SQL analysis questions.
- Add, view, update, and delete player records.
- Use the included schema and sample data without an API key.

## Tech Stack

- Python 3.10+
- Streamlit
- SQLite
- Pandas
- Requests
- Cricbuzz REST API through RapidAPI

## Project Structure

```text
Cricbuzz-LiveStats/
|-- main.py
|-- requirements.txt
|-- database/
|   |-- schema.sql
|   |-- sample_data.sql
|-- pages/
|   |-- 1_Home.py
|   |-- 2_Live_Matches.py
|   |-- 3_Player_Stats.py
|   |-- 4_SQL_Analytics.py
|   |-- 5_CRUD_Operations.py
|-- utils/
|   |-- api.py
|   |-- db_connection.py
|   |-- queries.py
```

The local `database/cricket.db` file is generated on first run and is intentionally ignored by Git.

## Installation

From the project root, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

SQLite is included with Python and does not need a separate package.

## API Key Setup

Live match data requires a RapidAPI key for the Cricbuzz API. Create `.streamlit/secrets.toml`:

```toml
CRICBUZZ_API_KEY = "your-rapidapi-key"
```

Alternatively, set `CRICBUZZ_API_KEY` as an environment variable. The database, player stats, SQL analytics, and CRUD pages work without the key.

## Run

```powershell
streamlit run main.py
```

On the first run, the application creates the SQLite schema and loads the bundled sample data.

## Database

The normalized database includes `teams`, `players`, `venues`, `series`, `matches`, `batting_stats`, `bowling_stats`, and `fielding_stats` tables with keys, constraints, and indexes.

## License

This project is available under the MIT License. See `LICENSE`.
