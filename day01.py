import adventofcode


def part1(input):
    """
    >>> part1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    7
    """
    return sum(1 if input[i] < input[i+1] else 0 for i in range(len(input)-1))


def part2(input):
    """
    >>> part2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263])
    5
    """
    window = lambda i, list : list[i] + list[i+1] + list[i+2]
    return sum(1 if window(i, input) < window(i+1, input) else 0 for i in range(len(input)-3))


def main():
    puzzle_input = adventofcode.read_input(1)
    input_nums = [int(num) for num in puzzle_input]
    adventofcode.answer(1, 1581, part1(input_nums))
    adventofcode.answer(2, 1618, part2(input_nums))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
