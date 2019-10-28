# Constants to show geographic location

ANCH_MAX_LONG = -149.68
ANCH_MIN_LONG = -150.01
ANCH_MIN_LAT = 61.08
ANCH_MAX_LAT = 61.25

FAIRBANKS_MAX_LONG = -148
FAIRBANKS_MIN_LONG = -147.25
FAIRBANKS_MIN_LAT = 64.7
FAIRBANKS_MAX_LAT = 64.9

FAIRBANKS_SEN_MAX_LONG = -148
FAIRBANKS_SEN_MIN_LONG = -147.25
FAIRBANKS_SEN_MIN_LAT = 64.78
FAIRBANKS_SEN_MAX_LAT = 64.9

MATSU_MAX_LONG = -145
MATSU_MIN_LONG = -155
MATSU_MIN_LAT = 58
MATSU_MAX_LAT = 66

JUNEAU_MAX_LONG = -136
JUNEAU_MIN_LONG = -132
JUNEAU_MIN_LAT = 56
JUNEAU_MAX_LAT = 60

class Coords:
  def __init__(self, min_lat=None, max_lat=None, min_long=None, max_long=None):
    self.min_lat = min_lat
    self.max_lat = max_lat
    self.min_long = min_long
    self.max_long = max_long

ANCHORAGE = Coords(min_lat=ANCH_MIN_LAT, max_lat=ANCH_MAX_LAT, min_long=ANCH_MIN_LONG, max_long=ANCH_MAX_LONG)
MATSU = Coords(min_lat=MATSU_MIN_LAT, max_lat=MATSU_MAX_LAT, min_long=MATSU_MIN_LONG, max_long=MATSU_MAX_LONG)
JUNEAU = Coords(min_lat=JUNEAU_MIN_LAT, max_lat=JUNEAU_MAX_LAT, min_long=JUNEAU_MIN_LONG, max_long=JUNEAU_MAX_LONG)
FAIRBANKS_REPS = Coords(min_lat=FAIRBANKS_MIN_LAT, max_lat=FAIRBANKS_MAX_LAT, min_long=FAIRBANKS_MIN_LONG, max_long=FAIRBANKS_MAX_LONG)
FAIRBANKS_SENS = Coords(min_lat=FAIRBANKS_SEN_MIN_LAT, max_lat=FAIRBANKS_SEN_MAX_LAT, min_long=FAIRBANKS_SEN_MIN_LONG, max_long=FAIRBANKS_SEN_MAX_LONG)



