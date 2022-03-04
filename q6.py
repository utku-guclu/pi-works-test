# q6

import csv

total_vax_number = []
with open('country_vaccination_stats.csv', 'r+') as f:
    file = csv.reader(f)
    next(file)

    total_vax = 0
    for row in file:
        if row[1] == '1/6/2021':
            if row[2] == "":
                continue
            total_vax += int(row[2])

    total_vax_number.append(total_vax)

new_data = open('country_vaccination_stats.csv', 'w')
writer = csv.writer(new_data)
writer.writerow(total_vax_number)
