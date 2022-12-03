# Day 3 (2022)

`Day 3: Rucksack Reorganization` ([prompt](https://adventofcode.com/2022/day/3))

## Part 1
Distilling the requirements, we essentially need to carry out the following operations:
1. Split each line from input into half.
2. Compare first half with the second half to get a common character.
3. Convert this common character into the value defined.
4. Sum this value across all lines.

So let's start by defining the 'priority' dictionary, with the keys being the characters `[a-zA-Z]` and the values being `1, 2, ..., 52` respectively. 

```
priority = "abcdefghijklmnopqrstuvwxyz"
priority = priority + priority.upper()

val = 1
val_lst = []

for i in priority:
    val_lst.append(val)
    val+=1
    
prio_dict = dict(zip([key for key in priority], val_lst))

```

In the above code, a list of values (`val_lst`) were created by iterating through all elements in the `priority` string. This way, if we have future key values added, we can still assign the list of values dynamically. We also created the dict by zipping together the priority keys (converted to a list) with `val_lst`.

Next, let's split each line of input into half, and get the common character between each halves.

```
shared = []

for idx, i in enumerate(self.input):
    lst = [char for char in i]
    
    half = int(len(lst)/2)
    
    comp_1 = lst[:half]
    comp_2 = lst[half:]

    for item in comp_1:
        if item in comp_2:
            shared.append(item)
            break
```
In the above code, each input line is separated into two by slicing the input line with `int(len(lst)/2)`. Then, each half is compared with each other by looping through a half and checking if an element exists in the other half.

Lastly, we can get the value of the common item based on our priority dictionary and sum across all common characters.

```
prio_item_val = []

for shared_item in shared:
    prio_item_val.append(prio_dict[shared_item])

return sum(prio_item_val)
```

Based on our input, this gives us an answer of `8053`.

## Part 2
For the second part of the Day 3 quiz, we will need to make some modifications to our solution from Part 1. Instead of comparing one half of each line with its other half of the same line, we now need to compare and extract  between 3 lines.

So we will have to separate our lines of input into groups of three. We can achieve this with the following code:

```
group = []

for i in range(0, len(self.input), 3):
    group.append(self.input[i: i+3])

```

The above code gives us a list, with each element of the list being a group of three lines of our input.

Now, with a slight adjustment to the code from Part 1, we can make the comparison between all members of a group with the following code:

```
for i in group:
    elf_1 = i[0]
    elf_2 = i[1]
    elf_3 = i[2]
        
    for item in elf_1:
        if item in elf_2 and item in elf_3:
            shared.append(item)
            break
```

We can use the same code from Part 1 to convert the common item into a priority value and sum across all groups.

```
    prio_item_val = []

    for shared_item in shared:
        prio_item_val.append(prio_dict[shared_item])

return sum(prio_item_val)
```

Which gives us a value of `2425` based on our input.