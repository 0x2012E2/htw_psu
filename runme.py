import csv
with open('wirelessoverview-03.csv', 'rb') as f:
  reader = csv.reader(f)
  data_as_list = list(reader)

print data_as_list
print data_as_list[2][3]