import unittest


class day_3_tests(unittest.TestCase):
    def test_part_1(self):
        file_name = 'test.txt'
        self.assertEqual(part_1(file_name), (22, 9, 198))

    def test_part_2(self):
        file_name = 'test.txt'
        self.assertEqual(part_2(file_name), (23, 10, 230))


def file_read(file_name):
    with open(file_name) as f:
        data = [line.strip() for line in f]
    return data


def part_1(file_name):
    data = file_read(file_name)

    gamma = ''
    epsilon = ''

    ones = 0
    zeroes = 0

    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[j][i] == '1':
                ones += 1
            elif data[j][i] == '0':
                zeroes += 1

        if ones > zeroes:
            gamma += '1'
            epsilon += '0'
        elif zeroes > ones:
            gamma += '0'
            epsilon += '1'

        ones, zeroes = 0, 0

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    power_consumption = gamma * epsilon

    if not file_name.startswith('test'):
        print('Part 1', power_consumption)

    return (gamma, epsilon, power_consumption)


def criteria_filter(data, width, criterion):
    filtered_data = data
    for w in range(width - 1, -1, -1):
        mask = 1 << w
        bits = [0, 0]

        for d in filtered_data:
            bits[1 if (d & mask) > 0 else 0] += 1

        keep_bit = criterion(bits)

        filtered_data = [d for d in filtered_data
                         if keep_bit == (1 if (d & mask) > 0 else 0)]

        if len(filtered_data) == 1:
            return filtered_data[0]
    return 0


def part_2(file_name):
    data = file_read(file_name)

    width = len(data[0])

    nums = [int(line, 2) for line in data]

    oxygen_generator_rating = criteria_filter(
        nums, width, lambda x: 1 if x[1] >= x[0] else 0)

    CO2_scrubber_rating = criteria_filter(
        nums, width, lambda x: 0 if x[0] <= x[1] else 1)

    life_support_rating = oxygen_generator_rating * CO2_scrubber_rating

    if not file_name.startswith('test'):
        print('Part 2', life_support_rating)

    return (oxygen_generator_rating, CO2_scrubber_rating, life_support_rating)


def day_3(file_name):

    part_1(file_name)

    part_2(file_name)


if __name__ == "__main__":
    day_3('input.txt')
    unittest.main(exit=True)
