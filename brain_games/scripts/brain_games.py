#!/usr/bin/env python3
import sys
import os

# Добавить путь к корневой директории проекта в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from brain_games.cli import welcome_user
def welcome_message():
    print('Welcome to the Brain Games!')


def main():
    welcome_message()
    welcome_user()

if __name__ == '__main__':
    main()
