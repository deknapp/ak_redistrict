import geopandas
import geoplot

boroughs = geopandas.read_file('borough/mv_borough_py.shp')
borough_geometry = boroughs['geometry']
print(borough_geometry)
print(boroughs)
borough_plot = boroughs.plot(color='white', edgecolor='black')
borough_plot.get_figure().savefig('/Users/nknapp/Desktop/test.pdf')

