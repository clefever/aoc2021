import adventofcode


def part1(input):
    """
    >>> part1(['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010'])
    198
    """
    dict = {}
    length = len(input)
    lineLength = len(input[0])
    for line in input:
        for pos in range(len(line)):
            if pos in dict:
                dict[pos] += int(line[pos])
            else:
                dict[pos] = int(line[pos])
    gamma = 0
    epsilon = 0
    for i in range(lineLength):
        if dict[i] > (length / 2):
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
    oxygen = calc_oxygen(input, 0)
    co2 = calc_co2(input, 0)
    return int(oxygen[0], 2) * int(co2[0], 2)


def calc_oxygen(input, bit):
    dict = {}
    length = len(input)
    lineLength = len(input[0])
    for line in input:
        for pos in range(len(line)):
            if pos in dict:
                dict[pos] += int(line[pos])
            else:
                dict[pos] = int(line[pos])
    oxygen = input.copy()

    if bit >= lineLength:
        return oxygen

    if dict[bit] >= (length / 2):
        if len(oxygen) > 1:
            oxygen = [x for x in oxygen if x[bit] == '1']
            return calc_oxygen(oxygen, bit+1)
        else:
            return oxygen
    else:
        if len(oxygen) > 1:
            oxygen = [x for x in oxygen if x[bit] == '0']
            return calc_oxygen(oxygen, bit+1)
        else:
            return oxygen


def calc_co2(input, bit):
    dict = {}
    length = len(input)
    lineLength = len(input[0])
    for line in input:
        for pos in range(len(line)):
            if pos in dict:
                dict[pos] += int(line[pos])
            else:
                dict[pos] = int(line[pos])
    co2 = input.copy()

    if bit >= lineLength:
        return co2

    if dict[bit] >= (length / 2):
        if len(co2) > 1:
            co2 = [x for x in co2 if x[bit] == '0']
            return calc_co2(co2, bit+1)
        else:
            return co2
    else:
        if len(co2) > 1:
            co2 = [x for x in co2 if x[bit] == '1']
            return calc_co2(co2, bit+1)
        else:
            return co2


def main():
    puzzle_input = adventofcode.read_input(3)
    adventofcode.answer(1, 2595824, part1(puzzle_input))
    adventofcode.answer(2, 2135254, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
