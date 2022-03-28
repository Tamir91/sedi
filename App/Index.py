"""
    This file
"""
import sys
from typing import List


class Index:
    option: str = ''
    operand: str = ''
    std_input: List = []

    def __init__(self, args) -> None:
        """
        initialization function
        :param args: received arguments of sed command
        """
        self.std_input = self.get_stdin()

        if self.is_option_valid(args):
            self.option = args[0]

        # if self.is_operand_valid(args[1]):
        #     self.operand = args[1]

        if self.option == '-e':
            self.option_e_received()

        elif self.option == '-f':
            self.option_f_received()

        else:
            self.option_not_exist()

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

    # TODO WIP
    # BUG
    def is_option_valid(self, option) -> bool:
        """
        valid received option
        :param option: of command sed
        :return: True if option is valid otherwise False
        """
        return option is not None and type(option) is str and option[0] == '-'

    # TODO WIP
    # BUG
    def is_operand_valid(self, operand) -> bool:
        """
        valid received operand
        :param operand: of command sed
        :return: True if operand is valid otherwise False
        """
        return operand is not None and type(operand) is str

    def option_e_received(self):
        """
        called when option -e received.
        :return:
        """
        print('option_e_received')

    def option_f_received(self):
        """
        called when option -f received.
        :return:
        """
        print('option_f_received')

    def option_not_exist(self):
        """
        called when invalid option received.
        :return:
        """
        print('sed: invalid option -- ', self.option)
