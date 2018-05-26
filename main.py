import pandas
from read_files import *
from dataPreprocessing import *


def main():
    # Data Reading
    df = read_aspect1()
    df_pruned = pruning(df)
    print(df_pruned.head())


if __name__ == "__main__":
    main()