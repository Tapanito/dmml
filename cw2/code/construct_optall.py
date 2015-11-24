import ppc
import sys

def main():
    filename = "../opt{0}.txt"
    tmp = []
    for i in range(10):
        tmp.append(ppc.main(filename.format(str(i))))

    

if __name__ == "__main__":
    main() 
