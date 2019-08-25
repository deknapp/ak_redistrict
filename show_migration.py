import geopandas

boroughs = geopandas.read_file('borough/mv_borough_py.shp')
boroughs.head()
boroughs.plot()
