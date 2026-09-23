from typing import Literal, Optional

from pydantic import BaseModel, Field, field_validator


class JournalEntryCreate(BaseModel):
    """Payload for creating a new journal entry."""

    entry: str = Field(..., min_length=1, max_length=500)
    mood: Optional[Literal["happy", "sad", "neutral"]] = None

    @field_validator("entry")
    @classmethod
    def entry_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Entry cannot be empty")
        return value


class JournalEntry(BaseModel):
    """A saved journal entry, as returned by the API."""

    id: int
    message: str
    mood: str
    timestamp: str
