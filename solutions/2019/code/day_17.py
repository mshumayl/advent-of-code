# prompt: https://adventofcode.com/2019/day/17

from typing import List

from .intcode import IntcodeComputer, IntcodeSolution

SCAFFOLD_CHARS = {"#", "v", "^", "<", ">"}


class Diagram:
    # pylint: disable=invalid-name

    diagram: List[List[str]] = [[]]
    # [ [ 0,0 | 0,1 | 0,2 ],
    #   [ 1,0 | 1,1 | 1,2 ]
    #   [ 2,0 | 2,1 | 2,2 ]]

    def is_saffold(self, x, y):
        return self.diagram[y][x] in SCAFFOLD_CHARS

    def add_point(self, ascii_code):
        if ascii_code == 10:
            self.diagram.append([])
        else:
            self.diagram[-1].append(chr(ascii_code))
            # self.map_[(self.pos_x, self.pos_y)] = chr(ascii_code)

    def is_valid_coordinate(self, x, y):
        if x < 0 or y < 0:
            return False

        if y >= len(self.diagram):
            return False

        # this could honestly just look at the first row since the diagram is rectangular
        if x >= len(self.diagram[y]):
            return False

        return True

    def is_intersection(self, x, y):
        # each cardinal direction is also a piece of scaffold
        for pair in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if not (self.is_valid_coordinate(*pair) and self.is_saffold(*pair)):
                return False
        return True

    def get_intersections(self):
        intersections = []
        for y, row in enumerate(self.diagram):
            for x, _ in enumerate(row):
                if self.is_saffold(x, y) and self.is_intersection(x, y):
                    intersections.append((x, y))
        return intersections

    def pretty(self) -> str:
        return "\n".join(["".join(row) for row in self.diagram])


class Solution(IntcodeSolution):
    year = 2019
    number = 17

    def part_1(self):
        computer = IntcodeComputer(self.input)
        computer.run()
        diag = Diagram()
        for ascii_code in computer.output:
            diag.add_point(ascii_code)

        return sum([x * y for x, y in diag.get_intersections()])

    def part_2(self):
        pass

    def solve(self):
        pass
