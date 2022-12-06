# Day 5 (2022)

`Day 5: Supply Stacks` ([prompt](https://adventofcode.com/2022/day/5))

## Part 1
For the first part of our challenge, we were tasked with the following:
1. Parse the input into two parts,(1) initial state of the stacks and (2) procedure to carry out on the stacks.
2. Parse the stacks into a programmable data structure.
3. Parse the procedures and carry them out for our stacks.

I tried to solve today's challenge with some basic OOP. A flesh-out of the structure of our classes would be as the following.

We will need a `Stack` class which represents a stack of crates. This class will be responsible for handling operations like initializing the crates in the stack, adding crates in the stack, and removing crates from the stack. We also need a method to give us the top crate in the stack i.e. our answer. 

```
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
    
    def get_top_crate(self):
        return self.crates[-1]
```

For this part, we are required to carry out the crate movements based on LIFO (Last In First Out). Hence, our `decrease_stack()` method pops the last element of each array iteratively, and feeds it into a list. This list can be fed directly into `increase_stack()`

Next, we will need a `Cargo` class which represents a collection of stacks, and contains methods to orchestrate the operations needed based on the procedure in our input. It is also responsible to instantiate our stacks. Details are commented:

```

class Cargo:
    def __init__(self, raw_input):
        # print(raw_input)

        self.stack_list = []

        self.raw_crates = raw_input.split("\n\n")[0]
        self.stack_size = int(raw_input.split("\n\n")[0].strip()[-1])
        self.raw_procedures = raw_input.split("\n\n")[1]

        # print(f"{self.raw_crates=}, \n{self.stack_size=} \n{self.raw_procedures=}")


    def parse_crates(self):
        self.unordered_crates = []
        
        print(self.raw_crates)
        
        for i in self.raw_crates.split("\n")[:-1]:
            temp = []
            for j in i[1:-1:4]: # Hard-coded step-size 
                temp.append(j)
            self.unordered_crates.append(temp)

        print(f"{self.unordered_crates=}")
    
        
    def order_crates(self):
        # Transpose the list
        transposed = list(zip(*self.unordered_crates))
        self.ordered_crates = []
        
        # Clean up after transposing 
        for r in transposed:
            r = list(r)

            # Remove elements that are empty spaces
            try:
                r = [val for val in r if (val != " ")]
            except ValueError:
                pass

            # Reverse list to accommodate the usage of list methods
            self.ordered_crates.append(r[::-1])
        
        print(f"{self.ordered_crates=}")
    
    
    def create_stacks(self, type=None):
        for i in range(self.stack_size):

            #Instantiate the stacks based on type required -- this is for Part 2
            if type == "crate_mover_9001":
                stack = CrateMover9001(self.ordered_crates[i])
            else:
                # Method for Part 1
                stack = Stack(self.ordered_crates[i])
            self.stack_list.append(stack)
        
    
    def parse_procedures(self):
        self.parse_procedures = []
        
        # Carry out procedures while parsing to minimize time-space complexity
        for i in self.raw_procedures.split("\n"):
            ct = int(i.split("move")[1].split("from")[0].strip())
            src = int(i.split("from")[1].split("to")[0].strip())
            tgt = int(i.split("to")[1].strip())
            # print(f"{ct=}, {src=}, {tgt=}")
            
            self.carry_procedure(ct, src, tgt)
    
    
    def carry_procedure(self, ct, src, tgt):
        temp_holder = []

        # print(f"Moving {ct} crates from {src} to {tgt}")

        # print("Current stack:")
        self.stack_list[src-1].display_stack()

        temp_holder.append(self.stack_list[src-1].decrease_stack(ct))
        
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
```

In our main `solution.py` class, we'll have the following simple method calls:

```
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
```

This gives us the answer of `FWNSHLDNZ`.

## Part 2
For the second part, instead of moving the crates based on LIFO, we'll be able to do it with FIFO (First In First Out). As we have implemented our `Stack` class before, we can change how we reduce our crates by inheriting `Stack` and only overriding the `decrease_stack()` method.

```
class CrateMover9001(Stack):
    def decrease_stack(self, count):
        _temp = self.crates[-count:]
        self.crates = self.crates[:-count]
        return _temp
```

Also, as we have implemented in our `Cargo` class before, we can instantiate `CrateMover9001` by having passing a `type` parameter when instantiating `Cargo` in our main program. This way, we can instantiate our stacks based on the `type` parameter.

```
def create_stacks(self, type=None):
    for i in range(self.stack_size):
        #Instantiate the stacks
        if type == "crate_mover_9001":
            stack = CrateMover9001(self.ordered_crates[i])
        else:
            stack = Stack(self.ordered_crates[i])
        self.stack_list.append(stack)
```

Also, as we have overridden our `decrease_stack()` method, we do not need to change anything on our `carry_procedure()` method in `Cargo` as it carries the right method based on the class of the current stack.

```
def carry_procedure(self, ct, src, tgt):
    temp_holder = []

    temp_holder.append(self.stack_list[src-1].decrease_stack(ct))
    self.stack_list[tgt-1].increase_stack(temp_holder)
```

Running the following main code,

```
def part_2(self) -> int:
    filename = "solutions//2022//day_05//input.txt"
    
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        my_input = f.read()
    
    cargo = Cargo(my_input)
    
    cargo.parse_crates()
    cargo.order_crates()
    cargo.create_stacks(type="crate_mover_9001") # Define which type to instantiate
    cargo.parse_procedures()
    cargo.display_updated_stacks()
    
    answer = cargo.get_top_crates()
                        
    return answer
```

we get our final answer of `RNRGDNFQG`!
