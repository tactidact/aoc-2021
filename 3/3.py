import unittest


class myTests(unittest.TestCase):
    def test_part_1(self):
        file_name = 'test.txt'
        self.assertEqual(part_1(file_name), (22, 9, 198))


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
        print(power_consumption)

    return (gamma, epsilon, power_consumption)


def day_3(file_name):

    part_1(file_name)


if __name__ == "__main__":
    day_3('input.txt')
    unittest.main(exit=True)
