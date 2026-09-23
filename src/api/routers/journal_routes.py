from datetime import datetime
from typing import Literal, Optional

from fastapi import APIRouter

from src.api.models.journal_model import JournalEntry, JournalEntryCreate
from src.api.utils.file_handler import load_entries, save_entry_to_csv
from src.core.config import MOOD_SYMBOLS

router = APIRouter(prefix="/journal", tags=["journal"])

# The filter uses sentiment words, while entries are stored by mood name.
SENTIMENT_TO_MOOD = {
    "positive": "happy",
    "negative": "sad",
    "neutral": "neutral",
}


@router.get("", response_model=list[JournalEntry])
def get_journal_entries(
    sentiment_filter: Optional[Literal["positive", "negative", "neutral"]] = None,
):
    """Return journal entries, optionally filtered by sentiment."""
    entries = load_entries()

    if sentiment_filter is None:
        return entries

    mood_symbol = MOOD_SYMBOLS[SENTIMENT_TO_MOOD[sentiment_filter]]
    return [entry for entry in entries if entry["mood"] == mood_symbol]


@router.post("", response_model=JournalEntry)
def add_entry(payload: JournalEntryCreate):
    """Create a new journal entry and persist it to the CSV file."""
    mood = payload.mood or "neutral"
    new_entry = {
        "id": len(load_entries()) + 1,
        "message": payload.entry,
        "mood": MOOD_SYMBOLS[mood],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    save_entry_to_csv(new_entry)
    return new_entry
