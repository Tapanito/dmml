import ppc
import sys
import numpy as np

def column(matrix, i):
    return [row[i] for row in matrix]

def main(args):
    filename = "../opt{0}.txt"
    script, size = args
    tmp = []
    for i in range(10):
        tmp.append(ppc.main(filename.format(str(i))))
    
    lines = ppc.open_csv(filename.format(str(0)))
    lines = ppc.to_int(lines)
    qq = column(lines, tmp[0][tmp[0].keys()[0]])




if __name__ == "__main__":
    main(sys.argv) 
