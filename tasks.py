#tasks.py

def added_tasks(name, desk, days, priority):
    print(f'You added new task - {name}.')
    print(f'Description: {desk}.')
    print(f'Repeat the task by: {', '.join(days)}.')
    if priority == 'HIGH':
        print(f'Priority: {priority.upper()}!')
    else:
        print(f'Priority: {priority.lower()}.')

