import migration

def get_file_for_years(yearA, yearB):
  return str(yearA) + '-' + str(yearB) + '-Table 1.csv'

def migration_dict(yearA, yearB):
  return migration.read_file(get_file_for_years(yearA, yearB))

dct_list = []
for i in range(2010, 2016):
  dct_list.append(migration_dict(i, i+1)) 

sum_dict = migration.add_migration_dicts(dct_list)

for key in sum_dict:
  print('------------------------')
  print(key)
  print('------------------------')
  for k in sum_dict[key]:
    val = sum_dict[key][k]
    print(k, val)
  


