"""
    this class work with provided script
"""
import os.path
import sys
from typing import List
import re


class Script:

    def __init__(self, argv: List):
        self.args: str = ''
        self.options: List = []
        self.script: str = ''
        self.file_path = ''
        self.separated_script: List = []

        self.argv = argv

        self.calculate()

    def calculate(self):
        self.options = self.create_options_list(self.argv)
        self.script = self.find_script_in_string(self.argv)
        self.file_path = self.find_file_path(self.argv)
        self.separated_script = self.split_script(self.script)
        self.run_script(self.separated_script, self.file_path)

    def create_options_list(self, argv: List) -> List:
        string = ' '.join(argv)
        pattern = r'-[efn]'
        match_obj = re.findall(pattern, string)
        print("create_options_list: ", match_obj)
        return match_obj

    def find_script_in_string(self, argv: List) -> str:
        suggestions = [i for i in argv if not i.startswith('-')]
        return None if not suggestions else suggestions[0]

    def find_file_path(self, argv: List) -> str:
        suggestions = [i for i in argv if i.endswith('.txt')]
        return None if not suggestions else suggestions[0]

    def split_script(self, script: str) -> List:
        pattern = '/'
        match_obj = re.split(pattern, script)
        print("split_script: ", match_obj)
        return match_obj

    def run_script(self, script: List, file_path: str):
        if script is not None:
            if script[0] == 's':  # we go swap substring with another string
                self.swap_string_with_substring(script, file_path)

    def swap_string_with_substring(self, script: List, file_path: str):
        if file_path and os.path.exists(file_path) and os.path.isfile(file_path):

            with open(file_path, 'r') as file:
                for line in file:
                    self.swap_and_print(script, line)

        else:
            print('file not found')
            std_input: List = self.get_stdin()

            for line in std_input:
                self.swap_and_print(script, line)


    def get_stdin(self) -> List:
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

    def swap_and_print(self, script: List, line: str):
        if script is not None:

            line = line.rstrip()  # remove new line character from a tail
            if len(script) == 4 and script[3] == 'g':  # Swapping all occurrences
                string = re.sub(script[1], script[2], line, count=0)
                print(string)

            elif len(script) == 4 and script[3] == '':  # Swapping first occurrence
                string = re.sub(script[1], script[2], line, count=1)
                print(string)
