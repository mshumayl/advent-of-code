class Stack:

    def __init__(self, crates: list):
        self.crates = crates

    def decrease_stack(self):
        return self.crates.pop()
        
    def increase_stack(self, new_crates: list):
        self.crates.extend(new_crates)
        
    def display_stack(self):
        # print(self.crates)
        pass
    
    def get_top_crate(self):
        return self.crates[-1]