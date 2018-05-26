import pandas as pd


def read_corine():
    data = pd.read_csv('resources/Corine.txt', sep=" ", header=None)
    data = data.drop([0,1,3,5],1)
    data.columns = ['x','y','class']
    return data
