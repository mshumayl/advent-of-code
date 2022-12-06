class Stack:
    def __init__(self, crates: list):
        self.crates = crates

    def decrease_stack(self, count=0):
        # print(f"Removing {count} crates, one by one.")
        _temp = []
        for i in range(count):
            _temp.append(self.crates.pop())
        return _temp
        
    def increase_stack(self, new_crates: list):
        # print(f"Adding {new_crates[0]} to stack.")
        self.crates.extend(new_crates[0])
        
    def display_stack(self):
        # print(self.crates)
        pass
    
    def get_top_crate(self):
        return self.crates[-1]
    

class CrateMover9001(Stack):
    def decrease_stack(self, count):
        # print(f"Original: {self.crates}")
        _temp = self.crates[-count:]
        # print(f"Removing: {_temp}")
        self.crates = self.crates[:-count]
        # print(f"After removal: {self.crates}")
        return _temp