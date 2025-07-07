import csv

with open('my_csv_1.csv', 'r', encoding='utf8') as f:
    data = csv.reader(f)
    print(data)

    for i in data:
        print(i)

# f = open('my_csv_1.csv','r',encoding='utf8')
# #
# data = f.read()
# print(data)
# f.close()