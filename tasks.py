#tasks.py

from datetime import datetime
import json

def enter_task():
    task_name = input('Enter task name: ')
    task_desk = input('Enter task description: ')

    days = input('Enter task days: ').split(',')
    days = [d.strip() for d in days]

    priority = input('Enter task priority (low, medium, high): ')

    print_task(task_name, task_desk, days, priority)

    return write_task_to_file(task_name, task_desk, days, priority)


def print_task(name, desc, days, priority):
    return print(f'You added new task - {name}. Created time: {datetime.now().isoformat()}\n'
                 f'Description: {desc}.\n'
                 f'Repeat the task by: {', '.join(days)}.\n'
                 f'Priority: {priority if priority == 'low' else priority.upper()}!'
                 )


def write_task_to_file(name, desk, days, priority):
    try:
        task_dict = {
                'name': f'{name}.',
                'desk': f'{desk}.',
                'repeat_on': f'{', '.join(days)}.',
                'priority': f'{priority}',
                'created_at': f'{datetime.now().isoformat()}'
                }
        with open('db.json', 'w', encoding='utf-8') as file:
            json.dumps(task_dict, indent=4)
            json.dump(task_dict, file)
    except:
        print('Ooops!')
    return