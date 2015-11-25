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
    for i in range(1):
        tmp.append(ppc.main(filename.format(str(i))))
    print tmp[0]    
    lines = ppc.open_csv(filename.format(str(0)))
    lines = ppc.to_int(lines)

    del lines[10:]
    # first file first column
    qq = column(lines, tmp[0][tmp[0].keys()[0]])
    for i in qq:
        tmp.append([i])


if __name__ == "__main__":
    main(sys.argv) 
