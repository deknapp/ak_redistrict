import geopandas
import matplotlib.pyplot as plt
import pandas
import os
import osr
import legislators
import districts
import locations

def plot_legs(coords, title, typ, shade=False, custom_legend=None):
  leg_gdf_plot = legislators.get_leg_plot(typ)
  district_gdf = districts.get_district_gdf(districts.HOUSE_PRJ, districts.HOUSE_SHAPE)
  final = district_gdf.plot(ax=leg_gdf_plot, color="none", edgecolor='black', facecolor="none")
  final = districts.label_anch_rep_districts(final)
  plt.ylim(coords.min_lat, coords.max_lat)`
  plt.xlim(coords.max_long, coords.min_long)
  if custom_legend is not None:
    leg_handles = custom_legend
  if typ == 'rep':
    leg_handles = legislators.house_party_legend_anch()
  if typ == 'sen':
    leg_handles = legislators.sen_party_legend_anch()
  else:
    print("ERROR: incorrect tye of leg plot")
    exit() 
  plt.legend(handles=leg_handles, loc='upper left', fontsize='xx-small')
  plt.title(title)
  final.get_figure().savefig('/Users/nknapp/Desktop/akpirg/leg_plots/' + title + '.pdf') 

plot_legs(locations.MATSU, "Matsu Senators and 
