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

def flow_dict(start_year, end_year):
  flw_dct = dict()
  for frm in names.PLACE_LIST:
    flw_dct[frm] = dict()
    for to in names.PLACE_LIST:
      if frm != to:
        total = sum(get_net_migration_list(start_year, end_year, to, frm))
        flw_dct[frm][to] = total
  return flw_dct

def pie_chart_migration(to, start_year, end_year):
  inflow_dct = dict()
  outflow_dct = dict() 
  for frm in names.PLACE_LIST:
    if frm != to:
      total = sum(get_net_migration_list(start_year, end_year, to, frm))
      if total > 0:
        outflow_dct[frm] = total
      elif total < 0:
        inflow_dct[frm] = total
  print("INFLOW")
  print(inflow_dct)
  print("OUTFLOW")
  print(outflow_dct)    
  plt.clf()
  plt.rcParams["font.size"] = 8
  plt.title('Population inflow to ' + to + ' since '+ str(start_year))
  labels = inflow_dct.keys()
  values = inflow_dct.values()
  ten_percent_value = sum(values)/10.0
  end_labels = [label for label in labels if (inflow_dct[label] > ten_percent_value)]
  end_val = [val for val in values if val > ten_percent_value]
  fig1, ax1 = plt.subplots()
  ax1.pie(values, labels=labels)
  ax1.axis('equal')
  plt.savefig('/Users/nknapp/Desktop/akpirg/pie_charts/inflow_to_' + to + '.png')
  plt.clf()
  plt.rcParams["font.size"] = 8
  plt.title('Population outflow from ' + to + ' since '+ str(start_year))
  labels = outflow_dct.keys()
  values = outflow_dct.values()
  ten_percent_value = sum(values)/10.0
  end_labels = [label for label in labels if outflow_dct[label] > ten_percent_value]
  end_val = [val for val in values if val > ten_percent_value]
  fig1, ax1 = plt.subplots()
  ax1.pie(end_val, labels=end_labels)
  ax1.axis('equal')
  plt.savefig('/Users/nknapp/Desktop/akpirg/pie_charts/outflow_from_' + to + '.png')


def plot_all_pie_chart_migration(start_year, end_year):
  for to in names.PLACE_LIST:
    pie_chart_migration(to, start_year, end_year)

def get_dict_scale(dct):
  vals = []
  for a in dct.keys():
    for b in dct[a].keys():
       vals.append(dct[a][b])
  mean = statistics.mean(vals)
  if mean == 0:
    return 1
  return mean   

def flow_graph(start_year, end_year, places):
  flw_dict = flow_dict(start_year, end_year)
  scale = get_dict_scale(flw_dict)
  g = nx.DiGraph()
  edge_label_dict = {} 
  for to in places:
    for frm in places: 
      if to != frm:
        if to in flw_dict[frm].keys():
          if flw_dict[frm][to] != 0 and flw_dict[frm][to] > 0:  
            g.add_edge(to, frm, title=str(flw_dict[frm][to]))
  pos = nx.spring_layout(g, dim=2)
  labels = nx.get_edge_attributes(g, 'title')
  nx.draw(g, pos, with_labels=True)
  nx.draw_networkx_edge_labels(g, pos, edge_labels=labels) 
  plt.axis('off')
  plt.show()
  
big_place_names = [names.ANCHORAGE, names.FAIRBANKS, names.JUNEAU, names.OUT_OF_STATE, names.MATSU] 
flow_graph(2010,2016, big_place_names)


 
