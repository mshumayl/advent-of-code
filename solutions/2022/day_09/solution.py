# prompt: https://adventofcode.com/2022/day/9

from ...base import StrSplitSolution, answer
import sys

# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 9

    # @answer(1234)
    def part_1(self) -> int:

        print(sys.version)

        head_footprint = set()  
        tail_footprint = set()

        head_footprint.add("1,1")
        tail_footprint.add("1,1")

        headx = 1
        heady = 1
        tailx = 1
        taily = 1
        
        def get_movement():

            distx = headx-tailx
            disty = heady-taily

            try: 
                x_hat = distx/abs(distx) 
            except ZeroDivisionError:
                x_hat = 0
            
            try:    
                y_hat = disty/abs(disty) 
            except ZeroDivisionError:
                y_hat = 0
            
            movement = (int(x_hat), int(y_hat))
            
            return movement            


        def move_head(direction: str, distance: int):
            nonlocal headx, heady, head_footprint
            
            print(f"{direction=}, {distance=}")
            
            match direction:
                case 'L':
                    headx -= distance
                case 'R':
                    headx += distance
                case 'D':
                    heady -= distance
                case 'U':
                    heady += distance
            
            print(f"{headx=}, {heady=}")
            
            head_footprint.add(f"{headx},{heady}")


        # function to update location of tail based on head
        def move_tail(movement_vector: tuple):
            nonlocal tailx, taily, tail_footprint
            
            tailx += movement_vector[0]
            taily += movement_vector[1]
            
            tail_footprint.add(f"{tailx},{taily}")
        
            
        for i in self.input:
            print(i)
            
            head_dir, head_dist = i.split(" ")[0], int(i.split(" ")[1])
            
            move_head(head_dir, head_dist)
            movement = get_movement()
            move_tail(movement)

        # print(head_footprint)
        print(tail_footprint)
        print(len(tail_footprint))
        
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
