from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

m = Basemap(projection='mill',
            llcrnrlat=-90,
            llcrnrlon=-180,
            urcrnrlat=90,
            urcrnrlon=180,
            resolution='c')

m.drawcoastlines()
m.drawcountries(linewidth=2)
##m.drawstates(color='b')
##m.drawcounties(color='darkred')
# m.fillcontinents()
# m.etopo()
# m.bluemarble()

xs = []
ys = []

NYClat, NYClon = 40.7127, -74.0059
xpt, ypt = m(NYClon, NYClat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'c*', markersize=15)

LAlat, LAlon = 34.05, -118.25
xpt, ypt = m(LAlon, LAlat)
xs.append(xpt)
ys.append(ypt)
m.plot(xpt, ypt, 'g^', markersize=15)
m.plot(xs, ys, color='r', linewidth=3, label='Flight 98')
m.drawgreatcircle(NYClon, NYClat, LAlon, LAlat, color='c', linewidth=3, label='ARC')
plt.legend(loc=4)
plt.title('Basemap Tutorial')
plt.show()
