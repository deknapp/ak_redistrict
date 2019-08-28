import geopandas
import matplotlib.pyplot as plt
import pandas
import os

os.system('SHAPE_RESTORE_SHX=YES fio info shapefiles/2013_districts.shp')

#borough_file = 'shapefiles/boroughs.shp'
#precinct_file = 'shapefiles/2013_precincts.shp'
district_file = 'shapefiles/2013_districts.shp'
full_file = os.path.join(os.getcwd(), district_file)
df = geopandas.read_file(full_file) 
geometry = df['geometry']
plot = geometry.plot(color='white', edgecolor='black')

gdf = geopandas.GeoDataFrame(df, geometry=geometry) 

gdf.plot(ax=plot, color='white', edgecolor='black')

anchorage_min = 61.0
anchorage_max = 61.24
anchorage_min_long = -150.03
anchorage_max_long = -149.7
#plt.ylim(anchorage_min, anchorage_max)
#plt.xlim(anchorage_min_long, anchorage_max_long)
plt.show()

#borough_plot.get_figure().savefig('/Users/nknapp/Desktop/test.pdf')




