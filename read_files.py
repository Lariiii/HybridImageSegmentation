import pandas as pd


def read_corine():
    data = pd.read_csv('resources/Corine.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'class']
    return data

def read_subjective1():
    data = pd.read_csv('resources/Subjective1.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'class']
    return data

def read_subjective2():
    data = pd.read_csv('resources/Subjective2.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'class']
    return data

def read_slope():
    data = pd.read_csv('resources/Slope.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data

def read_aspect1():
    data = pd.read_csv('resources/Aspect_c1.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data

def read_aspect2():
    data = pd.read_csv('resources/Aspect_c2.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data

def read_aspect_degree():
    data = pd.read_csv('resources/Aspect_degree.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data

def read_dem():
    data = pd.read_csv('resources/DEM.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data

def read_ndvi():
    data = pd.read_csv('resources/NDVI.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data