import ppc
import sys
import numpy as np

def column(matrix, i):
    return [row[i] for row in matrix]

def print_opt(data):
    with open(filename, options) as f:
            for s in data:
                for i in range(len(s)):
                    print str(i) + " "


def main(args):
    filename = "../opt{0}.txt"
    script, size = args
    tmp = []
    result = []
    for i in range(1):
        tmp.append(ppc.main(filename.format(str(i))))
        lines = ppc.open_csv(filename.format(str(0)))
        lines = ppc.to_int(lines)
        del lines[10:]
        # i file first column key
        for j in range(int(size)):
            qq = column(lines, tmp[i][j][0])
            if len(result) == 0:
                for i in qq:
                    result.append([i])
            else:
                for i in range(len(result)):
                    result[i].append(qq[i])

    print result

if __name__ == "__main__":
    main(sys.argv) 
