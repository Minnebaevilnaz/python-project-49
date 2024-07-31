#!/usr/bin/env python3
from brain_games.cli import welcome_user


def welcome_message():
    print('Welcome to the Brain Games!')


def main():
    welcome_message()
    welcome_user()


if __name__ == '__main__':
    main()
