from pathlib import Path

# Resolve paths relative to the project root so the CSV location doesn't
# depend on the current working directory the app is launched from.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CSV_FILE = BASE_DIR / "data" / "journal.csv"
CSV_FIELDS = ["id", "message", "mood", "timestamp"]

# Moods are stored as ASCII emoticons rather than plain words.
MOOD_SYMBOLS = {
    "happy": ":)",
    "sad": ":(",
    "neutral": ":|",
}
