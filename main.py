import pandas
from read_files import *
from dataPreprocessing import *


def main():
    # Data Reading
    df = read_aspect1()
    pruning()


if __name__ == "__main__":
    main()