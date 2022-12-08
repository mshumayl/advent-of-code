# prompt: https://adventofcode.com/2022/day/8

from ...base import StrSplitSolution, answer
from collections import defaultdict
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 8

    # @answer(1234)
    def part_1(self) -> int:
        matrix = []
        visible_trees = set()
        
        # Load into matrix
        for i in self.input:
            tree = [int(x) for x in i]
            matrix.append(tree)

        # Transpose the matrix
        transposed_matrix = []
        for col in range(len(matrix[0])):
            cols = []
            for rw in range(len(matrix)):
                cols.append(matrix[rw][col])
            transposed_matrix.append(cols)


        print(matrix)
        print(transposed_matrix)

        def get_visible_trees(matrix, transposed: bool):
            for rix, row in enumerate(matrix):
                for cix, column in enumerate(row):
                    # Current tree
                    print(f"\nCurrent tree: {matrix[rix][cix]}")

                    if transposed:
                        cix, rix = rix, cix

                    right_diff = 0
                    left_diff = 0

                    # From left
                    print(f"Left: {matrix[rix][:cix]}")
                    try:
                        left_diff = int(matrix[rix][cix]) - max(matrix[rix][:cix])
                        print(f"Max: {max(matrix[rix][:cix])}")
                    except ValueError:
                        pass
                    # print(f"{left_diff=}")
                    
                    # From right
                    print(f"Right: {matrix[rix][cix+1:]}")
                    try:
                        right_diff = int(matrix[rix][cix]) - max(matrix[rix][cix+1:])
                        print(f"Max: {max(matrix[rix][cix+1:])}")
                    except ValueError:
                        pass
                    # print(f"{right_diff=}")
                    
                    if left_diff>=0 or right_diff>=0:
                        visible_trees.add(f"{rix},{cix}")

        
        get_visible_trees(matrix, False)
        get_visible_trees(transposed_matrix, True)
        
        ans = len(visible_trees)
        tried_ans = [3234, 3831, 1727, 5127]
        # print(f"\n{matrix=}")
        if ans not in tried_ans:
            print(f"\n{ans=}")
        else:
            print(f"\n{ans} has already been tried. Tried values -> {tried_ans}")
        # print(f"{visible_trees}")
        
    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
