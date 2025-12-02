#main.py
import os

from menu import menu_list
from os import mkdir, path


def main():
    if not path.isdir('tasks'):
        mkdir('tasks')
    while True:
        menu_list()



if __name__ == '__main__':
    main()
