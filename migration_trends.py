import migration 
import names
import matplotlib

def get_net_migration_list(first_year, last_year, dest, source):
  lst = []
  for i in range(first_year, last_year):
    dct = migration.migration_dict(i, i+1)
    to_val = 0
    to_val = dct[source][dest] 
    from_val = 0
    from_val = dct[dest][source] 
    net_val = to_val - from_val
    lst.append(net_val)
  return lst

def plot_migration(to, frm, lst, start_year, end_year):
  title = 'Migration From ' + frm + ' To ' + to
  x_vals = range(start_year, end_year+1)
  plt.   


print(get_net_migration_list(2010, 2016, names.ANCH, names.BETHEL))
