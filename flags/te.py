import csv
def read_csv(path):
    with open(path, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        data1_data2 = [row for row in reader]
        return data1_data2

li = read_csv('./list.csv')
print(li)