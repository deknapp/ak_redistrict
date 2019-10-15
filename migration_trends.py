import migration 
import names
import matplotlib.pyplot as plt

def get_net_migration_list(first_year, last_year, dest, source):
  lst = []
  for i in range(first_year, last_year):
    dct = migration.migration_dict(i, i+1)
    if i == 2010:
      print(dct)
    to_val = 0
    to_val = dct[source][dest] 
    from_val = 0
    from_val = dct[dest][source] 
    net_val = to_val - from_val
    lst.append(net_val)
  return lst

def plot_migration(frm, to, start_year, end_year):
  lst = get_net_migration_list(start_year, end_year, to, frm)
  title = 'Migration From ' + frm + ' To ' + to
  x_vals = range(start_year, end_year+1)
  y_vals = [0]
  for val in lst:
    y_vals.append(y_vals[-1] + val)
  plt.title('Migration from Bethel to Anchorage since last census')
  plt.ylabel('Net migration from Bethel to Anchorage since ' + str(start_year))
  plt.xlabel('Year')
  plt.plot(x_vals, y_vals)
  plt.savefig('/Users/nknapp/Desktop/akpirg/migration_' + frm + '_' + to + '_' + str(start_year) + '_' + str(end_year) + '.png') 

plot_migration(names.BETHEL, names.ANCHORAGE, 2010, 2016)

