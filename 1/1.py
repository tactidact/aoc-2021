def day_1():
    with open('input.txt') as f:
        depth_list = f.readlines()

    depth_list = list(map(lambda s: s.strip(), depth_list))

    increased = 0
    decreased = 0

    for i in range(len(depth_list)-1):
        if int(depth_list[i]) < int(depth_list[i+1]):
            increased += 1
        elif int(depth_list[i]) > int(depth_list[i+1]):
            decreased += 1

    print('Part 1', increased, decreased)

    sums = []
    for i in range(len(depth_list)-1):
        if i < len(depth_list)-2:
            sums.append(int(depth_list[i]) + int(
                depth_list[i+1]) + int(depth_list[i+2]))

    increased = 0
    decreased = 0

    for i in range(len(sums)-1):
        if int(sums[i]) < int(sums[i+1]):
            increased += 1
        elif int(sums[i]) > int(sums[i+1]):
            decreased += 1

    print('Part 2', increased, decreased)


if __name__ == "__main__":
    day_1()
