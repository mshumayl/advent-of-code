# prompt: https://adventofcode.com/2022/day/9

from ...base import StrSplitSolution, answer
import sys

# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 9

    # @answer(6376)
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
            
            # print(f"{direction=}, {distance=}")
            
            match direction:
                case 'L':
                    headx -= distance
                case 'R':
                    headx += distance
                case 'D':
                    heady -= distance
                case 'U':
                    heady += distance
            
            # print(f"{headx=}, {heady=}")
            
            head_footprint.add(f"{headx},{heady}")


        # function to update location of tail based on head
        def move_tail(movement_vector: tuple):
            nonlocal tailx, taily, tail_footprint
            
            # print(f"\nMoving tail from ({tailx},{taily}) with vector ({movement_vector[0]},{movement_vector[1]})")
            tailx += movement_vector[0]
            taily += movement_vector[1]
        
            # print(f"Update tail coords: ({tailx},{taily})")            
            tail_footprint.add(f"{tailx},{taily}")
        
            
        for i in self.input:
            # print(i)
            
            head_dir, head_dist = i.split(" ")[0], int(i.split(" ")[1])
            
            for step in range(head_dist):
                move_head(head_dir, 1)
                
                abs_distx = abs(headx-tailx)
                abs_disty = abs(heady-taily)
                
                if (abs_distx>1 or abs_disty>1):
                    movement = get_movement()
                    move_tail(movement)
                else:
                    continue

        # print(head_footprint)
        # print(tail_footprint)
        # print(len(tail_footprint))
        
        pass

    # @answer(1234)
    def part_2(self) -> int:
        
        head_footprint = set()  
        tail_footprint = set()

        tail_footprint.add("0,0")

        
        all_coords = []
        
        for i in range(10):
            all_coords.append([0,0]) # starting coords
        
        print(all_coords)
        
        def move_head(direction):
            nonlocal all_coords
            
            match direction:
                case 'L':
                    mvmt = (-1,0)
                case 'R':
                    mvmt = (1,0)
                case 'D':
                    mvmt = (0,-1)
                case 'U':
                    mvmt = (0,1)
            
            all_coords[0][0] += mvmt[0]
            all_coords[0][1] += mvmt[1]

        
        def move_end(headx, heady, tailx, taily, end):
            nonlocal all_coords
            
            movex, movey = get_movement(headx, heady, tailx, taily)

            # print(f"{movex=}\n{movey=}\n\n")

            all_coords[end][0] += movex
            all_coords[end][1] += movey

            if end==9:
                tail_footprint.add(f"{tailx},{taily}")

        def get_movement(headx, heady, tailx, taily):
            distx = headx-tailx
            disty = heady-taily

            mvmt = (0,0)
        
            if abs(distx)>1 or abs(disty)>1:
                try: 
                    x_hat = distx/abs(distx) 
                except ZeroDivisionError:
                    x_hat = 0
                
                try:    
                    y_hat = disty/abs(disty) 
                except ZeroDivisionError:
                    y_hat = 0
                
                mvmt = (int(x_hat), int(y_hat))

            return mvmt            


        for i in self.input:
            head_dir, head_dist = i.split(" ")[0], int(i.split(" ")[1])
            
            for _ in range(head_dist):
                move_head(head_dir)
                
                for step in range(1, len(all_coords)):
                    is_last = False

                    headx, heady = all_coords[step-1]
                    tailx, taily = all_coords[step]
                    
                    move_end(headx, heady, tailx, taily, step)
            
        print(len(tail_footprint))

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
