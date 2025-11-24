#main.py
from tasks import added_tasks

def main():
    task_name = input('Enter task name: ')
    task_desk = input('Enter task deskription: ')

    days = input('Enter task days: ').split(',')
    days = [d.strip() for d in days]

    priority = input('Enter task priority (low, medium, high): ').upper()

    added_tasks(task_name, task_desk, days, priority)

    return (f'{task_name}'
            f'\n{task_desk}!'
            f'\n{days}'
            f'\n{priority}')

if __name__ == '__main__':
    main()
