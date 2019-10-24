ANCHORAGE = 'Anchorage Municipality'
BETHEL = 'Bethel Census Area'
FAIRBANKS = 'Fairbanks North Star Borough'
VALDEZ_CORDOVA = 'Valdez-Cordova Census Area'
NW_ARCTIC = 'Northwest Arctic Borough'
MATSU = 'Matanuska-Susitna Borough'
HYDER = 'Prince of Wales-Hyder Census Area'
JUNEAU = 'Juneau City and Borough'
ALEUTIANS_EAST = 'Aleutians East Borough'
ALEUTIANS_WEST = 'Aleutians West Census Area'
DENALI = 'Denali Borough'
BRISTOL = 'Bristol Bay Borough'
KENAI = 'Kenai Peninsula Borough'
OUT_OF_STATE = 'Out of State'
HAINES = 'Haines Borough'
SE_FAIRBANKS = 'Southeast Fairbanks Census Area'
WRANGELL = 'Wrangell City and Borough'
SITKA = 'Sitka City and Borough'
LAKE = 'Lake and Peninsula Borough'
DILLINGHAM = 'Dillingham Census Area'
HOONAH = 'Hoonah-Angoon Census Area'
KETCHIKAN = 'Ketchikan Gateway Borough'
KODIAK = 'Kodiak Island Borough'
KUSILVAK = 'Kusilvak Census Area'
NOME = 'Nome Census Area'
NORTH_SLOPE = 'North Slope Borough'
PETERSBURG = 'Petersburg Census Area'
SKAGWAY = 'Skagway Municipality'
YAKUTAT = 'Yakutat Census Area'
YUKON = 'Yukon-Koyukuk Census Area'

PLACE_LIST = [ANCHORAGE, BETHEL, FAIRBANKS, VALDEZ_CORDOVA, NW_ARCTIC, MATSU, HYDER, JUNEAU, ALEUTIANS_EAST, ALEUTIANS_WEST, DENALI, BRISTOL, KENAI, OUT_OF_STATE, HAINES, SE_FAIRBANKS, WRANGELL, SITKA, LAKE, DILLINGHAM, HAINES, HOONAH, KETCHIKAN, KODIAK, KUSILVAK, NOME, NORTH_SLOPE,
PETERSBURG, SKAGWAY, YAKUTAT, YUKON]

SHORT_PLACES = [name.split()[0] for name in PLACE_LIST]

BIG_CITIES = [ANCHORAGE, JUNEAU, FAIRBANKS]
RURAL_NORTHERN = [NW_ARCTIC, DENALI, NORTH_SLOPE, YUKON, NOME]
RURAL_SOUTHEAST = [HYDER, HAINES, WRANGELL, SITKA, HOONAH, KETCHIKAN, PETERSBURG, YAKUTAT, SKAGWAY]
RURAL_WESTERN = [ALEUTIANS_EAST, ALEUTIANS_WEST, BRISTOL, LAKE, DILLINGHAM, KUSILVAK] 
RURAL_BIG = [DILLINGHAM, YUKON, NOME, BRISTOL, LAKE, NW_ARCTIC, NORTH_SLOPE]
ALL_RURAL = RURAL_NORTHERN + RURAL_SOUTHEAST + RURAL_WESTERN

RURAL_AREA_DICT = {'Rural Western': RURAL_WESTERN, 'Rural Southeast': RURAL_SOUTHEAST, 'Rural Northern': RURAL_NORTHERN}
RURAL_TOTAL_DICT ={'Rural': ALL_RURAL}

LOW_DISTRICTS_ANCH = [13, 14, 19, 20, 21]
HIGH_DISTRICTS_MATSU = [7, 8, 9, 10, 11, 12]




 
