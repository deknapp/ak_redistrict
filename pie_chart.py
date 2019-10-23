import names
import matplotlib.pyplot as plt

def pie_chart_migration(to, start_year, end_year):
  inflow_dct = dict()
  outflow_dct = dict()
  for frm in names.PLACE_LIST:
    if frm != to:
      total = sum(get_net_migration_list(start_year, end_year, to, frm))
      if total > 0:
        outflow_dct[frm] = total
      elif total < 0:
        inflow_dct[frm] = total
  print("INFLOW")
  print(inflow_dct)
  print("OUTFLOW")
  print(outflow_dct)
  plt.clf()
  plt.rcParams["font.size"] = 8
  plt.title('Population inflow to ' + to + ' since '+ str(start_year))
  labels = inflow_dct.keys()
  values = inflow_dct.values()
  ten_percent_value = sum(values)/10.0
  end_labels = [label for label in labels if (inflow_dct[label] > ten_percent_value)]
  end_val = [val for val in values if val > ten_percent_value]
  fig1, ax1 = plt.subplots()
  ax1.pie(values, labels=labels)
  ax1.axis('equal')
  plt.savefig('/Users/nknapp/Desktop/akpirg/pie_charts/inflow_to_' + to + '.png')
  plt.clf()
  plt.rcParams["font.size"] = 8
  plt.title('Population outflow from ' + to + ' since '+ str(start_year))
  labels = outflow_dct.keys()
  values = outflow_dct.values()
  ten_percent_value = sum(values)/10.0
  end_labels = [label for label in labels if outflow_dct[label] > ten_percent_value]
  end_val = [val for val in values if val > ten_percent_value]
  fig1, ax1 = plt.subplots()
  ax1.pie(end_val, labels=end_labels)
  ax1.axis('equal')
  plt.savefig('/Users/nknapp/Desktop/akpirg/pie_charts/outflow_from_' + to + '.png')


def plot_all_pie_chart_migration(start_year, end_year):
  for to in names.PLACE_LIST:
    pie_chart_migration(to, start_year, end_year)
