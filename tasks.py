#tasks.py

def added_tasks(name, desk, days, priority):
    print(f'You added new task - {name}')
    print(f'Deskription: {desk}')
    print(f'Repeat the task by: {', '.join(days)}')
    if priority == 'HIGH':
        print(f'Priority: {priority}!')
    else:
        print(f'Priority: {priority}')

