import geopandas
import matplotlib.pyplot as plt
import pandas
import os
import osr

import legislators

os.system('SHAPE_RESTORE_SHX=YES fio info shapefiles/2013_districts.shp')

prj_name = 'shapefiles/2013_precincts_proj.prj'
full_name = os.path.join(os.getcwd(), prj_name)
prj = open(full_name)
proj4 = osr.SpatialReference(prj.read()).ExportToProj4()

district_file = 'shapefiles/2013_districts.shp'
full_file = os.path.join(os.getcwd(), district_file)
df = geopandas.read_file(full_file) 
leg_gdf = legislators.get_leg_gdf()
leg_gdf_plot = leg_gdf.plot(color='red')

geometry = df['geometry'].to_crs(proj4)
gdf = geopandas.GeoDataFrame(df, geometry=geometry, crs=proj4) 
gdf.plot(ax=leg_gdf_plot, color="none", edgecolor='black', facecolor="none")
anchorage_min_long = -149.7
anchorage_max_long = -150.1
anchorage_min = 61
anchorage_max = 61.25

plt.ylim(anchorage_min, anchorage_max)
plt.xlim(anchorage_min_long, anchorage_max_long)
plt.show()

#borough_plot.get_figure().savefig('/Users/nknapp/Desktop/test.pdf')




