"""Computation of weighted average of squares."""

import argparse  # 新增：导入 argparse


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]


if __name__ == "__main__":
    import argparse

    # 创建命令行解析器
    parser = argparse.ArgumentParser(
        description="Compute the weighted average of squares."
    )

    # 位置参数：numbers，可以有一个或多个
    parser.add_argument(
        "numbers",
        nargs="+",
        help="Numbers to be squared and averaged"
    )

    # ⭐ 添加可选参数 weights
    parser.add_argument(
        "--weights",
        nargs="+",              # 接受多个参数
        help="Optional weights for each number"
    )

    # 解析命令行参数
    args = parser.parse_args()

    # 将 numbers 转成 float 列表
    numbers = convert_numbers(args.numbers)

    # 将 weights 转成 float 列表（如果用户有输入）
    if args.weights is not None:
        weights = convert_numbers(args.weights)
    else:
        weights = None    # 默认情况（使用 equal weights）

    # 调用函数（会自动处理 None = 全部权重为 1）
    result = average_of_squares(numbers, weights)

    print(result)

