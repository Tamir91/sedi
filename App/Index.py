"""
    This file
"""
import sys
from typing import List

from Script import Script


class Index:
    options: List = []
    operands: List = []
    std_input: List = []
    script: str = ''

    def __init__(self, args: str) -> None:
        """
        initialization function
        :param args: received arguments of sed command
        """
        # obj = sys.stdin.readlines()
        # print(sys.stdin.readlines() is None)
        Script(args)

    def get_stdin(self) -> List[str]:
        """
        retrieve lines from std input
        :return: list of strings from std input
        """
        std_input = []
        try:
            std_input = sys.stdin.readlines()
            print(std_input)
        except KeyboardInterrupt:
            sys.stdout.flush()
            pass
        return std_input


