import geopandas
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
handle = open('leg_coord_dict.csv', 'r'   

leg_coord_dict = {}
lines = handle.readlines()


# get coordinates for addresses
geolocator = Nominatim(user_agent='ak_redistrict')
for leg in leg_dict:
  if leg not in leg_coord_dict:
    leg_address = leg_dict[leg][0] + ' ' + leg_dict[leg][1]
    try:
      leg_location = geolocator.geocode(leg_address)
    except:
      continue
  if leg_location is not None:
    print(leg_location)
    leg_coord_dict[leg] = [leg_location.latitude, leg_location.longitude]
 
print(leg_coord_dict)
 
