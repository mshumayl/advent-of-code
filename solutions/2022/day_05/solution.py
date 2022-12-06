# prompt: https://adventofcode.com/2022/day/5

from ...base import TextSolution, answer
from .classes.cargo import Cargo
import os
# from typing import Tuple

class Solution(TextSolution):
    _year = 2022
    _day = 5

    @answer("FWNSHLDNZ")
    def part_1(self) -> int:
        filename = "solutions//2022//day_05//input.txt"
        
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            my_input = f.read()
        
        cargo = Cargo(my_input)
        
        cargo.parse_crates()
        cargo.order_crates()
        cargo.create_stacks()
        cargo.parse_procedures()
        cargo.display_updated_stacks()
        
        answer = cargo.get_top_crates()
                         
        # print(f"\nThe final answer is {answer}")
        return answer

    @answer("RNRGDNFQG")
    def part_2(self) -> int:
        filename = "solutions//2022//day_05//input.txt"
        
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            my_input = f.read()
        
        cargo = Cargo(my_input)
        
        cargo.parse_crates()
        cargo.order_crates()
        cargo.create_stacks(type="crate_mover_9001")
        cargo.parse_procedures()
        cargo.display_updated_stacks()
        
        answer = cargo.get_top_crates()
                         
        # print(f"\nThe final answer is {answer}")
        return answer

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
