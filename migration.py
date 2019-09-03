import os

MIGRATION_CSV_DIRECTORY = 'csv_files/migration_csv_files'
CHANGE_HEADER_LINE = 6
FIRST_CHANGE_LINE = 8
LAST_CHANGE_LINE = 33
TOTALS_LINE = 35

# returns dict showing migration between two different years
def read_file(file_name):
  full_file_name = os.path.join(os.getcwd() + MIGRATION_CSV_DIRECTORY, file_name)
  handle = open(full_file_name, 'r')
  lines = handle.readlines()
  header_line = lines[HEADER_LINE-1]
  to_names = header_line.split(','][2:-2]
  to_from_dict = {]
  for name in to_names:
    to_from_dict[name] = {}
  for line in lines[FIRST_CHANGE_LINE-1, LAST_CHANGE_LINE-1]:
    split_line = line.split(',')
    area_name = split_line[0]
    from_name = area_name.split('in')[-1]
    i = 2
    for number in split_line[2:-2]:
      to_from_dict[header_line[i]] = number
      i = i + 1
