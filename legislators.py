import geopandas
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas
import os

senate_dems = ['Kawasaki', 'Wielechowski', 'Gray-Jackson', 'Begich', 'Kiehl', 'Hoffman', 'Olson']
senate_gop = ['Coghill', 'Bishop', 'Wilson', 'Shower', 'Hughes', 'Reinbold', 'Costello', 'von-Imhof', 'Giessel', 'Micciche', 'Stevens', 'Stedman']
senate = senate_dems + senate_gop
 
house_ind = ['Ortiz', 'Edgmon']
house_gop_coalition = ['LeBon', 'Thompson', 'Kopp', 'Johnston', 'Knopp', 'Stutes'] 
house_dems = ['Hopkins', 'Wool', 'Spohnholz', 'Josephson', 'Drummond', 'Tarr', 'Fields', 'Claman', 'Hannan', 'Story', 'Kreiss-Tomkins', 'Zulkosky', 'Foster', 'Lincoln', 'Tuck']   
house_gop = ['Wilson', 'Talerico', 'Sullivan-Leonard', 'Neuman', 'Rauscher', 'Eastman', 'Johnson', 'Tilton', 'Jackson', 'Merrick', 'Ledoux', 'Revak', 'Shaw', 'Pruitt', 'Carpenter', 'Vance', 'Rasmussen'] 
house = house_ind + house_gop_coalition + house_dems + house_gop

def house_party_legend_anch():
  dem_patch = mpatches.Patch(color='b', label='Democrat')    
  republican_patch = mpatches.Patch(color='r', label='Republican')    
  coalition_patch = mpatches.Patch(color='g', label='Coalition Republican')    
  return [dem_patch, republican_patch, coalition_patch]    

def house_party_legend_anch_with_shade():
  dem_patch = mpatches.Patch(color='b', label='Democrat')    
  republican_patch = mpatches.Patch(color='r', label='Republican')    
  coalition_patch = mpatches.Patch(color='g', label='Coalition Republican')    
  low_patch = mpatches.Patch(color='m', label='Population Lower Than Ideal')  
  return [dem_patch, republican_patch, coalition_patch, low_patch]    

def sen_party_legend():
  dem_patch = mpatches.Patch(color='b', label='Democrat')    
  republican_patch = mpatches.Patch(color='r', label='Republican')    
  return [dem_patch, republican_patch]    

def get_senator_label_color(full_sen):
  sen = full_sen.split()[1] 
  if sen in senate_dems:
    return 'b'
  elif sen in senate_gop:
    return 'r'
  else:
    return 'k'   

def get_rep_label_color(full_rep):
  rep = full_rep.split()[1]
  if rep in house_dems:
    return 'b'
  elif rep in house_gop:
    return 'r'
  elif rep in house_ind:
    return 'k'
  elif rep in house_gop_coalition:
    return 'g' 
  else:
    return 'w'

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
  leg_gdf_plot = leg_gdf.plot(color='black')
  i = 0 
  for x, y, label in zip(leg_df.Longitude, leg_df.Latitude, leg_df.Legislator):
    print(label)
    if 'Fields' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x+0.003, y+0.005))
      text.set_fontsize(6)
      text.set_color(get_rep_label_color(label))
    elif 'Tarr' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x+0.003, y+0.005))
      text.set_fontsize(6)
      text.set_color(get_rep_label_color(label))
    elif 'Rasmussen' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x, y-0.007))
      text.set_fontsize(6)
      text.set_color(get_rep_label_color(label))
    elif 'Claman' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x-0.01, y-0.01))
      text.set_fontsize(6)
      text.set_color(get_rep_label_color(label))
    elif 'Shaw' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x-0.01, y+0.005))
      text.set_fontsize(6)
      text.set_color(get_rep_label_color(label))
    elif 'Spohnholz' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x, y+0.005))
      text.set_fontsize(6)
      text.set_color(get_rep_label_color(label))
    elif 'Ledoux' in label:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x-0.01, y+0.005))
      text.set_fontsize(6)
      text.set_color(get_rep_label_color(label))
    else:
      text = leg_gdf_plot.annotate(label, xy=(x,y), xytext=(x+0.003, y-0.006))
      text.set_fontsize(6) 
      if typ == 'rep':
        text.set_color(get_rep_label_color(label))
      else:
        text.set_color(get_senator_label_color(label))
  return leg_gdf_plot
 
