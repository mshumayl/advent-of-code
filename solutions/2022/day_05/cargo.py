from stack import Stack

class Cargo:
    def __init__(self, stack_count: int):
        self.stack_count = stack_count
        self.stack_list = []
        
        for stack in stack_count:
            self.stack_list.append(Stack())
            
    def initialize_cargo(self, raw_input):
        pass