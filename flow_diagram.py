import names
import networkx as nx
import migration_trends
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.patches as mp
import statistics


MY_ARROWS = mp.ArrowStyle("Fancy", head_length=10, head_width=5, tail_width=.4)

def flow_dict(start_year, end_year):
  flw_dct = dict()
  for frm in names.PLACE_LIST:
    short_frm = frm.split()[0]
    flw_dct[short_frm] = dict()
    for to in names.PLACE_LIST:
      short_to = to.split()[0]
      if frm != to: 
        total = sum(migration_trends.get_net_migration_list(start_year, end_year, to, frm))
        flw_dct[short_frm][short_to] = total
  return flw_dct

def get_dict_scale(dct):
  vals = []
  for a in dct.keys():
    for b in dct[a].keys():
      if dct[a][b] != 0:
        vals.append(abs(dct[a][b]))
  mx = max(vals)
  mn = min(vals)
  return mx, mn   

def flow_graph(start_year, end_year, places):
  flw_dict = flow_dict(start_year, end_year)
  mx, mn = get_dict_scale(flw_dict)
  g = nx.DiGraph()
  edge_label_dict = {}
  for to in places:
    short_to = to.split()[0]
    for frm in places:
      short_frm = frm.split()[0]
      if to != frm:
        if short_to in flw_dict[short_frm].keys():
          if flw_dict[short_frm][short_to] != 0 and flw_dict[short_frm][short_to] > 0:
            number = flw_dict[short_frm][short_to]
            g.add_node(short_to, name=short_to)
            g.add_node(short_frm, name=short_frm)
            g.add_edge(short_to, short_frm, number=str(number))

  pos = nx.circular_layout(g)
  pos_attrs = {}
  for node, coords in pos.items():
    pos_attrs[node] = (coords[0], coords[1] + 0.08)

  node_attrs = nx.get_node_attributes(g, 'name')
  custom_node_attrs = {}
  for node, attr in node_attrs.items():
    custom_node_attrs[node] = attr

  edge_labels = nx.get_edge_attributes(g, 'number')
  colors = [int(x) for x in edge_labels.values()] 
  nx.draw(g, pos=pos, node_size=10, edge_color=colors, edge_cmap=cmx.Reds, width=2, arrowsize=1, arrowstyle=MY_ARROWS) 
  nx.draw_networkx_labels(g, pos_attrs, labels=custom_node_attrs)
  nx.draw_networkx_edge_labels(g, pos_attrs, edge_labels=edge_labels)

  #plt.axis('off')
  plt.tight_layout()
  plt.savefig('/Users/nknapp/Desktop/akpirg/sample_network_plot_big_places.png', pad_inches=0.2, dpi=600)

big_place_names = [names.ANCHORAGE, names.FAIRBANKS, names.JUNEAU, names.OUT_OF_STATE, names.MATSU] 
flow_graph(2010,2016, big_place_names)
print(mpl.get_backend())



