import geopandas
import matplotlib.pyplot as plt
import pandas
import os

coord_file = os.path.join(os.getcwd(), 'leg_coord_dict.csv')
handle = open(coord_file, 'r')
legs = []
lats = []
longs = []
for line in handle.readlines():
  split_line = line.split(',')
  legs.append(split_line[0])
  lats.append(float(split_line[1]))
  longs.append(float(split_line[2]))   

print(lats)

os.system('SHAPE_RESTORE_SHX=YES fio info gz_2010_us_050_00_20m.shp')

leg_coord_dict = {'Legislator':legs, 'Longitude':longs, 'Latitude':lats}
  
df = pandas.DataFrame(leg_coord_dict)
gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

borough_file = 'gz_2010_us_050_00_20m.shp'
full_file = os.path.join(os.getcwd(), borough_file)
boroughs = geopandas.read_file(full_file) 
borough_geometry = boroughs['geometry']

borough_plot = borough_geometry.plot(color='white', edgecolor='black')

# We can now plot our ``GeoDataFrame``.
gdf.plot(ax=borough_plot, color='red')

plt.ylim(58, 70)
plt.xlim(-160, -140)
plt.show()

#borough_plot.get_figure().savefig('/Users/nknapp/Desktop/test.pdf')




