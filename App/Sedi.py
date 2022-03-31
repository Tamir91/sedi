#! /usr/bin/python3

""" This file is entry point to the App. """
import sys

from Index import Index


def main(args=None):
    if not args:
        print('No arguments')
    else:
        print(args)
        Index(args)


if __name__ == "__main__":

    sys.exit(main(sys.argv[1:]))
    # sys.exit(main(['-e', 's/Mar [0-9][0-9]/DATE/g', '/home/ty/PycharmProjects/sedi/App/input.txt']))
