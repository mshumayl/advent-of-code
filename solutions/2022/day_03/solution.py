# prompt: https://adventofcode.com/2022/day/3

from ...base import StrSplitSolution, answer
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 3


    # @answer(1234)
    def part_1(self) -> int:
 
        shared = []

        priority = "abcdefghijklmnopqrstuvwxyz"
        priority = priority + priority.upper()

        val = 1
        val_lst = []

        for i in priority:
            val_lst.append(val)
            val+=1
            
        prio_dict = dict(zip([key for key in priority], val_lst))
        
        print(prio_dict)
            
        for idx, i in enumerate(self.input):
            lst = [char for char in i]
            
            half = int(len(lst)/2)
            
            comp_1 = lst[:half]
            comp_2 = lst[half:]

            print(f"Rucksack {idx} half => {half}\n{comp_1=}\n{comp_2=}")
            
            for item in comp_1:
                if item in comp_2:
                    print(f"Shared: {item}")
                    shared.append(item)
                    break
                
        prio_item_val = []
        
        for shared_item in shared:
            prio_item_val.append(prio_dict[shared_item])
        
        print(sum(prio_item_val))
        
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
