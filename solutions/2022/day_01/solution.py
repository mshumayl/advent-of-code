# prompt: https://adventofcode.com/2022/day/1

from ...base import TextSolution, answer
from typing import Tuple

class Solution(TextSolution):
    _year = 2022
    _day = 1

    @answer(68923)
    def part_1(self) -> int:
        lines = []
        
        with open(r"solutions\2022\day_01\input.txt", 'r') as f:
            for line in f:
                lines.append(line)
        
        separated = []

        slc_start = 0
        slc_end = 0

        for idx, i in enumerate(lines):
            if i == "\n":
                slc_end = idx
                separated.append(lines[slc_start:slc_end])
                slc_start = slc_end+1
            else:
                lines[idx] = int(i.replace('\n', ''))

        tally = []

        for idx, i in enumerate(separated):
            tally.append(sum(separated[idx]))

        ans = max(tally)

        return ans


    @answer(200044)
    def part_2(self) -> int:
        lines = []
        
        with open(r"solutions\2022\day_01\input.txt", 'r') as f:
            for line in f:
                lines.append(line)
        
        separated = []

        slc_start = 0
        slc_end = 0

        for idx, i in enumerate(lines):
            if i == "\n":
                slc_end = idx
                separated.append(lines[slc_start:slc_end])
                slc_start = slc_end+1
            else:
                lines[idx] = int(i.replace('\n', ''))

        tally = []

        for idx, i in enumerate(separated):
            tally.append(sum(separated[idx]))

        tally.sort(reverse=True)

        ans = sum(tally[:3])

        return ans

    # @answer((68923, 200044))
    # def solve(self) -> Tuple[int, int]:
    #     pass
