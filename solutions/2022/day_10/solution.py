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
        x_register = 1
        cycle = 0
        raw_display = ["." for _ in range(241)]
        
        def draw_crt():
            nonlocal x_register, cycle, addx
            
            if cycle in [x_register-1, x_register, x_register+1]:
                print(f"Draw pixel # at position {cycle}.")
                raw_display[cycle] = "#"
            else:
                print(f"Draw pixel . at position {cycle}.")

        
        for idx, i in enumerate(self.input):
            try:
                addx = int(i.split(" ")[1])
            except IndexError:
                pass

            if i.startswith("noop"):
                draw_crt()    
                cycle += 1
                print("Finish executing noop.")

            elif i.startswith("addx"):
                print(f"Begin executing addx {addx}")
                draw_crt()
                cycle+=1
                print(f"At {cycle=}. Current {x_register=}.")

                draw_crt()
                x_register += addx
                print(f"Added {addx} at {cycle=}. Current {x_register=}.")

                cycle+=1

            else:
                raise ValueError("Invalid input.")
        return raw_display
            
                

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
