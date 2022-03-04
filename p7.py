# q7

import csv


def median(data):
    total = 0
    len_count = 0

    for key, value in data.items():
        total += value
        len_count += 1

    return total / len_count


sql = []
data = {}
query = {}

with open('country_vaccination_stats.csv', 'r+') as f:
    file = csv.reader(f)
    next(file)

    for row in file:
        if row[0] in data:
            data[row[0]] += 1
        else:
            data[row[0]] = 1
        sql.append(row)

    sufficient_data = median(data)

    for key, value in data.items():
        if value < sufficient_data:
            query[key] = 0
        else:
            for item in sql:
                if item[2] == "" and item[0] not in query:
                    query[item[0]] = 1


new_data = open('country_vaccination_stats.csv', 'w')
writer = csv.writer(new_data)
writer.writerow(query.items())