import legislators
from geopy.distance import geodesic

def calculate_distance(coordA, coordB):
  return geodesic(origin, dist).meters


# finds the senators and reps that live closest to each other

sen_coord_dict = legislators.get_leg_coord_dict('sen')
rep_coord_dict = legislators.get_leg_coord_dict('rep')


overall_dict = dict()

for i in range(len(sen_coord_dict['Legislator')))
  leg = sen_coord_dict['Legislator'][i]
  lat = sen_coord_dict['Latitude'][i]
  lng = sen_coord_dict['Longitude'][i]
  overall_dict[leg] = [lat, lng] 

for i in range(len(rep_coord_dict['Legislator')))
  leg = rep_coord_dict['Legislator'][i]
  lat = rep_coord_dict['Latitude'][i]
  lng = rep_coord_dict['Longitude'][i]
  overall_dict[leg] = [lat, lng] 

distance_list = []

for legA in overall_dict.keys():
  for legB in overall_dict.keys():
    if legA == legB:
      continue
    else:
      coordA = (overall_dict[legA][0], overll_dict[legA][1])
      coordB = (overall_dict[legB][0], overll_dict[legB][1])
      distance = calculate_distance(coordA, coordB)
      distance_list.append([legA, legB, distance]) 






origin = (30.172705, 31.526725)  # (latitude, longitude) don't confuse
dist = (30.288281, 31.732326)
print(geodesic(origin, dist).meters)  # 23576.805481751613


