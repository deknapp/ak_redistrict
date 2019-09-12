import migration

def get_file_for_years(yearA, yearB):
  return str(yearA) + '-' + str(yearB) + '-Table 1.csv'

def migration_dict(yearA, yearB):
  return migration.read_file(get_file_for_years(yearA, yearB))

dict_2010_2011 = migration_dict(2010, 2011)

for key in dict_2010_2011:
  print(key)
  print('------------------------')
  for k in dict_2010_2011[key]:
    val = dict_2010_2011[key][k]
    if val != '-':
      print(val)
  


