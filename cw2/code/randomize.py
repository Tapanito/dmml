import sys
import csv
import random


def open_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        return list(reader)


def write_csv(filename, data, options='w'):
    with open(filename, options) as f:
        for s in data:
            for i in s:
                f.write(str(i) + ' ')
            f.write('\n')


def randomize(data):
    res = []
    for item in range(len(data)):
        i = random.choice(data)
        data.remove(i)
        res.append(i)
    return res


def main(argv):
    script, filename = argv
    lines = open_csv(filename)
    lines = randomize(lines)
    # print lines
    write_csv('randomized', lines)


if __name__ == "__main__":
    main(sys.argv)
