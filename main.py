import json
from pathlib import Path


def note(new_id, title, body):
    x = {
        "id": new_id,
        "title": title,
        "task": body
    }
    return x


# Split off logic, delete will later utilise its own version to output only id + title.
def checkNotes():
    file_path = Path("notes.json")

    if file_path.exists():
        try:
            with open("notes.json", "r") as file:
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            print("Note format incorrect")
            return
    else:
        print("Note file missing, please add notes first.")
        return


def previewNotes():
    data = checkNotes()

    if not data:
        return

    for item in data:
        print(json.dumps(item, indent=4))

def deleteNote():
    print("Please enter id of note below")
    previewNotes()

def newNote():
    title = input("Please add note title: \n")
    body = input("Please insert note's body: \n")

    file_path = Path("notes.json")

    # preloads notes to later append new notes to.
    # if note doesn't exist or is formatted incorrectly creates blank
    if file_path.exists():
        try:
            with open("notes.json", "r") as f:
                notes = json.load(f)
        except json.JSONDecodeError:
            notes = []

    else:
        notes = []

    # Checks notes for all id's, assigns id based on final note
    # Most likely goes by highest, likely doesn't fill blanks
    if notes:
        last_id = max(note["id"] for note in notes)
        new_id = last_id + 1
    else:
        new_id = 1

    x = note(new_id, title, body)

    notes.append(x)

    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)


print("Testing Notes Management")
print("-----------------------")

while True:
    user_input = input("Do you wish to: \n Preview notes: (1) \n Add a new note: (2)"
                       " \n Delete a note: (3) \n Quit? (Q) \n").lower()

    match user_input:

        case "1":
            previewNotes()

        case "2":
            newNote()

        case "3":
            deleteNote()

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
