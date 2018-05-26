import pandas as pd
from read_files import *
from datafiles import *

def pruning():
    data = read_dem()
    df = removeCoordinates(data)

    print(df.median(axis=1))
