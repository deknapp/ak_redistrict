import legislators
from geopy.distance import geodesic
from functools import cmp_to_key
import itertools

def calculate_distance(coordA, coordB):
  return geodesic(coordA, coordB).meters

def compare_distance(item1, item2):
  return item1[4] - item2[4]

# finds the senators and reps that live closest to each other

sen_coord_dict = legislators.get_leg_coord_dict('sen')
rep_coord_dict = legislators.get_leg_coord_dict('rep')


overall_dict = dict()

for i in range(len(sen_coord_dict['Legislator'])):
  leg = sen_coord_dict['Legislator'][i]
  lat = sen_coord_dict['Latitude'][i]
  lng = sen_coord_dict['Longitude'][i]
  overall_dict[leg] = [lat, lng, 'Senator'] 

for i in range(len(rep_coord_dict['Legislator'])):
  leg = rep_coord_dict['Legislator'][i]
  lat = rep_coord_dict['Latitude'][i]
  lng = rep_coord_dict['Longitude'][i]
  overall_dict[leg] = [lat, lng, 'Rep'] 

distance_list = []
allLegPairs = []
num_legs = len(overall_dict.keys())
overall_dict_key_list = list(overall_dict.keys())
for i in range(num_legs):
  for j in range(i+1, num_legs):
    legA = overall_dict_key_list[i]
    legB = overall_dict_key_list[j]  
    allLegPairs.append([legA, legB])

for pair in allLegPairs:
  legA = pair[0]
  legB = pair[1]
  coordA = (overall_dict[legA][0], overall_dict[legA][1])
  coordB = (overall_dict[legB][0], overall_dict[legB][1])
  distance = calculate_distance(coordA, coordB)
  typA = overall_dict[legA][2]
  typB = overall_dict[legB][2]
  distance_list.append([legA, typA, legB, typB, distance]) 

sorted_distance_list = sorted(distance_list, key=cmp_to_key(compare_distance))

for element in sorted_distance_list[:20]:
  print(element)


