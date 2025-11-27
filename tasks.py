#tasks.py

from datetime import datetime
import json

def enter_task():
    task_name = input('Enter task name: ')
    task_desk = input('Enter task description: ')

    days = input('Enter task days: ').split(',')
    days = [d.strip() for d in days]

    priority = input('Enter task priority (low, medium, high): ')

    return write_task_to_file(task_name, task_desk, days, priority)



def write_task_to_file(name, desk, days, priority):
    try:
        task_dict = {
                'name': f'You added new task - {name}.',
                'desk': f'Description: {desk}.',
                'days': f'Repeat the task by: {', '.join(days)}.',
                'priority': f'Priority: {priority.upper() if priority == 'HIGH' else priority.lower()}!',
                'time': f'Add time: {datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")}'
                }
        with open('db.json', 'w', encoding='utf-8') as file:
            json.dumps(task_dict, indent=4)
            json.dump(task_dict, file)
    except:
        print('Ooops!')
    return