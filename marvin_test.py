from dataPreprocessing import pruning
from read_files import *

#df_geo = pruning(read_subjective1())
df_geo = read_subjective1()

minValue_x = 4423900
minValue_y = 5746100

min_x = 100000000
max_x = 0

min_y = 100000000
max_y = 0


for i, row in df_geo.iterrows():
    df_geo.set_value(i, 'x', row['x']/100)
    df_geo.set_value(i, 'y', row['y']/100)
    if row['x'] < min_x:
        min_x = row['x']
    if row['x'] > max_x:
        max_x = row['x']

    if row['y'] < min_y:
        min_y = row['y']
    if row['y'] > max_y:
        max_y = row['y']

for i, row in df_geo.iterrows():
    df_geo.set_value(i,'x', row['x'] - min_x)
    df_geo.set_value(i, 'y', row['y'] - min_y)

min_x = 100000000
max_x = 0

min_y = 100000000
max_y = 0

for i, row in df_geo.iterrows():
    if row['x'] < min_x:
        min_x = row['x']
    if row['x'] > max_x:
        max_x = row['x']

    if row['y'] < min_y:
        min_y = row['y']
    if row['y'] > max_y:
        max_y = row['y']

print(max_x)
print(min_x)
print(max_y)
print(min_y)
#print(df_geo)

import numpy
from PIL import Image

data = numpy.zeros((431,337 , 3), dtype=numpy.uint8)

colors = [[255,255,255], [255,0,0], [0,255,0], [0,0,255], [255,255,0], [0,255,255], [255,0,255], [128,0,0], [0,128,0], [0,0,128], [128,128,0], [0,128,128] ]
colors = list(numpy.random.choice(range(256), size=20))

colors = []
for i in range(20):
    colors.append([numpy.random.randint(low=0, high=255), numpy.random.randint(low=0, high=255), numpy.random.randint(low=0, high=255)])

#data[512, 511] = [255, 0, 0]
for i, row in df_geo.iterrows():
    #print(""+str(row['x'])+" "+str(row['y']))
    data[int(row['x'])][int(row['y'])] = colors[int(row['class'])-1]


image = Image.fromarray(data)
image.save('test.png')