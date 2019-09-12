import os

MIGRATION_CSV_DIRECTORY = 'csv_files/migration_csv_files'
CHANGE_HEADER_LINE = 6
FIRST_CHANGE_LINE = 8
LAST_CHANGE_LINE = 33
TOTALS_LINE = 35

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
    split_line = cleaned_line.split(',')
    area_name = split_line[0]
    from_name = area_name.split('in')[1]
    if len(area_name.split('in')) > 2:     
      for name_part in area_name.split('in')[2:]:
        from_name = from_name + 'in' + name_part
    i = 2
    to_from_dict[from_name] = dict()
    for number in split_line[2:-3]:
      if i > len(split_header_line) - 1:
        break
      to_from_dict[from_name][split_header_line[i]] = number
      i = i + 1
  return to_from_dict

