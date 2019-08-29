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

def label_districts(plot):
  df = get_district_df()
  i = 1
  for x, y, label in df.Longitude, df.Latitude, df.Legislator):
    text = plot.annotate(str(i))
    text.set_fontsize(15) 
    i++ 
 

