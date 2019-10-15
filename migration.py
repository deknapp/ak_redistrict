import os

MIGRATION_CSV_DIRECTORY = 'csv_files/migration_csv_files'
CHANGE_HEADER_LINE = 6
FIRST_CHANGE_LINE = 8
LAST_CHANGE_LINE = 33
TOTALS_LINE = 35

def get_file_for_years(yearA, yearB):
  return str(yearA) + '-' + str(yearB) + '-Table 1.csv'

def migration_dict(yearA, yearB):
  return read_file(get_file_for_years(yearA, yearB))

def add_inner_dict(dctA, dctB):
  for key in dctB:
    if key not in dctA.keys():
      dctA[key] = dctB[key]
    else:
      dctA[key] = dctA[key] + dctB[key]
  return dctA

def add_migration_dicts(lst):
  sum_dict = {}
  for dct in lst:
    for key in dct:
      if key not in sum_dict.keys():
        sum_dict[key] = dict() 
      sum_dict[key] = add_inner_dict(sum_dict[key], dct[key])
  return sum_dict

# returns dict showing migration between two different years
def read_file(file_name):
  full_file_name = os.path.join(os.getcwd(), MIGRATION_CSV_DIRECTORY, file_name)
  handle = open(full_file_name, 'r')
  lines = handle.readlines()
  header_line = lines[CHANGE_HEADER_LINE-1]
  split_header_line = header_line.split(',')
  to_from_dict = {}
  for line in lines[FIRST_CHANGE_LINE-1:LAST_CHANGE_LINE-1]:
    quote_split_line = line.split('"')
    i = 0
    cleaned_line = ''
    for chunk in quote_split_line:
      if i%2 == 0:
        cleaned_line += chunk
      else:
        cleaned_line += chunk.replace(',',"")
      i = i+1 
    split_line = [chunk.strip() for chunk in cleaned_line.split(',')]
    area_name = split_line[0]
    from_name = area_name.split('in')[1].strip()
    if len(area_name.split('in')) > 2:     
      for name_part in area_name.split('in')[2:]:
        from_name = from_name + 'in' + name_part
    i = 2
    to_from_dict[from_name] = dict()
    for number in split_line[2:-3]:
      if i > len(split_header_line) - 1:
        break
      if number.isdigit():
        to_from_dict[from_name][split_header_line[i]] = int(number)
      i = i + 1
  return to_from_dict

