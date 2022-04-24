import csv
    
r = csv.reader(open('data/source.csv'))
header = next(r) #skip header
header1 = ['year', 'region', 'value']
data = list(r)
writer = csv.writer(open('data/result.csv', 'w', newline=''))
for line in data:
    line[0] = '{year}-{month}-{day}'.format(year = line[0], month = "01", day = "01")
writer.writerow(header1)
for line in data:
    writer.writerow(line)
