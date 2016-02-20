import ppc
import sys

def main():
    filename = "../opt{0}.txt"
    for i in range(10):
        ppc.main(filename.format(str(i)))

    

if __name__ == "__main__":
    main() 
