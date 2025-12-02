#main.py
import os

from menu import menu_list
from os import mkdir, path


def main():
    try:
        path.isdir('tasks')
    except:
        mkdir('tasks')
    while True:
        menu_list()



if __name__ == '__main__':
    main()
