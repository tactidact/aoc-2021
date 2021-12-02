def file_read(file_name):
    with open(file_name) as f:
        data = f.readlines()
    return data


def splitter(data):
    split_data = []
    for item in data:
        split_data.append(item.split())
    return split_data


def part_1(data):
    split_data = splitter(data)

    horiz_pos = 0
    depth = 0

    for item in split_data:
        if item[0] == 'forward':
            horiz_pos += int(item[1])
        elif item[0] == 'down':
            depth += int(item[1])
        elif item[0] == 'up':
            depth -= int(item[1])

    # answer is 1868935
    print('Part 1', horiz_pos*depth)


def part_2(data):
    split_data = splitter(data)

    horiz_pos = 0
    depth = 0
    aim = 0

    for item in split_data:
        if item[0] == 'forward':
            horiz_pos += int(item[1])
            depth += aim * int(item[1])
        elif item[0] == 'down':
            aim += int(item[1])
        elif item[0] == 'up':
            aim -= int(item[1])

    # answer is 1965970888
    print('Part 2', horiz_pos*depth)


def day_2():
    data = file_read('input.txt')

    part_1(data)

    part_2(data)


if __name__ == "__main__":
    day_2()
