import csv
r = csv.reader(open('C:\\Users\\nurzh\\Desktop\\source.csv'))
lines = list(r)
lines[1][0] = '2020-1-1'
lines[2][0] = '2021-1-1'
writer = csv.writer(open('C:\\Users\\nurzh\\Desktop\\result.csv', 'w'))
writer.writerows(lines)