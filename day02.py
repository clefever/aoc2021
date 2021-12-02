import adventofcode


def part1(input):
    """
    >>> part1(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])
    150
    """
    coords = [0, 0]
    for line in input:
        command = line.split(' ')
        if command[0] == "forward":
            coords[0] += int(command[1])
        if command[0] == "down":
            coords[1] += int(command[1])
        if command[0] == "up":
            coords[1] -= int(command[1])
    return coords[0] * coords[1]


def part2(input):
    """
    >>> part2(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2'])
    900
    """
    coords = [0, 0, 0]
    for line in input:
        command = line.split(' ')
        if command[0] == "forward":
            coords[0] += int(command[1])
            coords[1] += int(command[1]) * coords[2]
        if command[0] == "down":
            coords[2] += int(command[1])
        if command[0] == "up":
            coords[2] -= int(command[1])
    return coords[0] * coords[1]


def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 1660158, part1(puzzle_input))
    adventofcode.answer(2, 1604592846, part2(puzzle_input))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
