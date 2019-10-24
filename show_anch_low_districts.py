import geopandas
import matplotlib.pyplot as plt
import pandas
import os
import osr
import legislators
import districts
import names

leg_gdf_plot = legislators.get_leg_plot('rep')

district_gdf = districts.get_district_gdf(districts.HOUSE_PRJ, districts.HOUSE_SHAPE)
final = district_gdf.plot(ax=leg_gdf_plot, color="none", edgecolor='black', facecolor="none")
final = districts.label_anch_rep_districts(final, shade=True)

anchorage_max_long = -149.68
anchorage_min_long = -150.01
anchorage_min = 61.08
anchorage_max = 61.25

plt.ylim(anchorage_min, anchorage_max)
plt.xlim(anchorage_min_long, anchorage_max_long)
plt.legend(handles=legislators.house_party_legend_anch(), loc='upper left', fontsize='xx-small')
title = "Anchorage Districts With Population Lower Than Ideal"
plt.title(title)
final.get_figure().savefig('/Users/nknapp/Desktop/akpirg/' + title)
