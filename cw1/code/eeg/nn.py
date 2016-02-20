
import sys
import csv
import math


def convert_to_float(lines):
    # convert str to float in the csv
    for line in lines:
        for index in range(len(line)):
            line[index] = float(line[index])
    return lines


def get_difference_squared(a, b):
    return math.pow((a-b), 2)


def find_distance(a, b):
    res = 0
    for x in range(len(a) - 1):
        res += get_difference_squared(a[x], b[x])
    return res


def main(argv):
    # my code here
    filename = argv

    # print("Working on: " + filename)
    # # txt = open(filename, 'r')
    # with open(filename, 'rb') as f:
    #     reader = csv.reader(f)
    #     lines = list(reader)
    # lines = convert_to_float(lines)

    lines = argv
    accuracy = 0

    for i in range(len(lines)):
        cur_small = None
        cur_small_dist = 99999
        for j in range(len(lines)):
            # skip if i == j
            if i == j:
                continue
            distance = find_distance(lines[i], lines[j])

            if cur_small_dist > distance:
                cur_small = lines[j]
                cur_small_dist = distance

        if cur_small is not None and cur_small[-1] == lines[i][-1]:
            accuracy += 1

    qq = float(100 * accuracy) / len(lines)
    # print "Accuracy of nearest neigbour is: {0}%".format(str(round(qq, 2)))
    return qq


if __name__ == "__main__":
    main(sys.argv)
