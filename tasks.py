#tasks.py

from datetime import datetime

def added_tasks(name, desk, days, priority):
    print(f'You added new task - {name}. {datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")}')
    print(f'Description: {desk}.')
    print(f'Repeat the task by: {', '.join(days)}.')
    if priority == 'HIGH':
        print(f'Priority: {priority.upper()}!')
    else:
        print(f'Priority: {priority.lower()}.')

