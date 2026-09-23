import csv

from src.core.config import CSV_FIELDS, CSV_FILE


def load_entries() -> list:
    """Load all saved entries from the CSV file, if it exists."""
    if not CSV_FILE.is_file():
        return []

    with open(CSV_FILE, newline="") as f:
        return list(csv.DictReader(f))


def save_entry_to_csv(entry: dict) -> None:
    """Append a single entry to the CSV file, adding a header if it's new."""
    file_exists = CSV_FILE.is_file()
    CSV_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)
