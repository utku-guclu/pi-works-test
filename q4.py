# q4

import csv

data = []

with open('country_vaccination_stats.csv', 'r+') as f:
    file = csv.reader(f)

    for row in file:
        if row[2] == "":
            row[2] = '0'
        data.append(row)

new_data = open('country_vaccination_stats.csv', 'w')
writer = csv.writer(new_data)

for row in data:
    writer.writerow(row)
