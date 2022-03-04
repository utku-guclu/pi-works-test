# q5

import csv

data = {}

with open('country_vaccination_stats.csv', 'r+') as f:
    file = csv.reader(f)
    next(file)
    sum_vax = 0
    for row in file:
        if row[0] in data:
            sum_vax += int(row[2])
            data[row[0]] = sum_vax
        else:
            sum_wax = 0
            data[row[0]] = sum_vax


def top_countries(dic):
    return sorted(dic, key=dic.get, reverse=True)[:3]


top_three_countries = top_countries(data)

new_data = open('country_vaccination_stats.csv', 'w')
writer = csv.writer(new_data)
writer.writerow(top_three_countries)
