# prompt: https://adventofcode.com/2022/day/6

from ...base import TextSolution, answer
# from typing import Tuple

class Solution(TextSolution):
    _year = 2022
    _day = 6

    @answer(1093)
    def part_1(self) -> int:
        
        WINDOW_SIZE = 4

        seen = []
        
        for idx, i in enumerate(self.input):
            seen.append(i)

            if len(seen)>=4:
                print(f"Window = {seen[-WINDOW_SIZE:]}")
                seen_set = set(seen[-WINDOW_SIZE:]) 
                print(seen_set)
                if len(seen_set)==WINDOW_SIZE:
                    ans = idx+1
                    break

        return ans

    @answer(3534)
    def part_2(self) -> int:
        WINDOW_SIZE = 14

        seen = []
        
        for idx, i in enumerate(self.input):
            seen.append(i)

            if len(seen)>=4:
                print(f"Window = {seen[-WINDOW_SIZE:]}")
                seen_set = set(seen[-WINDOW_SIZE:]) 
                print(seen_set)
                if len(seen_set)==WINDOW_SIZE:
                    ans = idx+1
                    break
        return ans

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
