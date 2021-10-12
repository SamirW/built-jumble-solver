# Jumble Solver Coding Challenge

Author: Samir Wadhwania  
Date: 12 Oct, 2021

## Intro

This is my (naive) implementation of a Jumble Solver for the Built Robotics Coding Challenge. Below, I'll outline the algorithm, assumptions, complexity analysis, and comments.

## Usage

Basic CLI functionality:

```
python3 jumble.py hireme
reme
eire
emir
heir
...
```

## Implementation

### Assumptions

* CLI is sufficient, and no one is trying to break the code via CLI (only basic input cleaning takes place)
* If the letters make a word, you want that word returned as well
* The shortest word in the dictionary is at least 2 letters long

### Algorithm

1. Create a dictionary hashmap with all words in a provided word list
2. Create all letter permutations of length 2 to n possible from provided letters 
3. Check permutations to see if they exist in dictionary
4. Return (print) valid words

### Packages

I used *itertools.permutations* to iterate through permuations of letters of length 2 to n. This made the implementation quite straightforward with the function `itertools.permutations(letters, length)`.

### Complexity Analysis

There are two (three, optionally) driving factors for time-complexity of the algorithm. Firstly, we run `itertools.permutations` which finds the `n!` permutations of length `n`. Secondly, because we need to loop from length `2 to n`, we will be looking at a complexity of `n*n!`. Since we (optionally/unnecessarily) also sort our output answer list, we could also consider `.sort()` having a runtime of `nlogn` (but the `n` here is the length of the output list). Because this is so much lower than `n!`, we can ignore and leave the complexity at `O(n*n!)`.

Space-wise, we are using a generator to avoid storing all `n!` permutations even if they are not valid words. However, in a worst case where all permutations of a string of letters are valid (think a word list dictionary of all permutations), then we would also have a space-complexity of `O(n*n!)`.

## Comments

* This is a very naive implementation. If a string of letters contains more than one instance of a letter, then there will be wasted time (roof has two combinations of length three that are "roo" and "roo"). A more intelligent permutation implementation would skip over these, whereas I simply check to make sure I haven't seen the word before.
* Another idea I had was instead of going through permutations of the query, filter out the dictionary instead -- depending on the length of the query and dictionary, this could be more efficient as `n!` increases. A pseudoalgorithm for this would go:
```
  1. Find all the letters that are not in the queried letters
  2. Iterate over the dictionary and:
    2a. Take out words that have any of the non-query-letters
    2b. If the word has more than one instance of a letter, check if there are enough letters in the query
  3. Return the list of valid words
```

## Acknowledgements
 
Thanks to the Built Robotics team for giving me this opportunity! I enjoyed my conversation with Kelly on Friday and hope to continue the conversation. I recognize that this is a very simple solution, but I love thinking about and talking about problems like this; I would be more than excited to discuss why this is a *terrible* idea and work through a better one.
