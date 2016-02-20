import sys
import csv
from random import randint


def main(argv):
    script, filename = argv

    print("Working on: " + filename)
    # txt = open(filename, 'r')
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        lines = list(reader)

    # convert all to float
    for line in lines:
        for index in range(len(line)):
            line[index] = float(line[index])

    new_lines = []
    # reduce dataset
    index = 0
    print len(lines)
    while index < len(lines):
        val = randint(0, 9)
        if val+index in range(len(lines)):
            new_lines.append(lines[index+val])
        index += 9

    print len(new_lines)
    with open('reduced', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(new_lines)

if __name__ == "__main__":
    main(sys.argv)
