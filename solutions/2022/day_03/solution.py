# prompt: https://adventofcode.com/2022/day/3

from ...base import StrSplitSolution, answer
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 3


    # @answer(8053)
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
            
        for idx, i in enumerate(self.input):
            lst = [char for char in i]
            
            half = int(len(lst)/2)
            
            comp_1 = lst[:half]
            comp_2 = lst[half:]

            for item in comp_1:
                if item in comp_2:
                    shared.append(item)
                    break
                
        prio_item_val = []
        
        for shared_item in shared:
            prio_item_val.append(prio_dict[shared_item])
        
        return sum(prio_item_val)
        
    @answer(2425)
    def part_2(self) -> int:
        shared = []

        priority = "abcdefghijklmnopqrstuvwxyz"
        priority = priority + priority.upper()

        val = 1
        val_lst = []

        for i in priority:
            val_lst.append(val)
            val+=1
            
        prio_dict = dict(zip([key for key in priority], val_lst))
            
        group = []

        for i in range(0, len(self.input), 3):
            group.append(self.input[i: i+3])

        for i in group:
            elf_1 = i[0]
            elf_2 = i[1]
            elf_3 = i[2]
             
            for item in elf_1:
                if item in elf_2 and item in elf_3:
                    shared.append(item)
                    break
            
            prio_item_val = []
            
            for shared_item in shared:
                prio_item_val.append(prio_dict[shared_item])
            
        return sum(prio_item_val)

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
