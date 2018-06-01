import pandas as pd

'''
Methods to conveniently read the data files. The hardcoded filepaths are relative to the execution root (usually the project root).

The data will be returned as Pandas Dataframe, with the coordinates as 'x' and 'y' and 
- a single class as 'class'
- multiple classes (representing images) as 'm1', 'm2', 'm3', ...
'''


def read_corine():
    data = pd.read_csv('resources/Corine.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'class']
    return data


def read_subjective1():
    data = pd.read_csv('resources/Subjective_1.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'class']
    return data


def read_subjective2():
    data = pd.read_csv('resources/Subjective_2.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'class']
    return data


def read_slope():
    data = pd.read_csv('resources/Slope.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14',
                    'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data


def read_aspect1():
    data = pd.read_csv('resources/Aspect_c1.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14',
                    'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data


def read_aspect2():
    data = pd.read_csv('resources/Aspect_c2.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14',
                    'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data


def read_aspect_degree():
    data = pd.read_csv('resources/Aspect_degrees.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14',
                    'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data


def read_dem():
    data = pd.read_csv('resources/DEM.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14',
                    'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data


def read_ndvi():
    data = pd.read_csv('resources/NDVI.txt', sep="  ", header=None)
    data.columns = ['x', 'y', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14',
                    'm15', 'm16', 'm17', 'm18', 'm19', 'm20']
    return data


'''
Specify the filename of a csv-file matching the structure from above (or a similar one), so it can be read and parsed in a similar way. 

Somehow it is a more generic method, which could also be used to read any of the files above (or in the resources directory).

The data will be returned as Pandas Dataframe, with the coordinates as 'x' and 'y' and 
- a single class as 'class'
- multiple classes (representing images) as 'm1', 'm2', 'm3', ...
'''


def read_generic(filename):
    data = pd.read_csv(filename, sep="  ", header=None)
    columnCount = len(data.columns)
    if columnCount == 3:
        columns = ['x', 'y', 'class']
    else:
        columns = ['x', 'y']
        for i in range(columnCount - 2):
            columns.append(''.join(['m' + str(i)]))
    data.columns = columns
    return data
