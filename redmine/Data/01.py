import csv

with open('my_csv_1.csv','r',encoding='utf-8') as f:
    data = csv.reader(f)
    print(data)
    for i in data:
        print(i)

