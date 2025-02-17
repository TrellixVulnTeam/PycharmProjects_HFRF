from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

my_map = Basemap(projection='ortho', lat_0=50, lon_0=-100, resolution='l', area_thresh=1000.0)
my_map.drawcoastlines()
plt.show()
