import geopandas

legislator_file = 'lgaddr_corrected.csv'
handle = open(legislator_file, 'r')
lines = handle.readlines()
leg_dict = {}

# read in addresses to dictionary
for line in lines:
  split_line = line.split(',')
  if len(split_line) == 3:
    leg_dict[split_line[0]] = [split_line[1], split_line[2][:-1]]

# get coordinates for addresses





# plot coordinates

 
