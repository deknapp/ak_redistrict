import os

MIGRATION_CSV_DIRECTORY = 'csv_files/migration_csv_files'
FIRST_CHANGE_LINE = 8
LAST_CHANGE_LINE = 33
TOTALS_LINE = 35

# returns dict showing migration between two different years
def read_file(file_name):
  full_file_name = os.path.join(os.getcwd() + MIGRATION_CSV_DIRECTORY, file_name)
  handle = open(full_file_name, 'r')
  lines = handle.readlines()
  for line in lines[FIRST_CHANGE_LINE-1, LAST_CHANGE_LINE-1]:
    split_line = line.split(',')
    area_name = split_line[0]
    area_name_short = area_name.split('in')[-1]
         

