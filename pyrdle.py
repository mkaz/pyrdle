#!/usr/bin/env python3
"""
Wordle Solver

A program that helps you solve wordle puzzles.
It solves by using your guess and result to filter the list
or words using a sieve to eliminate invalid words and then
present a set of word to pick from.
"""

from typing import List, Set


def main():
    print("Wordle Solver")
    print("Key: a for yellow, A for locked, . for any)")
    print("")

    with open("words.txt") as f:
        words = [x.strip() for x in f]

    print(f"Words: {len(words)}")
    for _ in range(6):
        # gather guess
        guess = input("Your guess? ")

        # gather result
        #    .  - letter not in word
        #    a  - lowercase letter in word wrong pos
        #    A  - uppercase letter in word right pos
        result = input("Result : ")
        print("")

        result = result.strip()
        empty = result.replace(".", "")

        # 1. What letters are invalid
        #    Using Python sets get the difference between guess/result
        #    This returns all letters in guess not in result
        invalid = set(guess).difference(result.lower())

        # Remove all words that have invalid letters
        words = remove_invalid(invalid, words)

        if empty != "":
            # Remove words without required characters
            words = only_required(result, words)

            # Remove words with correct letter but wrong position
            words = wrong_position(result, words)

            # Remove words with correct letter and right position
            words = right_position(result, words)

        # Suggest 10 Words
        print(f"Words remaining {len(words)}")
        for i, word in enumerate(words):
            print(f"    {word}")
            if i > 4:
                break

        print("")


# Remove invalid words from list.
#   - Loop through list of words
#   - Check if word contains any letters in invalid string
#   - If the word does not it is good append to valid list
def remove_invalid(invalid: Set, words: List) -> List:
    valid = []

    # loop through list words
    for word in words:
        # is intersection empty set
        if set(word).intersection(invalid) == set():
            valid.append(word)

    return valid


# Remove words that do not contain required characters
#   - Convert guess to just chars, order doesn't matter
#   - Use set difference
def only_required(required: str, words: List) -> List:
    valid = []

    # remove . and lower
    required = required.replace(".", "").lower()

    # loop through words
    for word in words:
        # intersection is not empty means that the word
        # does contain a letter from required
        # so need to loop both since all letters are required
        # break if one character is produces empty
        k = True
        for ch in required:
            if set(word).intersection(ch) == set():
                k = False
        if k:
            valid.append(word)

    return valid


# Remove words that do have the letter in the wrong pos.
# Right letter, wrong position
#   - iterate over result
#   - if character is lowercase (right word, wrong pos)
#   - then loop over words add words that don't have
def wrong_position(result: str, words: List) -> List:
    valid = []
    for i, ch in enumerate(result):
        if ch.islower():
            for word in words:
                if word[i] != ch:
                    valid.append(word)

    return set(valid)  # makes unique


# Remove words that do not have letter in the right pos.
# Right letter, right position
#   - iterate over result
#   - if character is uppercase (right word, right pos)
#   - then loop over words add words that have same
def right_position(result: str, words: List) -> List:
    valid = []
    for i, ch in enumerate(result):
        if ch.isupper():
            for word in words:
                if word[i] == ch.lower():
                    valid.append(word)

    return set(valid)  # makes unique


if __name__ == "__main__":
    main()
