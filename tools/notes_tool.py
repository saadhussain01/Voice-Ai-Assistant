NOTES_FILE = "memory/notes.txt"

def add_note(note):
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    return "Note added."

def view_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            return f.read() or "No notes found."
    except FileNotFoundError:
        return "No notes found."
