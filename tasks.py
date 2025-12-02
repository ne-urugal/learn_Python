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

    def print_task(*args):
        printed = (
            f'You added new task - {task_name}. Created time: {datetime.now().isoformat()}\n'
            f'Description: {task_desc}.\n'
            f'Repeat the task by: {', '.join(rep_days)}.\n'
            f'Priority: {priority_task if priority_task == 'low' else priority_task.upper()}!'
        )

        return printed

    print(print_task())

    return



#def deleted_task():
#    name_task = input('Enter thr name of the task you want to delete: ')
#    for tasks in task_list: