from dataPreprocessing import pruning;
from read_files import *;


#df_geo_cleaned = pruning(read_aspect1())
df_geo = read_aspect1()

import numpy as np
import matplotlib.pyplot as plt

INPUT = df_geo[['x', 'y', 'm1']].values()

# get ranges
xmin = INPUT[:,0].min()
xmax = INPUT[:,0].max()
ymin = INPUT[:,1].min()
ymax = INPUT[:,1].max()
zmin = INPUT[:,2].min()
zmax = INPUT[:,2].max()

# create array for image : zmax+1 is the default value
shape = (xmax-xmin+1,ymax-ymin+1)
img = np.ma.array(np.ones(shape)*(zmax+1))

for inp in INPUT:
    img[inp[0]-xmin,inp[1]-ymin]=inp[2]

# set mask on default value
img.mask = (img==zmax+1)

# set a gray background for test
img_bg_test =  np.zeros(shape)
cmap_bg_test = plt.get_cmap('gray')
plt.imshow(img_bg_test,cmap=cmap_bg_test,interpolation='none')

# plot
cmap = plt.get_cmap('jet')
plt.imshow(img,cmap=cmap,interpolation='none',vmin=zmin,vmax=zmax)
plt.colorbar()

plt.imsave("test.png",img)
plt.show()