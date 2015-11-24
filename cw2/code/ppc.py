import sys
import csv
import math


def open_csv(filename):
    with open(filename, 'r') as f:
        res = []
        for line in f:
            num_string = line.split()
            numbers = [int(n) for n in num_string]
            res.append(numbers)
        return res


def write_csv(filename, data, options='w'):
    with open(filename, options) as f:
        for s in data:
            for i in s:
                f.write(str(i) + ' ')
            f.write('\n')


# calculate mean
def calc_mean(data, index):
    total = 0
    for i in data:
        total += i[index]
    mean = float(total)/float(len(data))

    return mean


# calculate standard deviation
def std(data, index, mean):
    total = 0
    for item in data:
        total += math.pow((int(item[index]) - mean), 2)

    std = float(total) / float(len(data))

    return std


def ppc(data, field_1, field_2):
    mean_1 = calc_mean(data, field_1)
    mean_2 = calc_mean(data, field_2)
    if mean_1 == 0 or mean_2 == 0:
        return 0
    std_1 = std(data, field_1, mean_1)
    std_2 = std(data, field_2, mean_2)
    total = 0
    for item in data:
        x = (int(item[field_1]) - mean_1) / std_1
        y = (int(item[field_2]) - mean_2) / std_2

        total += x*y

    ppc = total / len(data)

    return ppc


def to_int(lines):
    # convert str to float in the csv
    for line in lines:
        for index in range(len(line)):
            line[index] = int(line[index])
    return lines


def main(argv):
    script, filename = argv
    lines = open_csv(filename)
    lines = to_int(lines)

    # print lines
    for i in range(len(lines[0]) - 1):
       tmp = ppc(lines, i, len(lines[0]) - 1)
       print "Coleration betwwen {0} and {1} is: {2}".format(str(i+1), str(len(lines[0])), str(tmp))


if __name__ == "__main__":
    main(sys.argv)
