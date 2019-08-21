csv_file_name = './lgaddr.csv'
better_file_name = './lgaddr_corrected.csv'
handle = open(csv_file_name, 'r')
lines = handle.readlines()[1:]

lga_list = list()

for line in lines:
  split_line = line.split(',')
  if len(split_line[2]) < 2:
    continue
  legislator = split_line[1]
  address_number = split_line[2].split()[0]
  street_name = ' '.join(split_line[2].split()[1:])
  lga_list.append(legislator + ',' + address_number[1:] + ',' + street_name + '\n')

handle = open(better_file_name, 'w')
for lga in lga_list:
  handle.write(lga)   




