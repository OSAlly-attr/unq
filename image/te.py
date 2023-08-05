import csv
list1 = []

with open('list1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        list1.append(row)

print(list1)