#method.py
#Create notes using a list comprehension, combine them with commas,
#and remove extra spaces.
def added_new_note():
    notes = input('Enter the notes through the symbol ",": ')
    return [note.strip() for note in notes.split(',')]

def added_new_day():
    return input('Enter the new day in english: ').lower().strip()