from UsserClass import printingUser
import method

user_1 = printingUser()

weak = {1: 'monday', 2: 'tuesday', 3: 'wednesday'}

new_notes = method.added_new_note(
    list(input('Enter the notes: ').split(', '))
    )

new_day = method.added_new_day(
    str.lower((input('Enter the day: ')))
)


if new_day == weak[1]:
    print(f'User: {user_1}. {new_day}: {new_notes}')