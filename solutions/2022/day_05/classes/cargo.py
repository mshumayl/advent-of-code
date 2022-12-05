from .stack import Stack

class Cargo:
    def __init__(self, raw_input):
        print(raw_input)

        self.stack_list = []

        self.raw_crates = raw_input.split("\n\n")[0]
        self.stack_size = int(raw_input.split("\n\n")[0].strip()[-1])
        self.raw_procedures = raw_input.split("\n\n")[1]

        print(f"{self.raw_crates=}, \n{self.stack_size=} \n{self.raw_procedures=}")

    
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
                r = [val for val in r if (val != '--')]
            except ValueError:
                pass

            self.ordered_crates.append(r[::-1])
        
        print(f"{self.ordered_crates=}")
    
    
    def create_stacks(self):
        for i in range(self.stack_size):
            #Instantiate the stacks
            stack = Stack(self.ordered_crates[i])
            self.stack_list.append(stack)
            
    
    def parse_procedures(self):
        self.parse_procedures = []
        
        for i in self.raw_procedures.split("\n"):
            ct = int(i.split("move")[1].split("from")[0].strip())
            src = int(i.split("from")[1].split("to")[0].strip())
            tgt = int(i.split("to")[1].strip())
            # print(f"{ct=}, {src=}, {tgt=}")
            
            self.carry_procedure(ct, src, tgt)
    
    
    def carry_procedure(self, ct, src, tgt):
        temp_holder = []

        print(f"Moving {ct} crates from {src} to {tgt}")

        print("Current stack:")
        self.stack_list[src-1].display_stack()

        for i in range(ct):
            temp_holder.append(self.stack_list[src-1].decrease_stack())
        
        # print(f"{temp_holder=}")
        self.stack_list[tgt-1].increase_stack(temp_holder)
        
    
    def display_updated_stacks(self):
        for stk in self.stack_list:
            stk.display_stack()
            
    def get_top_crates(self):
        temp = []        
        for stk in self.stack_list:
            temp.append(stk.get_top_crate())
            
        self.top_crate_list = temp
        
        return ''.join(self.top_crate_list)