import csv
import os
from datetime import datetime

CSV_FILE = "journal.csv"
CSV_FIELDS = ["id", "message", "mood", "timestamp"]

MOOD_SYMBOLS = {
    "happy": ":)",
    "sad": ":(",
    "neutral": ":|",
}


def get_user_name() -> str:
    """Greet the user and collect their name."""
    print("Welcome to the Secret Journal!")
    name = input("Enter your name:\n\n")
    print(f"\nHello {name} 👋 Let's start journaling!")
    return name


def get_message() -> str:
    """Prompt for a journal message, retrying until it isn't empty."""
    message = input("Write your journal message: ").strip()
    while not message:
        message = input("Message can't be empty. Write your journal message: ").strip()
    return message


def get_mood() -> str:
    """Prompt for a mood, retrying until it's one of the known moods."""
    mood = input("How do you feel today? (happy/sad/neutral) ").strip().lower()
    while mood not in MOOD_SYMBOLS:
        mood = input("Invalid mood. Please enter happy, sad, or neutral: ").strip().lower()
    return mood


def create_entry(entry_id: int) -> dict:
    """Create a new journal entry with user input and validation."""
    message = get_message()
    mood = get_mood()

    return {
        "id": entry_id,
        "message": message,
        "mood": MOOD_SYMBOLS[mood],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }


def save_entry_to_csv(entry: dict) -> None:
    """Append a single entry to the CSV file, adding a header if it's new."""
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)


def load_entries() -> list:
    """Load all saved entries from the CSV file, if it exists."""
    if not os.path.isfile(CSV_FILE):
        return []

    with open(CSV_FILE, newline="") as f:
        return list(csv.DictReader(f))


def display_entries(entries: list) -> None:
    """Print entries in a readable, bordered list."""
    if not entries:
        print("No entries yet.")
        return

    print("------ Journal Entries ------")
    for entry in entries:
        date = entry["timestamp"].split(" ")[0]
        print(f"{entry['id']} | {entry['mood']} | {entry['message']} | {date}")
    print("-----------------------------")


def show_menu() -> str:
    """Display the main menu and return the user's raw choice."""
    return input(
        "\nWhat would you like to do?\n"
        "1. Write a new journal entry\n"
        "2. View saved entries\n"
        "3. Exit\n"
        "Enter your choice: "
    )


def main() -> None:
    get_user_name()

    while True:
        choice = show_menu()

        if choice == "1":
            entry_id = len(load_entries()) + 1
            entry = create_entry(entry_id)
            save_entry_to_csv(entry)
            print("Entry saved!")
        elif choice == "2":
            display_entries(load_entries())
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
