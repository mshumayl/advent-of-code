# prompt: https://adventofcode.com/2022/day/10

from ...base import StrSplitSolution, answer
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 10

    # @answer(1234)
    def part_1(self) -> int:
        
        cumul_x = 0
        
        x_history = []
        signal_history = []
        
        for idx, i in enumerate(self.input):
            if i.startswith("noop"):
                x_history.append(cumul_x) # first cycle here
            
            elif i.startswith("addx"):
                add_x = int(i.split(" ")[1])
                
                x_history.append(cumul_x) # first cycle here
                
                cumul_x += add_x
                x_history.append(cumul_x) # second cycle here
                
                
        for jdx, j in enumerate(x_history):
            if jdx in [20, 60, 100, 140, 180, 220]:
                cyc = jdx
                current_x = int(x_history[jdx])
                signal_strength = current_x*cyc
                signal_history.append(signal_strength)
                print(f"{cyc}*{current_x}")

        print(sum(signal_history))        
        print(len(x_history)+1)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
