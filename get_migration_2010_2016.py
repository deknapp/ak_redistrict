import migration

def get_file_for_years(yearA, yearB):
  return str(yearA) + '-' + str(yearB) + '-Table 1.csv'

def migration_dict(yearA, yearB):
  return migration.read_file(get_file_for_years(yearA, yearB))

dct = migration_dict(2010, 2011)

