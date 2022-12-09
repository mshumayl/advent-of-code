# prompt: https://adventofcode.com/2022/day/8

from ...base import StrSplitSolution, answer
from collections import defaultdict
# from typing import Tuple

class Solution(StrSplitSolution):
    _year = 2022
    _day = 8

    # @answer(1870)
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

        # print(matrix)
        # print(transposed_matrix)

        def get_visible_trees(matrix, transposed: bool):
            for rix, row in enumerate(matrix):
                for cix, column in enumerate(row):
                    # Current tree
                    # print(f"\nCurrent tree: {matrix[rix][cix]}")

                    right_diff = False
                    left_diff = False

                    # From left
                    # print(f"Left: {matrix[rix][:cix]}")
                    try:
                        left_diff = int(matrix[rix][cix]) > max(matrix[rix][:cix])
                        # print(f"Max: {max(matrix[rix][:cix])}")
                        # print(left_diff)
                    except ValueError:
                        left_diff=True
                        pass
                    # print(f"{left_diff=}")
                    
                    # From right
                    # print(f"Right: {matrix[rix][cix+1:]}")

                    try:
                        right_diff = int(matrix[rix][cix]) > max(matrix[rix][cix+1:])
                        # print(f"Max: {max(matrix[rix][cix+1:])}")
                        # print(right_diff)
                    except ValueError:
                        right_diff=True
                        pass
                    # print(f"{right_diff=}")
                    
                    if left_diff or right_diff:
                        # print("Visible!")
                        if transposed:
                            visible_trees.add(f"{rix},{cix}")
                        else:
                            visible_trees.add(f"{cix},{rix}")

        get_visible_trees(matrix, False)
        get_visible_trees(transposed_matrix, True)
        
        ans = len(visible_trees)
        # print(f"{visible_trees}")

        return ans
        
    # @answer(1234)
    def part_2(self) -> int:

        matrix = []
        visible_trees = defaultdict(lambda: 1)
        
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

        def get_farthest_taller_tree(matrix, transposed: bool):
            for rix, row in enumerate(matrix):
                for cix, column in enumerate(row):
                    # Current tree
                    # print(f"\nCurrent tree: {matrix[rix][cix]}")

                    right_diff = False
                    left_diff = False

                    # From left
                    # print(f"Left: {matrix[rix][:cix]}")

                    current_tree = matrix[rix][cix]

                    left_trees = matrix[rix][:cix]
                    right_trees = matrix[rix][cix+1:]

                    print(current_tree)
                    print(left_trees)
                    print(right_trees)
                    print()

                    if len(left_trees)==0: # trees on edge
                        dist_left = 1
                    else:
                        dist_left = len(left_trees)

                    if len(right_trees)==0: # trees on edge
                        dist_right = 1
                    else:
                        dist_right = len(right_trees)


                    try:
                        if current_tree<max(left_trees):
                            idx_max = left_trees.index(max(left_trees))
                            score_left = len(left_trees[idx_max:])
                        else: # if no trees blocking
                            score_left = len(left_trees)
                    except ValueError: # array length 0, default to 0
                        score_left = 0

                    
                    try:
                        if current_tree<max(right_trees):
                            idx_max = right_trees.index(max(right_trees))
                            score_right = len(right_trees[:idx_max-1])
                        else: # if no trees blocking
                            score_right = len(right_trees)
                    except ValueError: # array length 0, default to 0
                        score_right = 0

                    

                    if transposed:
                        visible_trees[f"{rix}{cix}"] *= score_right*score_left
                        print(f"{rix}, {cix}")
                        print(f"{score_right=}")
                        print(f"{score_left=}\n")
                    else:
                        visible_trees[f"{cix}{rix}"] *= score_right*score_left
                        print(f"{cix}, {rix}")
                        print(f"{score_right=}")
                        print(f"{score_left=}\n")
        
        get_farthest_taller_tree(matrix, False)
        get_farthest_taller_tree(transposed_matrix, True)
        
        # print(visible_trees)

        tried_ans = [998, 0]

        ans = max(visible_trees.values())
        
        if ans in tried_ans:
            print(f"Already tried {ans}. Tried values -> {tried_ans}")
        else:
            print(ans)

        # print(len(visible_trees))

        print(visible_trees)
        assert ans==6

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
