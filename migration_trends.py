import migration 

def get_net_migration_list(first_year, last_year, area):
  lst = []
  for i in range(first_year, last_year):
    dct = migration.migration_dict(i, i+1)
    print(dct)
    exit()
    #to_val = 
    #from_val = 
    #net_val = to_val - from_val
    #lst.append(net_val)
  return lst

print(get_net_migration_list(2010,2011, 'blah')) 
