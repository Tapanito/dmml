import sys
import csv


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

    # normalise
    for i in range(56):
        # set min max to the first value of each column
        min_val = lines[0][i]
        max_val = lines[0][i]
        # find min max
        for line in lines:
            if line[i] > max_val:
                max_val = line[i]
            if line[i] < min_val:
                min_val = line[i]
        print "Before min max: " + str(i)
        print "Max: " + str(max_val)
        print "Min: " + str(min_val)
        # min max normalise
        for line in lines:
            line[i] = (line[i] - min_val) / (max_val - min_val)

    with open('min_maxed', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(lines)

if __name__ == "__main__":
    main(sys.argv)