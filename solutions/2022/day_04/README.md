# Day 4 (2022)

`Day 4: Camp Cleanup` ([prompt](https://adventofcode.com/2022/day/4))

## Part 1
In simple words, the requirements for this part is as such:
1. For each line in the input, there are a pair of a set of numbers.
2. The numbers are the range of sections.
3. Get lines where the range for one section is a subset of the other.

So to start off, we'll need to parse each line of input in order to grab our range and create a list of integers using that range:

```
reorg_ct = 0

for i in self.input:
    
    elf_a_range = [int(i) for i in i.split(",")[0].split("-")]
    elf_b_range = [int(i) for i in i.split(",")[1].split("-")]
    
    elf_a_sections = [i for i in range(elf_a_range[0], elf_a_range[1]+1)]
    elf_b_sections = [i for i in range(elf_b_range[0], elf_b_range[1]+1)]

```

Here, `reorg_ct` is initalized outside of the loop to store the tally of rows that match our requirement.

Next, we need to check if a section is a subset of the other section. To do  this, we will need to know which of the two sections is smaller, as a subset needs to be smaller than the superset by definition.

We will also iterate through each element in the smaller section and check if it exists in the larger section. If it does, we'll store it in a temporary list called `same`. At the end of all iteration, we'll compare if `same` is equal to our smaller component to determine if our smaller component is a subset of the bigger component. If it is, we'll add one to our `reorg_ct` tally.

```
same = []

#Check which range is longer in each pair
if len(elf_a_sections) < len(elf_b_sections):
    for sect in elf_a_sections:
        if sect in elf_b_sections:
            same.append(sect)
        if same == elf_a_sections:
            reorg_ct+=1
elif len(elf_a_sections) > len(elf_b_sections):
    for sect in elf_b_sections:
        if sect in elf_a_sections:
            same.append(sect)
        if same == elf_b_sections:
            reorg_ct+=1
else:
    if elf_a_sections==elf_b_sections:
        reorg_ct+=1
```
By the end of the iterations, we will get a count of all lines which where one of the parts is a subset of the other.

## Part 2
The requirement for the second part is similar to that of the first part, except that now we will need to count all lines where there is _any_ overlap between the two parts.

This makes our code simpler as we no longer need to check whether a part is a full subset of the other part.

With everything else kept the same, our comparison algorithm is simply as the following:

```
for sect in elf_a_sections:
    if sect in elf_b_sections:
        reorg_ct+=1
        break
```
