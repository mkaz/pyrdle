#!/usr/bin/env python3
"""
Wordle Solver

A program that helps you solve wordle puzzles.
It solves by using your guess and result to filter the list
or words using a sieve to eliminate invalid words and then
present a set of word to pick from.
"""

import argparse
from typing import List

# TODO: add args
#            --help
#            --info


def main():
    parser = argparse.ArgumentParser(
        prog="pyrdle",
        description="A Wordle Solver in Python",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""

EXAMPLE
---------------------------

Enter your guess first.

For result:
    use lowercase for yellow letters
    use uppercase for green letters
    use . for not found

Example: If the clue is "snake"

You guess: great
Enter result as: ..ea.

Next guess: place
Enter result as: ..A.E

Next guess: shake
Enter result as: S.AKE


ctrl-c to exit
""",
    )

    parser.add_argument("--info", action="store_true")
    args = parser.parse_args()

    print("---------------")
    print(" Wordle Solver")
    print("---------------")

    with open("words.txt") as f:
        words = [x.strip() for x in f]

    if args.info:
        print(f"Words: {len(words)}")
    print()

        # gather result
        #    .  - letter not in word
        #    a  - lowercase letter in word wrong pos
        #    A  - uppercase letter in word right pos
        result = input("Result : ")
        print("")

        # Remove all words that have invalid letters
        # 1. What letters are invalid
        #    Using Python sets get the difference between guess/result
        #    This returns all letters in guess not in result
        invalid = set(guess).difference(result.lower())
        words = remove_invalid(invalid, words)
        if args.info:
            print(f"Words after invalid: {len(words)}")

        # Remove words without required characters
        required = result.replace(".", "").lower()
        words = only_required(required, words)
        if args.info:
            print(f"Words after required: {len(words)}")

        # Remove words with correct letter but wrong position
        words = wrong_position(result, words)
        if args.info:
            print(f"Words after wrong pos: {len(words)}")

        # Remove words with correct letter and right position
        words = right_position(result, words)
        if args.info:
            print(f"Words after right pos: {len(words)}")

        # Suggest 10 Words
        print("Suggestions...")
        for i, word in enumerate(words):
            print(f"    {word}")
            if i > 4:
                break

        print("")


# Remove invalid words from list.
#   - Loop through list of words
#   - Check if word contains any letters in invalid string
#   - If the word does not it is good append to valid list
def remove_invalid(invalid: str, words: List) -> List:
    valid = []

    # loop through list words
    for word in words:
        if has_valid_chars(word, invalid):
            valid.append(word)

    return valid


# Remove words that do not contain required characters
#   - Convert guess to just chars, order doesn't matter
#   - Use set difference
def only_required(required: str, words: List) -> List:
    valid = []

    # loop through words
    for word in words:
        if has_required(word, required):
            valid.append(word)

    return valid


# Remove words that do have the letter in the wrong pos.
# Right letter, wrong position
#   - iterate over result
#   - if character is lowercase (right word, wrong pos)
#   - then loop over words add words that don't have
def wrong_position(result: str, words: List) -> List:
    valid = []
    for word in words:
        if not is_wrong_position(result, word):
            valid.append(word)

    return valid


# Remove words that do not have letter in the right pos.
# Right letter, right position
#   - iterate over result
#   - if character is uppercase (right word, right pos)
#   - then loop over words add words that have same
def right_position(result: str, words: List) -> List:
    valid = []
    for word in words:
        if is_right_position(result, word):
            valid.append(word)

    return valid


# Checks if word contains only valid chars
# - chars passed in are invalid
def has_valid_chars(word: str, chars: str) -> bool:
    # if the intersection is empty then no invalid
    if set(word).intersection(chars) == set():
        return True

    # contains an invalid
    return False


# Checks if word contains all required chars
def has_required(word: str, chars: str) -> bool:
    # Nothing required
    if chars == "":
        return True

    # intersection is not empty means that the word does contain a letter from
    # required so need to loop both since all letters are required break if one
    # character is produces empty
    for ch in chars:
        if set(word).intersection(ch) == set():
            return False

    return True


# Checks word for characters in result are in the wrong position
# Right letter. Wrong position.
#   - iterate over result
#   - only check lowercase letters
#   - confirm word does not have letter there
def is_wrong_position(result: str, word: str) -> bool:
    for i, ch in enumerate(result):
        if ch.islower():
            if word[i] == ch:
                return True

    return False


# Checks word for characters in result are in the right position
# Right letter. Right position.
#   - iterate over result
#   - only check uppercase letters
#   - confirm word has letter there
#   - confirm all letters, not just first
def is_right_position(result: str, word: str) -> bool:
    k = True
    for i, ch in enumerate(result):
        if ch.isupper():
            if word[i] != ch.lower():
                k = False

    return k


if __name__ == "__main__":
    main()
