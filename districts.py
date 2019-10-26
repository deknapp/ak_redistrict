import geopandas
import matplotlib.pyplot as plt 
import pandas
import os
import osr
import string
import names
import descartes

HOUSE_SHAPE = 'shapefiles/2013_districts.shp'
HOUSE_PRJ = 'shapefiles/2013_precincts_proj.prj'

def get_district_df(shape_file):
  os.system('SHAPE_RESTORE_SHX=YES fio info ' + shape_file)
  full_file = os.path.join(os.getcwd(), shape_file)
  df = geopandas.read_file(full_file) 
  return df 

def get_district_gdf(prj_file, shape_file):
  os.system('SHAPE_RESTORE_SHX=YES fio info ' + shape_file)
  full_name = os.path.join(os.getcwd(), prj_file)
  prj = open(full_name)
  proj4 = osr.SpatialReference(prj.read()).ExportToProj4()
  district_file = 'shapefiles/2013_districts.shp'
  full_file = os.path.join(os.getcwd(), district_file)
  df = geopandas.read_file(full_file) 
  geometry = df['geometry'].to_crs(proj4)
  gdf = geopandas.GeoDataFrame(df, geometry=geometry, crs=proj4) 
  i = 1
  colors = []
  return gdf

def label_anch_rep_districts(plot, shade=None):
  df = get_district_df(HOUSE_SHAPE)
  i = 1
  prj_name = 'shapefiles/2013_precincts_proj.prj'
  full_name = os.path.join(os.getcwd(), prj_name)
  prj = open(full_name)
  proj4 = osr.SpatialReference(prj.read()).ExportToProj4()
  for geo in df.geometry.to_crs(proj4): 
    if shade is not None:
      if i in names.LOW_DISTRICTS_ANCH:
        plot.add_patch(descartes.PolygonPatch(geo, fc='m', alpha=0.3))
    if i == 22:
      text = plot.annotate(sen_label(i), xy=(geo.centroid.x - 0.015, geo.centroid.y))
      text.set_fontsize(9) 
    elif i == 21:
      text = plot.annotate(sen_label(i), xy=(-149.98, 61.18))
      text.set_fontsize(9) 
    elif i == 24:
      text = plot.annotate(sen_label(i), xy=(-149.95, 61.11))
      text.set_fontsize(9) 
    elif i == 27:
      text = plot.annotate(sen_label(i), xy=(-149.73, 61.165))
      text.set_fontsize(9) 
    elif i == 15:
      text = plot.annotate(sen_label(i), xy=(geo.centroid.x, geo.centroid.y - 0.03))
      text.set_fontsize(9) 
    elif i == 18:
      text = plot.annotate(sen_label(i), xy=(geo.centroid.x, 61.185))
      text.set_fontsize(9) 
    elif i == 28:
      text = plot.annotate(sen_label(i), xy=(-149.73, 61.09))
      text.set_fontsize(9) 
    elif i == 14:
      text = plot.annotate(sen_label(i), xy=(-149.7, 61.2))
      text.set_fontsize(9) 
    elif i == 13:
      text = plot.annotate(sen_label(i), xy=(-149.72, 61.24))
      text.set_fontsize(9) 
    else: 
      text = plot.annotate(sen_label(i), xy=(geo.centroid.x, geo.centroid.y))
      text.set_fontsize(9) 
    i = i + 1
  return plot 

def house_sen_dict():
  dct = dict()
  letters = list(string.ascii_uppercase)
  j = 0
  for i in range(1, 41):
    dct[i] = letters[j]     
    if i%2 == 0:
      j += 1
  return dct 

def sen_house_dict():
  dct = dict()
  letters = list(string.ascii_uppercase)
  j = 0
  for i in range(1, 41):
    if letters[j] in dct.keys(): 
      dct[letters[j]].append(i)
    else:
      dct[letters[j]] = [i]     
    if i%2 == 0:
      j += 1
  return dct 

HOUSE_LABEL_DICT = house_sen_dict()

def sen_label(i):
  return str(i) + ' - ' + HOUSE_LABEL_DICT[i]

def label_anch_sen_districts(plot, shade=False):
  df = get_district_df(HOUSE_SHAPE)
  i = 1
  prj_name = 'shapefiles/2013_precincts_proj.prj'
  full_name = os.path.join(os.getcwd(), prj_name)
  prj = open(full_name)
  proj4 = osr.SpatialReference(prj.read()).ExportToProj4()

  for geo in df.geometry.to_crs(proj4): 
    if i == 22:
      text = plot.annotate(sen_label(i), xy=(geo.centroid.x - 0.015, geo.centroid.y))
      text.set_fontsize(9) 
    elif i == 21:
      text = plot.annotate(sen_label(i), xy=(-149.98, 61.18))
      text.set_fontsize(9) 
    elif i == 24:
      text = plot.annotate(sen_label(i), xy=(-149.95, 61.11))
      text.set_fontsize(9) 
    elif i == 27:
      text = plot.annotate(sen_label(i), xy=(-149.73, 61.165))
      text.set_fontsize(9) 
    elif i == 15:
      text = plot.annotate(sen_label(i), xy=(geo.centroid.x, geo.centroid.y - 0.03))
      text.set_fontsize(9) 
    elif i == 18:
      text = plot.annotate(sen_label(i), xy=(geo.centroid.x, 61.185))
      text.set_fontsize(9) 
    elif i == 28:
      text = plot.annotate(sen_label(i), xy=(-149.73, 61.09))
      text.set_fontsize(9) 
    elif i == 14:
      text = plot.annotate(sen_label(i), xy=(-149.7, 61.2))
      text.set_fontsize(9) 
    elif i == 13:
      text = plot.annotate(sen_label(i), xy=(-149.72, 61.24))
      text.set_fontsize(9) 
    else: 
      text = plot.annotate(sen_label(i), xy=(geo.centroid.x, geo.centroid.y))
      text.set_fontsize(9) 
    i = i + 1
  return plot

sen_to_rep_dict = sen_house_dict()
print(sen_to_rep_dict['D'], sen_to_rep_dict['E'], sen_to_rep_dict['F'])
 
