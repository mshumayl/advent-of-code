from .stack import Stack

class Cargo:
    def __init__(self, raw_input):
        print(raw_input)

        self.stack_list = []

        self.raw_crates = raw_input.split("\n\n")[0]
        self.stack_size = int(raw_input.split("\n\n")[0].strip()[-1])
        self.raw_procedures = raw_input.split("\n\n")[1]

        print(f"{self.raw_crates=}, \n{self.stack_size=} \n{self.raw_procedures=}")

        # self.parse_crates()
        # self.order_crates()
        
    
    def parse_crates(self):
        self.unordered_crates = []
        
        for i in self.raw_crates.split("\n")[:-1]:
            i = i.replace("[", "").replace("]", "")
            self.unordered_crates.append(i)
            
        self.unordered_crates = [i.strip().split(" ") for i in self.unordered_crates]
        print(f"{self.unordered_crates=}")
    
        
    def order_crates(self):
        
        transposed = list(zip(*self.unordered_crates))
        self.ordered_crates = []
        
        for r in transposed:
            r = list(r)

            try:
                r = [val for val in r if val != '..']
            except ValueError:
                pass

            self.ordered_crates.append(r[::-1])

        
        print(f"{self.ordered_crates=}")
    
    
    def create_stacks(self):
        for i in range(self.stack_size):
            #Instantiate the stacks
            stack = Stack(self.ordered_crates)
            self.stack_list.append(stack)
            
    
    def parse_procedures(self):
        pass
    
    
    def carry_procedure():
        # increase stack, etc.
        pass