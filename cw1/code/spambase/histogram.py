import sys
import csv


def convert_to_float(lines):
    # convert str to float in the csv
    for line in lines:
        for index in range(len(line)):
            line[index] = float(line[index])
    return lines


def main(argv):
    # my code here
    script, filename = argv

    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        lines = list(reader)

    f = open('histogram_data', 'w')
    writer = csv.writer(f)

    lines = convert_to_float(lines)

    for i in range(1, 5):
        bins = [0.2] * 5
        bin_count_0 = [0.0] * 5
        bin_count_1 = [0.0] * 5

        max_val = 0
        # find min max
        for line in lines:
            if line[i] >= max_val:
                max_val = line[i]
        # return
        val = round((max_val / 5.0), 2)
        for j in range(len(bins)):
            bins[j] = val
            val += round((max_val / 5.0), 2)

        # print bins
        for line in lines:
            for j in range(len(bins)):
                if line[i] <= bins[j]:
                    if line[-1] == 0.0:
                        bin_count_0[j] += 1
                    else:
                        bin_count_1[j] += 1
                    break
                # sanity check if line[i] is greater than upper bound increment last bin
                if j + 1 >= len(bins):
                    if line[-1] == 0.0:
                        bin_count_0[j] += 1
                    else:
                        bin_count_1[j] += 1
        # calc distribution %
        print bin_count_0
        val = 0
        for j in range(len(bin_count_0)):
            bin_count_0[j] = round((bin_count_0[j] / len(lines)) * 100, 2)
            bin_count_1[j] = round((bin_count_1[j] / len(lines)) * 100, 2)
        tmp = ["", "{0} - {1}".format(0, bins[0]), "{0} - {1}".format(bins[0], bins[1]), "{0} - {1}".format(bins[1], bins[2]), "{0} - {1}".format(bins[2], bins[3]) ,"{0} - {1}".format(bins[3], bins[4])]
        writer.writerow(tmp)
        writer.writerow(["Class: " + str(0)] + bin_count_0)
        writer.writerow(["Class: " + str(1)] + bin_count_1)

        print bin_count_0

if __name__ == "__main__":
    main(sys.argv)
