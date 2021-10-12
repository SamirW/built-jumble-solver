#!/usr/bin/env python3
"""Jumble solver for Built Robotics Coding Challenge.

The solver checks all permutations of anagrams and sub-anagrams of a queried
set of letters against a provided word list. Simple implentation via CLI.

    Typical usage example (from command line):

    python3 jumbly.py hiresamir
"""

import argparse
from itertools import permutations


def open_dictionary(filename: str) -> set:
    """Creates hashmap from provided word list file.

    Args:
        filename: Path of word list to be used.

    Returns:
        A set with all words in provided word list.
    """
    dictionary = set()

    with open(filename, 'r', encoding='UTF-8') as file:
        for word in file:
            dictionary.add(word.strip())

    return dictionary


def solve_jumble(letters: str, dictionary: set) -> list:
    """Finds all possible words able to be constructed from queried letters.

    Checks all permutations of letters length 2 and up in queried string of
    letters against a hashmap of possible words. Prints words in descending
    length, ascending alphabetical order for CLI usage.

    Args:
        letters: String of letters from which to construct words.
        dictionary: The dictionary against which to check for valid words.

    Returns:
        A list of valid words, each elementing representing one word.
    """
    if len(letters) < 2: # Assuming min word length is 2
        print("No words found")
        return []

    answers = set()

    for i in range(2, len(letters)+1):
        for permutation in permutations(letters, i):
            potential_word = ''.join(permutation)
            if potential_word not in answers:
                if potential_word in dictionary:
                    answers.add(potential_word)

    sorted_answers = list(answers)
    sorted_answers.sort()
    sorted_answers.sort(key=len, reverse=True)

    if sorted_answers:
        for word in sorted_answers:
            print(word)
    else:
        print("No words found")

    return sorted_answers


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Jumble Solver"
    )

    parser.add_argument(
        'letters',
        help='Letters to be unjumbled',
        type=str,
        default='')
    parser.add_argument(
        '-d', '--dict',
        help='Filename of dictionary to use',
        type=str,
        default='corncob_lowercase.txt')
    args = parser.parse_args()

    word_dict = open_dictionary(args.dict)
    query_letters = ''.join(x for x in args.letters if x.isalpha())
    solve_jumble(query_letters, word_dict)
