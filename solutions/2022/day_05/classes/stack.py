class Stack:
    def __init__(self, crates: list):
        self.crates = crates

    def decrease_stack(self, count=0):
        _temp = []
        for i in range(count):
            _temp.append(self.crates.pop())
        return _temp
        
    def increase_stack(self, new_crates: list):
        self.crates.extend(new_crates)
        
    def display_stack(self):
        # print(self.crates)
        pass
    
    def get_top_crate(self):
        return self.crates[-1]
    

class CrateMover9001(Stack):
    def decrease_stack(self, count):
        return self.crates[-count]