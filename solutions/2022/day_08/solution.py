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

    # tried_ans = [10160640, 998, 0, 235200, 262395, 201600] #235200 too low
    # @answer(1234)
    def part_2(self) -> int:

        trees_dict = defaultdict(dict)

        def get_tree_score(trees_input, transposed: bool=False):
            for rowidx, row in enumerate(trees_input):
                for idx, tree in enumerate(row): # exclusive at stop index
                    if len(row[:idx])==0:
                        left_score = 0
                    else:
                        left_trees = row[:idx]
                        left_trees.reverse() # because need to check from the tree that is nearest to the current tree
                        left_score = len(left_trees)
                    
                    if len(row[idx:])==len(row): # inclusive at start index
                        right_score = 0
                    else:
                        right_trees = row[idx+1:] # inclusive at start index
                        right_score = len(right_trees)

                    try:
                        for lidx, ltree in enumerate(left_trees):
                            if ltree>=tree:
                                left_score = lidx+1
                                break
                    except UnboundLocalError:
                        pass

                    try:
                        for ridx, rtree in enumerate(right_trees):
                            if rtree>=tree:
                                right_score = ridx=1
                                break
                    except UnboundLocalError:
                        pass

                    if transposed:
                        trees_dict[f"{rowidx},{idx}"]["top"] = int(left_score)
                        trees_dict[f"{rowidx},{idx}"]["bottom"] = int(left_score)
                    else:
                        trees_dict[f"{idx},{rowidx}"]["left"] = int(left_score)
                        trees_dict[f"{idx},{rowidx}"]["right"] = int(right_score)

        matrix = []

        for i in self.input:
            tree = [int(x) for x in i]
            matrix.append(tree)

        # tranpose input
        transposed_input = []
        for col in range(len(matrix[0])):
            cols = []
            for rw in range(len(matrix)):
                cols.append(matrix[rw][col])
            transposed_input.append(cols)

        get_tree_score(transposed_input, transposed=True)
        get_tree_score(matrix)

        all_scores = []

        for tree in trees_dict:
            tree_score = trees_dict[tree]["left"]*trees_dict[tree]["right"]*trees_dict[tree]["top"]*trees_dict[tree]["bottom"]
            all_scores.append(tree_score)
            print(tree)


        print(trees_dict.keys())
        print(trees_dict['0,1'])
        # assert trees_dict['0,0']["right"] == 2
        # assert trees_dict['0,0']["left"] == 0
        # assert trees_dict['0,0']["top"] == 
        # assert trees_dict['0,0']["bottom"] == 


        print(max(all_scores))
        print(all_scores)

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
