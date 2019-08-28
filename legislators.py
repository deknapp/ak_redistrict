import geopandas
import matplotlib.pyplot as plt
import pandas
import os

def get_leg_df():
	coord_file = os.path.join(os.getcwd(), 'csv_files/leg_coord_dict.csv')
	handle = open(coord_file, 'r')
	legs = []
	lats = []
	longs = []
	for line in handle.readlines():
	  split_line = line.split(',')
	  legs.append(split_line[0])
	  lats.append(float(split_line[1]))
	  longs.append(float(split_line[2]))
	leg_coord_dict = {'Legislator':legs, 'Longitude':longs, 'Latitude':lats}
	return pandas.DataFrame(leg_coord_dict)

def get_leg_gdf():
  df = get_leg_df()
  gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
  return gdf

def get_leg_points():
  df = get_leg_df()
  return geopandas.points_from_xy(df.Longitude, df.Latitude)
  
