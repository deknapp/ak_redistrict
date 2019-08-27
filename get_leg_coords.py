import geopandas
import os
from geopy.geocoders import Nominatim

legislator_file = 'lgaddr_corrected.csv'
handle = open(legislator_file, 'r')
lines = handle.readlines()
leg_dict = {}

# read in addresses to dictionary
for line in lines:
  split_line = line.split(',')
  if len(split_line) == 3:
    leg_dict[split_line[0]] = [split_line[1], split_line[2][:-1]]

# read existing coordinates from file
leg_coord_dict = {}
leg_coord_file_name = 'leg_coord_dict.csv'
full_name = os.path.join(os.getcwd(), leg_coord_file_name)
try:
  handle = open(full_name, 'r') 
  for line in handle.readlines():
    split_line = line.split(',')
    leg_coord_dict[split_line[0]] = [split_line[1], split_line[2]]
  handle.close()
except:
  pass

# get coordinates for addresses
geolocator = Nominatim(user_agent='ak_redistrict')
for leg in leg_dict:
  if leg not in leg_coord_dict:
    leg_address = leg_dict[leg][0] + ' ' + leg_dict[leg][1]
    try:
      leg_location = geolocator.geocode(leg_address)
      leg_coord_dict[leg] = [leg_location.latitude, leg_location.longitude]
      print(leg_coord_dict[leg])
    except:
      continue
 
os.system('rm ' + full_name)
handle = open(full_name, 'w') 
for leg in leg_coord_dict:
  handle.write(leg + ',' + str(leg_coord_dict[leg][0]) + ',' + str(leg_coord_dict[leg][1]) + '\n')
handle.close()  
