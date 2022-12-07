# prompt: https://adventofcode.com/2022/day/7

from ...base import TextSolution, answer
# from typing import Tuple

class Solution(TextSolution):
    _year = 2022
    _day = 7


    dir_dict = {
        "dir asdf": {
            "sasd.log": 23,
            "dir opiu": {
                "my.txt": 1
            }
        },
        "dir ragkh": {
            "s": 2451,
            "sadg.po": 980 
        }
    }

    # @answer(1234)
    def part_1(self) -> int:
        
        command_block = []
        current_dir = []
        all_dirs = set()
        
        all_files = []
        
        map_dict = {}
        
        for i in self.input.split("$"):
            command_block.append(i)
            
        # print(command_block)

        for i in command_block[1:]:
            if i.strip().startswith("cd"):
                j = ''.join(i.strip("\n").strip())
                if j.endswith(".."):
                    current_dir = current_dir[:-1]
                else:
                    current_dir.append(j.split(" ")[-1])
            else:
                j = i.strip().split("\n")
                j[0] = ''.join(current_dir)
                all_files.append(j)
            
            # print(f"{j=}")
            # print(f"{current_dir=}")
            all_dirs.add(''.join(current_dir))

        # print(f"{all_files=}")
        print(f"{all_dirs=}")

        for idx, f in enumerate(all_files):
            for kidx, k in enumerate(f):
                if k.startswith("dir"):
                    all_files[idx][kidx] = str(f[0]) + "".join(k.split(" ")[-1])
        
        
        for i in all_files:
            terminal_leaf = []
            for j in i[1:]:
                if j.startswith("/") and isinstance(j, str):
                    break
                else:
                    terminal_leaf.append(j)

            map_dict[i[0]] = terminal_leaf
            
                
        print("Completed")
        print(f"{all_files=}")        

        print("Dictionary")
        print(f"{map_dict=}")        
        
            
    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
