# Jumble Solver Coding Challenge

Author: Samir Wadhwania  
Date: 12 Oct, 2021

## Intro

This is my implementation of a Jumble Solver for the Built Robotics Coding Challenge. Below, I'll outline the algorithm, assumptions, complexity analysis, and comments.

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

Two different methods are used depending on the length of the query. If the query is below the threshold (9 assuming the default word list), then a permutation method is used:

1. Create a dictionary hashmap with all words in a provided word list
2. Create all letter permutations of length 2 to n possible from provided letters 
3. Check permutations to see if they exist in dictionary
4. Return (print) valid words

If the query is too large, then the permutation method will take longer than an iteration method:

1. Iterate through the word list and hash all words based on the letters present
2. Iterate through created dictionary and find all cases where no extra letters are present
3. Iterate through each word and add only those that do not have more instances of each letter than the query

### Packages

I used *itertools.permutations* to iterate through permuations of letters of length 2 to n. This made the implementation quite straightforward with the function `itertools.permutations(letters, length)`.

### Complexity Analysis

#### Permutation method

There are two (three, optionally) driving factors for time-complexity of the algorithm. Firstly, we run `itertools.permutations` which finds the `n!` permutations of length `n`. Secondly, because we need to loop from length `2 to n`, we will be looking at a complexity of `n*n!`. Since we (optionally/unnecessarily) also sort our output answer list, we could also consider `.sort()` having a runtime of `nlogn` (but the `n` here is the length of the output list). Because this is so much lower than `n!`, we can ignore and leave the complexity at `O(n*n!)`.

Space-wise, we are using a generator to avoid storing all `n!` permutations even if they are not valid words. However, in a worst case where all permutations of a string of letters are valid (think a word list dictionary of all permutations), then we would also have a space-complexity of `O(n*n!)`.

#### Iteration method

This implementation takes about the same amount of time regardless of the length of the query. Because it requires going through the entire word list, it is only useful whent he query is sufficiently large.

Iterating through and hashing the word list is `O(m)` where `m` is the length of the word list. Iterating through once again to check each key is `O(m)`. Because we are using set operations to check for inclusion, all of the internal operations are `O(1)`. The exception is counting letters to account for cases where a letter is repeated in a word; this is a `O(l)` operation where `l` is the length of the word. Overall, I would consider this a time-complexity of `O(m)`.

## Comments

* This is a very naive implementation of permutation checking. If a string of letters contains more than one instance of a letter, then there will be wasted time (roof has two combinations of length three that are "roo" and "roo"). A more intelligent permutation implementation would skip over these, whereas I simply check to make sure I haven't seen the word before.
* I simply tested at which point the iteration method became faster than the permutation method (more accurately, at which point the permutation method blew up). For our default word list, it is when the query length is 9 or greater.

## Acknowledgements
 
Thanks to the Built Robotics team for giving me this opportunity! I enjoyed my conversation with Kelly on Friday and hope to continue the conversation. I recognize that this is a very simple solution, but I love thinking about and talking about problems like this; I would be more than excited to discuss why this is a *terrible* idea and work through a better one.
