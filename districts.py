import geopandas
import matplotlib.pyplot as plt 
import pandas
import os
import osr
import string
import names
import descartes
import label
import string
import legislators

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
      
def label_districts(plot, label_dict=None, shade=False, typ=None):
  df = get_district_df(HOUSE_SHAPE)
  i = 1
  prj_name = 'shapefiles/2013_precincts_proj.prj'
  full_name = os.path.join(os.getcwd(), prj_name)
  prj = open(full_name)
  proj4 = osr.SpatialReference(prj.read()).ExportToProj4()
  for geo in df.geometry.to_crs(proj4): 
    if i in names.LOW_DISTRICTS_ANCH:
      plot.add_patch(descartes.PolygonPatch(geo, fc='m', alpha=0.3))
    elif i in names.HIGH_DISTRICTS_MATSU:
      plot.add_patch(descartes.PolygonPatch(geo, fc='b', alpha=0.3))
    if typ == legislators.SEN:
      txt = label.sen_label(i)
    else:
      txt = str(i)  
    text = label.annotate_label(plot=plot, text=txt, i=i, centroid=geo.centroid, label_dict=label_dict) 
    text.set_fontsize(9)
    i = i + 1
  return plot



 
