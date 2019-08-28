import geopandas
import matplotlib.pyplot as plt
import pandas
import os

os.system('SHAPE_RESTORE_SHX=YES fio info gz_2010_us_050_00_20m.shp')

borough_file = 'gz_2010_us_050_00_20m.shp'
full_file = os.path.join(os.getcwd(), borough_file)
boroughs = geopandas.read_file(full_file) 
borough_geometry = boroughs['geometry']

borough_plot = borough_geometry.plot(color='white', edgecolor='black')
gdf = geopandas.GeoDataFrame(boroughs, geometry=borough_geometry) 

gdf.plot(ax=borough_plot, color='white')

plt.ylim(58, 70)
plt.xlim(-160, -140)
plt.show()

#borough_plot.get_figure().savefig('/Users/nknapp/Desktop/test.pdf')




