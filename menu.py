#menu.py
from traceback import print_last

from tasks import enter_task
from writetask import task_list


def menu_list():
    while True:
        print('MENU\n'
              '1. Show current tasks.\n'
              '2. Create a new task.\n'
              '3. Delete the task.\n'
              )
        user_choice = input('Select menu item: ')
        if user_choice == '1':
            print(f'Current tasks: {task_list}\n\n')
            printed_tasks = enter_task()
            print(printed_tasks)
        elif user_choice == '2':
            enter_task()
        #elif user_choice == '3':
            #delet_task()
        else:
            print('Incorrect value, pleas repeat the selection.')
