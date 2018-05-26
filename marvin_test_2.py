import matplotlib.pyplot as plt
from PIL import Image

from dataPreprocessing import pruning
from read_files import *

df_geo = read_corine()

#df_geo.plot.scatter(x='x', y='y', c='class',colormap='viridis')
#plt.savefig('test.png', dpi=1000)

import numpy

data = numpy.zeros((1024, 1024, 3), dtype=numpy.uint8)

data[512, 511] = [255, 0, 0]
data[512, 512] = [0, 255, 0]
data[512, 513] = [0, 0, 255]

image = Image.fromarray(data)
image.save('test.png')