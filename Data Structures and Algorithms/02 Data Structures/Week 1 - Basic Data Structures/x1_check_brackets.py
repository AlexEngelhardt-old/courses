# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            # Process closing bracket
            if not opening_brackets_stack:  # then the closing bracket has no opening bracket before it
                return i+1
            partner = opening_brackets_stack.pop()
            if not are_matching(partner.char, next):
                return i+1  # solution requires 1-based index

    if opening_brackets_stack:  # if brackets is not empty
        unmatched_dude = opening_brackets_stack.pop()
        return unmatched_dude.position + 1

    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
