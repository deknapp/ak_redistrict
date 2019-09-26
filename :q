import geopandas
import matplotlib.pyplot as plt 
import pandas
import os
import osr

def get_district_df():
  os.system('SHAPE_RESTORE_SHX=YES fio info shapefiles/2013_districts.shp')
  district_file = 'shapefiles/2013_districts.shp'
  full_file = os.path.join(os.getcwd(), district_file)
  df = geopandas.read_file(full_file) 
  return df 

def get_district_gdf():
  os.system('SHAPE_RESTORE_SHX=YES fio info shapefiles/2013_districts.shp')
  prj_name = 'shapefiles/2013_precincts_proj.prj'
  full_name = os.path.join(os.getcwd(), prj_name)
  prj = open(full_name)
  proj4 = osr.SpatialReference(prj.read()).ExportToProj4()
  district_file = 'shapefiles/2013_districts.shp'
  full_file = os.path.join(os.getcwd(), district_file)
  df = geopandas.read_file(full_file) 
  geometry = df['geometry'].to_crs(proj4)
  gdf = geopandas.GeoDataFrame(df, geometry=geometry, crs=proj4) 
  return gdf

def label_rep_districts(plot):
  df = get_district_df()
  i = 1
  prj_name = 'shapefiles/2013_precincts_proj.prj'
  full_name = os.path.join(os.getcwd(), prj_name)
  prj = open(full_name)
  proj4 = osr.SpatialReference(prj.read()).ExportToProj4()
  for geo in df.geometry.to_crs(proj4): 
    if i == 22:
      text = plot.annotate(str(i), xy=(geo.centroid.x - 0.015, geo.centroid.y))
      text.set_fontsize(9) 
    elif i == 21:
      text = plot.annotate(str(i), xy=(-149.98, 61.18))
      text.set_fontsize(9) 
    elif i == 24:
      text = plot.annotate(str(i), xy=(-149.95, 61.11))
      text.set_fontsize(9) 
    elif i == 27:
      text = plot.annotate(str(i), xy=(-149.73, 61.165))
      text.set_fontsize(9) 
    elif i == 15:
      text = plot.annotate(str(i), xy=(geo.centroid.x, geo.centroid.y - 0.03))
      text.set_fontsize(9) 
    elif i == 18:
      text = plot.annotate(str(i), xy=(geo.centroid.x, 61.185))
      text.set_fontsize(9) 
    elif i == 28:
      text = plot.annotate(str(i), xy=(-149.73, 61.09))
      text.set_fontsize(9) 
    elif i == 14:
      text = plot.annotate(str(i), xy=(-149.7, 61.2))
      text.set_fontsize(9) 
    elif i == 13:
      text = plot.annotate(str(i), xy=(-149.72, 61.24))
      text.set_fontsize(9) 
    else: 
      text = plot.annotate(str(i), xy=(geo.centroid.x, geo.centroid.y))
      text.set_fontsize(9) 
    i = i + 1
  return plot 
