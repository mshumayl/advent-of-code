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

            i = i.split(" ")

            for idx, j in enumerate(i):
                i[idx] = int(j)

            res = i[0] - i[1]

            if res==0:
                point = i[1] + 3
            elif res==1 or res==-2:
                point = i[1]
            elif res==2 or res==-1:
                point = i[1] + 6
            else:
                raise ValueError
                        
            points.append(point)
    
        return(sum(points))
    
    
    @answer(12881)
    def part_2(self) -> int:
        
        dictionary = {
        "A": "1",
        "B": "2",
        "C": "3",
        "X": "0",
        "Y": "3",
        "Z": "6"
        }
        
        points = []

        def get_losing_option(opp_choice):
            if opp_choice==1:
                return 3
            else:
                return opp_choice-1
            
        def get_winning_option(opp_choice):
            if opp_choice==3:
                return 1
            else:
                return opp_choice+1

        for i in self.input:
            for key in dictionary.keys():
                i = i.replace(key, dictionary[key])

            i = i.split(" ")
            
            for idx, j in enumerate(i):
                i[idx] = int(j)

            if i[1]==0: #if to lose
                point = get_losing_option(i[0])
            elif i[1]==3: #if to draw
                point = i[0] + i[1]
            elif i[1]==6: #if to win
                point = get_winning_option(i[0]) + i[1]
            else: 
                raise ValueError

            points.append(point)
    
        return sum(points)

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
