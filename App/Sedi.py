#! /usr/bin/python3

""" This file is entry point to the App. """
import os
import sys

from Index import Index


def main(args=None):
    if not args:
        print('No arguments')
    elif len(args) == 1:
        print('1 args')
        Index(args)

    elif len(args) == 2:
        print('2 args')
    else:
        print('Oh, So many args!')


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
