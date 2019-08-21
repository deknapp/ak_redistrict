csv_file_name = './lgaddr.csv'
better_file_name = './lgaddr_corrected.csv'
handle = open(tsv_file_name, 'r')
lines = handle.readlines()[1:]

lga_dict = {}

for line in lines:
  split_line = line.split(',')
  legislator = split_line[1]
  address_number = split_line[2].split()[0]
  street_name = split_line[2].split()[1:].join(' ')
  print(legislator, address_number, street_name) 
 




