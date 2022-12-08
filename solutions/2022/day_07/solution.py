# prompt: https://adventofcode.com/2022/day/7

from ...base import StrSplitSolution, answer
from collections import defaultdict
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 7

    # @answer(1234)
    def part_1(self) -> int:
        location = []
        map_dict = defaultdict(int)

        for line in self.input:
            command = line.split(" ")
            if len(command) == 3: # lines with `cd` commands have 3 elements
                if command[2]=="/": # if base dir
                    location = [] 
                elif command[2] == "..": # if go up one dir
                    location = location[:-1]
                else: # if command[2] is a dir name
                    if len(location) == 0: 
                        location.append(command[2])
                    else:
                        location.append(location[-1] + "/" + command[2]) # append current location
            else: # console output and `ls` lines have 2 elements
                size = 0
                print(f"{size=}")
                print(f"{command[0]=}")
                if not command[0].startswith("dir") and not command[0].startswith("$"): # remove dirs and `ls` lines
                    size = int(command[0])
                
                if size > 0:
                    for i in location: # iterate over all directories and sum
                        map_dict[i] += size 
                        print(f"Added {size=} to dir {i} (total={map_dict[i]})")
                        print(map_dict.items())
            print(f"{location=}")
            
        print(f"{map_dict=}")
        print(f"{location=}")
                
        
            
    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
