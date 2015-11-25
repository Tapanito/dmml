import ppc
import sys
import numpy as np

def column(matrix, i):
    return [row[i] for row in matrix]

def write_csv(filename, data, options='w'):
    with open(filename, options) as f:       
        for s in data:
            for i in range(len(s)):
                f.write(str(s[i]) + ' ')

            f.write('\n')


def main(args):
    filename = "../opt{0}.txt"
    script, size = args
    tmp = []
    result = []
    for i in range(10):
        tmp.append(ppc.main(filename.format(str(i))))
        lines = ppc.open_csv(filename.format(str(i)))
        lines = ppc.to_int(lines)
        # i file first column key
        for j in range(int(size)):
            qq = column(lines, tmp[i][j][0])
            if len(result) == 0:
                for k in qq:
                    result.append([k])
            else:
                for m in range(len(result)):
                    result[m].append(qq[m])
 
    write_csv('newopt{0}.txt'.format(str(size)), result)
    

if __name__ == "__main__":
    main(sys.argv) 
