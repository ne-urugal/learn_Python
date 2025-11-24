#main.py

from UsserClass import PrintingUser
from method import added_new_day
from method import added_new_note

WEEK = {
    ('monday', ): 'Monday',
    ('tuesday', ): 'Tuesday',
    ('wednesday', ): 'Wednesday',
    ('thursday', ): 'Thursday',
    ('friday', ): 'Friday',
    ('saturday', ): 'Saturday',
    ('sunday', ): 'Sunday',
}

user = PrintingUser(input('Enter the name of the user: '))

print(f"Hi, {user.name}!")

notes = added_new_note()

day = added_new_day()


if day in WEEK:
    print(f'\nUser: {user.name}')
    print(f'{WEEK[day]}: {notes}')
else:
    print('None!')