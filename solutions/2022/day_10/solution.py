# prompt: https://adventofcode.com/2022/day/10

from ...base import StrSplitSolution, answer
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 10

    # @answer(13180)
    def part_1(self) -> int:
        cumul_x = 1
        add_x = 0
        cycle = 0
        signal_history = []
        
        def update_if_interesting():
            nonlocal cumul_x, cycle, add_x
            interesting = [20, 60, 100, 140, 180, 220]
            
            if cycle in interesting:
                prev_x = cumul_x-add_x # to exclude non-finished cycles
                
                print(f"{cycle}*{prev_x}={cycle*(prev_x)}")
                signal_history.append(cycle*prev_x)
        
        for idx, i in enumerate(self.input):
            add_x = 0
            if i.startswith("noop"):
                cycle += 1
                update_if_interesting()    

            elif i.startswith("addx"):
                cycle += 1
                update_if_interesting()
                
                add_x = int(i.split(" ")[1])
                cumul_x += add_x

                cycle+=1
                update_if_interesting()

            else:
                raise ValueError("Invalid input.")
                
        return sum(signal_history)
            
                

    # @answer(1234)
    def part_2(self) -> int:
        
        register_x = 1
        add_x = 0
        current_x = 0
        cycle = 0
        signal_list = ["" for _ in range(241)]
        
        def update_if_overlap(cyc, x):
            if cyc in [x, x+1, x-1]:
                signal_list[cyc] = "#"
            else:
                signal_list[cyc] = "."            
                
        
        for idx, i in enumerate(self.input):
            add_x = 0
            if i.startswith("noop"):
                cycle += 1
                # update_if_overlap(cycle, register_x)
                signal_list[cycle] = str(current_x)    

            elif i.startswith("addx"):
                cycle += 1
                # update_if_overlap(cycle, register_x)
                signal_list[cycle] = str(current_x)    

                add_x = int(i.split(" ")[1])
                current_x += add_x

                cycle+=1
                # update_if_overlap(cycle, register_x)
                signal_list[cycle] = str(current_x)    


            else:
                raise ValueError("Invalid input.")
                
        display = ["".join(signal_list[i:i+40]) for i in range(0, 241, 40)]
    
        return display
            
                
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
