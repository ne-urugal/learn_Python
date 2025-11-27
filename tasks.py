#tasks.py

from datetime import datetime
import json

def enter_task():
    task_name = input('Enter task name: ')
    task_desk = input('Enter task description: ')

    days = input('Enter task days: ').split(',')
    days = [d.strip() for d in days]

    priority = input('Enter task priority (low, medium, high): ')

    return added_tasks(task_name, task_desk, days, priority)



def added_tasks(name, desk, days, priority):
    try:
        task = (f'You added new task - {name}. Time: {datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")}'
                f'Description: {desk}.'
                f'Repeat the task by: {', '.join(days)}.'
                f'Priority: {priority.upper() if priority == 'HIGH' else priority.lower()}!')
        with open('db.json', 'w', encoding='utf-8') as file:
            json.dumps(task, indent=4)
            json.dump(task, file)
    except:
        print('Ooops!')
    return

    '''print(f'You added new task - {name}. Time: {datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")}')
    print(f'Description: {desk}.')
    print(f'Repeat the task by: {', '.join(days)}.')

    if priority == 'HIGH':
        print(f'Priority: {priority.upper()}!')
    else:
        print(f'Priority: {priority.lower()}.')'''

