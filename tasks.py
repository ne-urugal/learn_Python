#tasks.py
from datetime import datetime
from writetask import write_task_to_file, task_list


def enter_task():
    task_name = input('Enter task name: ')
    task_desc = input('Enter task description: ')

    rep_days = input('Enter task days: ').split(',')
    rep_days = [d.strip() for d in rep_days]

    priority_task = input('Enter task priority (low, medium, high): ')

    write_task_to_file(task_name, task_desc, rep_days, priority_task)

    return print_task(task_name, task_desc, rep_days, priority_task)


def print_task(name, desc, days, priority):
    printed = (
            f'You added new task - {name}. Created time: {datetime.now().isoformat()}\n'
            f'Description: {desc}.\n'
            f'Repeat the task by: {', '.join(days)}.\n'
            f'Priority: {priority if priority == 'low' else priority.upper()}!'
        )

    return printed



#def deleted_task():
#    name_task = input('Enter thr name of the task you want to delete: ')
#    for tasks in task_list: