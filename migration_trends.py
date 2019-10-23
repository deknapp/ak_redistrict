import migration 
import names
import matplotlib.pyplot as plt
import os
import networkx as nx
import statistics

def get_net_migration_list(first_year, last_year, dest, source):
  lst = []
  for i in range(first_year, last_year):
    dct = migration.migration_dict(i, i+1)
    to_val = 0
    try:
      to_val = dct[source][dest] 
    except:
      pass
    from_val = 0
    try: 
      from_val = dct[dest][source] 
    except:
      pass
    net_val = to_val - from_val
    lst.append(net_val)
  return lst

def compare_migration(start_year, end_year, from_list, to):
  plt.clf()
  plt.title('Rural migration to ' + to + ' since '+ str(start_year))
  plt.ylabel('Net population flow')
  plt.xlabel('Year')
  x_vals = range(start_year, end_year+1)
  for frm in from_list:
    lst = get_net_migration_list(start_year, end_year, frm, to)
    y_vals = [0]
    for val in lst:
      y_vals.append(y_vals[-1] + val)
    plt.plot(x_vals, y_vals, label=frm)
  plt.legend(loc='upper left')
  try:
    os.mkdir('/Users/nknapp/Desktop/akpirg/migration_compare_plots/')
  except:
    pass
  plt.savefig('/Users/nknapp/Desktop/akpirg/migration_compare_plots/migration_to_' + to + '_' + str(start_year) + '_' + str(end_year) + '.png') 

# NTK TODO:
def compare_sums_of_migration(start_year, end_year, from_list, to):
  plt.clf()
  plt.title('Rural migration to ' + to + ' since '+ str(start_year))
  plt.ylabel('Net population flow')
  plt.xlabel('Year')
  x_vals = range(start_year, end_year+1)
  for frm in from_list:
    lst = get_net_migration_list(start_year, end_year, frm, to)
    y_vals = [0]
    for val in lst:
      y_vals.append(y_vals[-1] + val)
    plt.plot(x_vals, y_vals, label=frm)
  plt.legend(loc='upper left')
  try:
    os.mkdir('/Users/nknapp/Desktop/akpirg/migration_compare_plots/')
  except:
    pass
  plt.savefig('/Users/nknapp/Desktop/akpirg/migration_compare_plots/migration_to_' + to + '_' + str(start_year) + '_' + str(end_year) + '.png') 

def plot_migration(frm, to, start_year, end_year):
  lst = get_net_migration_list(start_year, end_year, to, frm)
  x_vals = range(start_year, end_year+1)
  y_vals = [0]
  for val in lst:
    y_vals.append(y_vals[-1] + val)
  plt.clf()
  plt.rcParams["font.size"] = 8
  plt.title('Migration from ' + frm + ' to ' + to + ' since '+ str(start_year))
  plt.ylabel('Net population flow')
  plt.xlabel('Year')
  plt.plot(x_vals, y_vals)
  try:
    os.mkdir('/Users/nknapp/Desktop/akpirg/migration_plots/migration_to_' + to + '/')
  except:
    pass
  plt.show()
  plt.savefig('/Users/nknapp/Desktop/akpirg/migration_plots/migration_to_' + to + '/migration_from_' + frm + '_to_' + to + '_' + str(start_year) + '_' + str(end_year) + '.png') 

def plot_all_migration(start_year, end_year):
  for frm in names.PLACE_LIST:
    for to in names.PLACE_LIST:
      if frm != to:
        plot_migration(frm, to, start_year, end_year)

#compare_migration(2010, 2016, from_list_matsu, names.MATSU)

#from_list_anchorage = [names.MATSU, names.FAIRBANKS, names.JUNEAU, names.OUT_OF_STATE]
#compare_migration(2010, 2016, from_list_anchorage, names.ANCHORAGE)

#from_list_fairbanks = [names.MATSU, names.ANCHORAGE, names.JUNEAU, names.OUT_OF_STATE]
#compare_migration(2010, 2016, from_list_fairbanks, names.FAIRBANKS)

#from_list_juneau = [names.MATSU, names.ANCHORAGE, names.JUNEAU, names.OUT_OF_STATE]
#compare_migration(2010, 2016, from_list_juneau, names.JUNEAU)

#from_list_rural = [names.YUKON, names.NW_ARCTIC, names.NORTH_SLOPE, names.NOME, names.DENALI] #, names.ALEUTIANS_EAST, names.ALEUTIANS_WEST]
#compare_migration(2010, 2016, from_list_rural, names.ANCHORAGE)
#compare_migration(2010, 2016, from_list_rural, names.FAIRBANKS) 
