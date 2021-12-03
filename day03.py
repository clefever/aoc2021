import adventofcode


def part1(input):
    """
    >>> part1(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
    198
    """
    gamma = 0
    epsilon = 0
    dict = get_bit_counts(input)

    for i in range(len(input[0])):
        if dict[i] > (len(input) / 2):
            gamma = (gamma << 1) + 1
            epsilon = epsilon << 1
        else:
            gamma = gamma << 1
            epsilon = (epsilon << 1) + 1
    return gamma * epsilon


def part2(input):
    """
    >>> part2(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
    230
    """
    oxygen = calc_life_support(input, 0, False)
    co2 = calc_life_support(input, 0, True)
    return int(oxygen[0], 2) * int(co2[0], 2)


def get_bit_counts(list):
    dict = {}
    for line in list:
        for pos in range(len(line)):
            if pos in dict:
                dict[pos] += int(line[pos])
            else:
                dict[pos] = int(line[pos])
    return dict


def calc_life_support(input, bit, invert):
    lines = input.copy()
    dict = get_bit_counts(input)

    if bit >= len(input[0]) or len(lines) <= 1:
        return lines

    if (dict[bit] >= (len(input) / 2)) ^ invert:
        lines = [x for x in lines if x[bit] == '1']
        return calc_life_support(lines, bit+1, invert)
    else:
        lines = [x for x in lines if x[bit] == '0']
        return calc_life_support(lines, bit+1, invert)


def main():
    puzzle_input = adventofcode.read_input(3)
    adventofcode.answer(1, 2595824, part1(puzzle_input))
    adventofcode.answer(2, 2135254, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
