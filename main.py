import json
from pathlib import Path


def note(title, body):
    x = {
        "title": title,
        "task": body
    }
    return x


def previewNotes():
    with open("notes.json", "r") as file:
        data = json.load(file)

    for item in data:
        print(json.dumps(item, indent=4))


def newNote():
    title = input("Please add note title: \n")
    body = input("Please insert note's body: \n")

    x = note(title, body)

    file_path = Path("notes.json")

    if file_path.exists():
        with open("notes.json", "r") as f:
            notes = json.load(f)

    else:
        notes = []

    notes.append(x)

    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)


print("Testing Notes Management")
print("-----------------------")

while True:
    user_input = input("Do you wish to: \n Preview notes: (1) \n Add a new note: (2) \n Quit? (Q) \n").lower()

    match user_input:

        case "1":
            previewNotes()

        case "2":
            newNote()

        case "q":
            break

        case _:
            print("Please refer to proper inputs")

print("Shutting down")

# Baseline. New note, preview notes. Completed

# Add pagination
# Note removal
# Note confirmation (re-input specific part of title or body before upload)
# Adjust specific notes
# Body line splits? User input base or auto? or *arg based input?

# Add note IDs (will make removal/adjustments easy)
# Input validation to prevent empty inputs
# Search notes? Either by title or body
# Add a way to mark notes as completed/unfinished?
# Create backup or add an export option
# Simple clear all
