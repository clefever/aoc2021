import adventofcode


def part1(input):
    count = 0
    for i in range(len(input)-1):
        if int(input[i]) < int(input[i+1]):
            count += 1
    return count


def part2(input):
    count = 0
    for i in range(len(input)-3):
        a = int(input[i]) + int(input[i+1]) + int(input[i+2])
        b = int(input[i+1]) + int(input[i+2]) + int(input[i+3])
        if a < b:
            count += 1
    return count


def main():
    puzzle_input = adventofcode.read_input(1)
    adventofcode.answer(1, 1581, part1(puzzle_input))
    adventofcode.answer(2, 1618, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
