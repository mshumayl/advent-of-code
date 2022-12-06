# Day 6 (2022)

`Day 6: Tuning Trouble` ([prompt](https://adventofcode.com/2022/day/6))

## Part 1
For the first part of Day 6, we need to do some string processing. In short, the requirements are as such:
1. Go through the characters in the input string.
2. If all the characters in the previous 4 characters are unique, get the index of the first character in this window.

To check for the uniqueness of the previous 4 characters, I am using `set()`. Basically, the length of the set should also be 4 if all characters within the window is unique.

This can be implemented with the following code:
```
def part_1(self) -> int:
    
    seen = []
    
    for idx, i in enumerate(self.input):
        seen.append(i)

        if len(seen)>=4:
            print(f"Window = {seen[-4:]}")
            seen_set = set(seen[-4:]) 
            print(seen_set)
            if len(seen_set)==4:
                ans = idx+1
                break

    return ans
```

Which gives us an answer of `1093`.

## Part 2
For Part 2, instead of having a window size of 4 previous characters, we now need to check for uniqueness of the 14 previous characters.

This can be solved by generalizing the code we wrote for Part 1.

```
def part_1(self) -> int:
    
    WINDOW_SIZE = 14

    seen = []
    
    for idx, i in enumerate(self.input):
        seen.append(i)

        if len(seen)>=WINDOW_SIZE:
            print(f"Window = {seen[-WINDOW_SIZE:]}")
            seen_set = set(seen[-WINDOW_SIZE:]) 
            print(seen_set)
            if len(seen_set)==WINDOW_SIZE:
                ans = idx+1
                break

    return ans
```

Which returns our answer of `3534`.