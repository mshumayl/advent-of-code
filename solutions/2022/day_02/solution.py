# prompt: https://adventofcode.com/2022/day/2

from ...base import StrSplitSolution, answer
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 2

    
    @answer(13682)
    def part_1(self) -> int:

        dictionary = {
        "A": "1",
        "B": "2",
        "C": "3",
        "X": "1",
        "Y": "2",
        "Z": "3"
        }
        
        points = []

        for i in self.input:
            for key in dictionary.keys():
                i = i.replace(key, dictionary[key])

            i = i.split(' ')

            res = int(i[0])-int(i[1])

            if res==0:
                point = int(i[1]) + 3
            elif res==1 or res==-2:
                point = int(i[1])
            elif res==2 or res==-1:
                point = int(i[1]) + 6
            else:
                raise ValueError
                        
            points.append(point)
    
        return(sum(points))
    
    
    # @answer(1234)
    def part_2(self) -> int:
        
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
