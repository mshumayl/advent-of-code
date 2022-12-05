class Stack:

    def initialize_stack(self, crates: list):
        self.crates = crates

    def reduce_stack(self):
        self.crates.pop()
        
    def increase_stack(self, new_crate: str):
        if len(new_crate) != 1:
            raise ValueError("Crates can only be represented with one character.")
        self.crates.append(new_crate)
        