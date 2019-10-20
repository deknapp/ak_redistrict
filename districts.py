import geopandas
import matplotlib.pyplot as plt 
import pandas
import os
import osr
import string

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
  return gdf

def label_anch_rep_districts(plot):
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

def house_sen_dict():
  dct = dict()
  letters = list(string.ascii_uppercase)
  j = 0
  for i in range(1, 41):
    dct[i] = letters[j]     
    if i%2 == 0:
      j += 1
  return dct 

HOUSE_LABEL_DICT = house_sen_dict()

def sen_label(i):
  return str(i) + ' - ' + HOUSE_LABEL_DICT[i]

def label_anch_sen_districts(plot):
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
