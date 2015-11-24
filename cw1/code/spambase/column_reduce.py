import sys
import csv
import nn

def main(argv):

    script, filename = argv
    field_0 = -1
    field_1 = -1
    result = 0
    res_sum = 0
    avg_val = 0
    with open(filename, 'rb') as f:
                reader = csv.reader(f)
                lines = list(reader)
    print("Working on: " + filename)

    column_list = range(len(lines[0]) - 1)
    for item in column_list:
        for second in column_list:
            if item == second:
                continue

            columns = [item, second, -1]
            # convert all to float
            for line in lines:
                for index in range(len(line)):
                    line[index] = float(line[index])

            new_lines = []
            # reduce dataset
            index = 0
            # print len(lines)
            for line in lines:
                new_lines.append([line[columns[0]], line[columns[1]], line[columns[2]]])

            # with open('col_reduced', 'w') as f:
            #     writer = csv.writer(f)
            #     writer.writerows(new_lines)

            tmp = nn.main(new_lines)
            res_sum += tmp
            avg_val += 1
            print "Accuracy of nearest neigbour is: {0}%. Field {1} Field {2}".format(str(round(tmp, 2)), str(item), str(second))
            if tmp > result:
                field_0 = item
                field_1 = second
                result = tmp

    print "Highest accuracy is: {0}% for Field {1} and Field {2}".format(str(round(result, 2)), str(field_0), str(field_1))
    print "Average accuracy is: {0}%".format(str(round((res_sum/avg_val), 2)))

if __name__ == "__main__":
    main(sys.argv)
