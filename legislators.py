import geopandas
import matplotlib.pyplot as plt
import pandas
import os

senate_dems = ['Kawasaki', 'Wielechowski', 'Gray-Jackson', 'Begich', 'Kiehl', 'Hoffman', 'Olson']
senate_gop = ['Coghill', 'Bishop', 'Wilson', 'Shower', 'Hughes', 'Reinbold', 'Costello', 'Imhof', 'Giessel', 'Micciche', 'Stevens', 'Stedman']
senate = senate_dems + senate_gop
 
house_ind = ['Ortiz', 'Edgmon']
house_gop_coalition = ['LeBon', 'Thompson', 'Kopp', 'Johnston', 'Knopp', 'Stutes'] 
house_dems = ['Hopkins', 'Wool', 'Spohnholz', 'Josephson', 'Drummond', 'Tarr', 'Fields', 'Claman', 'Tuck', 'Hannan', 'Story', 'Kreiss-Tomkins', 'Zulkosky', 'Foster', 'Lincoln']   
house_gop = ['Wilson', 'Talerico', 'Sullivan-Leonard', 'Neuman', 'Rauscher', 'Eastman', 'Johnson', 'Tilton', 'Jackson', 'Merrick', 'LeDoux', 'Revak', 'Shaw', 'Pruitt', 'Carpenter', 'Vance'] 
house = house_ind + house_gop_coalition + house_dems + house_gop


def get_senator_label_color(sen):
  if sen in senate_dems:
    return 'b'
  elif sen in senate_gop:
    return 'r'
  else:
    return 'y'   

def get_rep_label_color(rep):
  if rep in house_dems:
    return 'b'
  elif rep in house_gop:
    return 'r'
  elif rep in house_ind:
    return 'b'
  elif rep in house_gop_coalition:
    return 'g' 
  else:
    return 'y'

def get_leg_df(typ):
  coord_file = os.path.join(os.getcwd(), 'csv_files/leg_coord_dict.csv')
  handle = open(coord_file, 'r')
  legs = []
  lats = []
  longs = []
  for line in handle.readlines():
    split_line = line.split(',')
    if typ == 'rep':
      if split_line[0].split()[1] in house: 
        legs.append(split_line[0])
        lats.append(float(split_line[1]))
        longs.append(float(split_line[2]))
    if typ == 'sen':
      if split_line[0].split()[1] in senate: 
        legs.append(split_line[0])
        lats.append(float(split_line[1]))
        longs.append(float(split_line[2]))
  leg_coord_dict = {'Legislator':legs, 'Longitude':longs, 'Latitude':lats}
  return pandas.DataFrame(leg_coord_dict)

def get_leg_gdf(typ):
  df = get_leg_df(typ)
  gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
  return gdf

def get_leg_points(typ):
  df = get_leg_df(typ)
  return geopandas.points_from_xy(df.Longitude, df.Latitude)

def get_leg_plot(typ):
  leg_df = get_leg_df(typ) 
  leg_gdf = get_leg_gdf(typ)
  leg_gdf_plot = leg_gdf.plot(color='red')
  i = 0 
  for x, y, label in zip(leg_df.Longitude, leg_df.Latitude, leg_df.Legislator):
    if 'Wielechowski' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x-0.01, y+0.005))
      text.set_fontsize(9)
    elif 'Fields' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x-0.01, y+0.005))
      text.set_fontsize(9)
    elif 'Rasmussen' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x+0.003, y+0.005))
      text.set_fontsize(9)
    else:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x+0.003, y-0.006))
      text.set_fontsize(9) 
  return leg_gdf_plot
 
