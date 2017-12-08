# prompt: https://adventofcode.com/2017/day/5

from base import BaseSolution, InputTypes

class Solution(BaseSolution):
    def input_type(self):
        return InputTypes.INTARRAY

    def part_1(self):
        def inc(j):
            return 1

        return self.solve(inc)

    def part_2(self):
        def maybe_inc(j):
            if j >= 3:
                return -1
            else:
                return 1

        return self.solve(maybe_inc)

    def solve(self, f):
        total = 0
        i = 0
        arr = self.input[:]  # don't mutate input

        while -1 < i < len(arr):
            dest = i + arr[i]  # the new index
            arr[i] += f(arr[i])  # alter this before we leave
            i = dest  # jump
            total += 1

        return total
