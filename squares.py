"""Computation of weighted average of squares."""

import argparse


def average_of_squares(list_of_numbers, list_of_weights=None):
    """Return the weighted average of a list of values.

    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)

    squares = [
        weight * number * number
        for number, weight in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace."""
    all_numbers = []
    for s in list_of_strings:
        all_numbers.extend([token.strip() for token in s.split()])
    return [float(number_string) for number_string in all_numbers]


def read_numbers_from_file(path):
    """Read numbers from a text file and return a list of floats."""
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return convert_numbers(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Compute the (weighted) average of squares from files."
    )

    # 必选：数字文件
    parser.add_argument(
        "numbers_file",
        help="Text file containing the numbers (one per line or separated by spaces)."
    )

    # 可选：权重文件
    parser.add_argument(
        "--weights",
        dest="weights_file",
        help="Optional text file containing the weights."
    )

    args = parser.parse_args()

    numbers = read_numbers_from_file(args.numbers_file)

    if args.weights_file is not None:
        weights = read_numbers_from_file(args.weights_file)
    else:
        weights = None

    result = average_of_squares(numbers, weights)
    print(result)


if __name__ == "__main__":
    main()
