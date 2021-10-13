#!/usr/bin/env python3
"""Jumble solver for Built Robotics Coding Challenge.

The solver checks all permutations of anagrams and sub-anagrams of a queried
set of letters against a provided word list. Simple implentation via CLI.

    Typical usage example (from command line):

    python3 jumble.py hiresamir
"""

import argparse
from itertools import permutations
from collections import defaultdict

ALPHABET = set('abcdefghijklmnopqrstuvwxyz')


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


def solve_jumble_permuation(letters: str, dictionary: set) -> list:
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
    if len(letters) < 2:  # Assuming min word length is 2
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
    return sorted_answers


def create_set_dictionary(filename: str) -> defaultdict:
    """Creates dictionary of words from provided word list file.

    Args:
        filename: Path of word list to be used.

    Returns:
        A dictionary where words containing the same letters are in a list stored
        under the same key.
    """
    dictionary = defaultdict(lambda: [])

    with open(filename, 'r', encoding='UTF-8') as file:
        for word in file:
            dictionary[frozenset(word.strip())].append(word.strip())

    return dictionary


def solve_jumble_iteration(query: str, dictionary: defaultdict) -> list:
    """Finds all possible words able to be constructed from queried letters.

    Checks to see which words in the dictionary do not contain any letters not
    present in the query. Proceeds to make sure no words has more instances of
    a letter than the query.

    Args:
        letters: String of letters from which to construct words.
        dictionary: The dictionary against which to check for valid words.

    Returns:
        A list of valid words, each elementing representing one word.
    """
    if len(query) < 2:  # Assuming min word length is 2
        return []

    non_query_set = ALPHABET-set(query)
    answers = []

    for letter_set, word_list in dictionary.items():
        if not non_query_set.intersection(letter_set):
            for word in word_list:
                valid_word = True
                for letter in letter_set:
                    if word.count(letter) > query.count(letter):
                        valid_word = False
                        break
                if valid_word:
                    answers.append(word)

    answers.sort()
    answers.sort(key=len, reverse=True)
    return answers


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

    query_letters = ''.join(x for x in args.letters if x.isalpha())

    if len(query_letters) < 9:  # Basic time testing shows 9 to be the inflection point
        answer = solve_jumble_permuation(query_letters, open_dictionary(args.dict))
    else:
        answer = solve_jumble_iteration(query_letters, create_set_dictionary(args.dict))

    if answer:
        for word in answer:
            print(word)
    else:
        print("No words found")
