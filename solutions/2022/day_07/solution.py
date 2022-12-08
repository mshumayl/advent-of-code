# prompt: https://adventofcode.com/2022/day/7

from ...base import StrSplitSolution, answer
from collections import defaultdict
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 7


    @answer(1449447)
    def part_1(self) -> int:
        location = []
        dir_dict = defaultdict(int)

        for line in self.input:
            command = line.split(" ")
            if len(command) == 3: # lines with `cd` commands have 3 elements
                if command[2]=="/": # if base dir
                    location = ["/"] 
                elif command[2] == "..": # if go up one dir
                    location = location[:-1]
                else: # if command[2] is a dir name
                    if len(location) == 0: 
                        location.append(command[2])
                    else:
                        location.append(location[-1] + "/" + command[2]) # append current location
            else: # console output and `ls` lines have 2 elements
                size = 0
                # print(f"{size=}")
                # print(f"{command[0]=}")
                if not command[0].startswith("dir") and not command[0].startswith("$"): # remove dirs and `ls` lines
                    size = int(command[0])
                
                if size > 0:
                    for i in location: # iterate over all directories and size_sum
                        dir_dict[i] += size 
                        # print(f"Added {size=} to dir {i} (total={dir_dict[i]})")
                        # print(dir_dict.items())
            # print(f"{location=}")
            
        # print(f"{dir_dict=}")
        # print(f"{location=}")
        
        size_sum = 0 

        for key, value in dir_dict.items():
            if value<100000:
                size_sum+=value
        
        return size_sum
            
            
    @answer(8679207)
    def part_2(self) -> int:
        location = []
        dir_dict = defaultdict(int)

        for line in self.input:
            command = line.split(" ")
            if len(command) == 3: # lines with `cd` commands have 3 elements
                if command[2]=="/": # if base dir
                    location = ["/"] 
                elif command[2] == "..": # if go up one dir
                    location = location[:-1]
                else: # if command[2] is a dir name
                    if len(location) == 0: 
                        location.append(command[2])
                    else:
                        location.append(location[-1] + "/" + command[2]) # append current location
            else: # console output and `ls` lines have 2 elements
                size = 0
                # print(f"{size=}")
                # print(f"{command[0]=}")
                if not command[0].startswith("dir") and not command[0].startswith("$"): # remove dirs and `ls` lines
                    size = int(command[0])
                
                if size > 0:
                    for i in location: # iterate over all directories and size_sum
                        dir_dict[i] += size 
                        # print(f"Added {size=} to dir {i} (total={dir_dict[i]})")
                        # print(dir_dict.items())
            # print(f"{location=}")
            
        # print(f"{dir_dict=}")
        # print(f"{location=}")
        
        available_space = 70000000 - dir_dict["/"]
        required_space = 30000000 - available_space

        sufficient_dirs = []

        for key, val in dir_dict.items():
            if val>required_space:
                sufficient_dirs.append(val)

        ans = min(sufficient_dirs)

        return ans



    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
