# Python AI Upskill — September 26

A repository for Python and AI upskilling exercises and projects.

## Setup

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## How to run

**CLI journal (Day 1):**

```bash
python src/cli/journal_cli.py
```

**API server (Day 2):**

```bash
uvicorn src.api.main:app --reload
```

The server starts at `http://localhost:8000`. Interactive docs are available at
`http://localhost:8000/docs`.

**Frontend preview:**

Open `frontend.html` directly in a browser (with the API server running) to
submit journal entries from a simple web form.

## API endpoints

### `GET /`

Landing route confirming the API is running.

**Response:**

```json
{ "message": "Journal API is running 🚀" }
```

### `GET /journal`

Return saved journal entries, optionally filtered by sentiment.

**Query parameters:**

| Name              | Type   | Required | Values                        |
| ----------------- | ------ | -------- | ------------------------------ |
| `sentiment_filter` | string | No       | `positive`, `negative`, `neutral` |

**Example:** `GET /journal?sentiment_filter=positive`

**Response:**

```json
[
  {
    "id": 1,
    "message": "Feeling productive",
    "mood": ":)",
    "timestamp": "2026-09-23 23:50"
  }
]
```

### `POST /journal`

Create a new journal entry and append it to `data/journal.csv`.

**Request body:**

```json
{
  "entry": "Today I learned FastAPI. It feels great!",
  "mood": "happy"
}
```

- `entry` is required, cannot be empty/blank, and must be 500 characters or fewer.
- `mood` is optional (`happy`, `sad`, or `neutral`); defaults to `neutral` if omitted.

**Response:**

```json
{
  "id": 4,
  "message": "Today I learned FastAPI. It feels great!",
  "mood": ":)",
  "timestamp": "2026-09-24 00:55"
}
```

A validation failure (empty entry, entry too long, or an invalid `mood`) returns
a `422 Unprocessable Entity` with details on which field failed.

## Learnings summary — Day 2

- Turned the Day 1 CLI script into a proper package layout (`src/cli`,
  `src/api`, `src/core`) so the same journal logic — CSV storage, mood
  handling — is shared between the terminal app and the web API instead of
  being duplicated.
- Built a FastAPI app with an `APIRouter` for the `/journal` resource,
  Pydantic models for request/response validation, and CORS middleware so a
  separately-hosted frontend can call the API.
- Learned that Pydantic (`Field`, `field_validator`, `Literal`) handles input
  validation declaratively — empty/oversized entries and invalid moods are
  rejected automatically with a `422` before the route code even runs.
- Practiced keeping the data layer (`file_handler.py`) separate from the HTTP
  layer (`journal_routes.py`), so the CSV read/write logic doesn't know
  anything about FastAPI.
- Wired up `black`, `isort`, and `flake8` for consistent formatting and
  linting, and learned that flake8's default line length needs to be raised
  to match Black's (88 chars) to avoid the two tools disagreeing.
- Built a minimal `frontend.html` using plain `fetch()` to confirm the API is
  actually usable from a browser, not just via curl/docs.
