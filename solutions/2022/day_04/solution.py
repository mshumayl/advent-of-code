# prompt: https://adventofcode.com/2022/day/4

from ...base import StrSplitSolution, answer
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 4

    @answer(456)
    def part_1(self) -> int:
        
        reorg_ct = 0
        
        for i in self.input:
            
            elf_a_range = [int(i) for i in i.split(",")[0].split("-")]
            elf_b_range = [int(i) for i in i.split(",")[1].split("-")]
            
            elf_a_sections = range(elf_a_range[0], elf_a_range[1]+1)
            elf_b_sections = range(elf_b_range[0], elf_b_range[1]+1)

            same = []
            
            #Check which range is longer in each pair
            if len(elf_a_sections) < len(elf_b_sections):
                for sect in elf_a_sections:
                    if sect not in elf_b_sections:
                        break
                    else:
                        same.append(sect)
                    if same == list(elf_a_sections):
                        reorg_ct+=1
                        pass
            elif len(elf_a_sections) > len(elf_b_sections):
                for sect in elf_b_sections:
                    if sect not in elf_a_sections:
                        break
                    else:
                        same.append(sect)
                    if same == list(elf_b_sections):
                        reorg_ct+=1
                        pass
            else:
                if elf_a_sections==elf_b_sections:
                    reorg_ct+=1
        
        return reorg_ct        

    @answer(808)
    def part_2(self) -> int:
        
        reorg_ct = 0
        
        for i in self.input:
            
            elf_a_range = [int(i) for i in i.split(",")[0].split("-")]
            elf_b_range = [int(i) for i in i.split(",")[1].split("-")]
            
            elf_a_sections = [i for i in range(elf_a_range[0], elf_a_range[1]+1)]
            elf_b_sections = [i for i in range(elf_b_range[0], elf_b_range[1]+1)]

            for sect in elf_a_sections:
                if sect in elf_b_sections:
                    reorg_ct+=1
                    break

        return reorg_ct

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
