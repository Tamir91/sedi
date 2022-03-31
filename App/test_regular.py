import re

from typing import List

arg = ' -f -e - n "s/Jun [0 – 9][0 – 9]/DATE/g"'
string = 's/Jun [0 – 9][0 – 9]/DATE/g'

def create_flags_list(args: str) -> List:
    pattern = r'-[efn]'
    matchObj = re.findall(pattern, args)
    print(matchObj)
    return matchObj

def find_script(ars: str) -> str:
   pattern = '"'
   matchObj = re.split(pattern, arg)
   # print(matchObj[1])
   return matchObj[1]

def split_script(arg: str):
   pattern = '/'
   matchObj = re.split(pattern, arg)
   print(matchObj)

def execute_script(script: List):
   if len(script) > 3:
      print('>3')
   else:
      pass

def swap_strings(file_path: str, pattern: str, replace: str):
   with open(file_path, "r") as file:
      for line in file:
         string = re.sub(pattern, replace, line)
         print(string)

# find_script(arg)
# create_flags_list(arg)
split_script(string)
swap_strings('input.txt', 'Mar [0-9][0-9]', 'dec')