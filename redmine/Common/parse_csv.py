import csv


def parse_csv(file):
    mylist = []
    with open(file, 'r',encoding='utf-8') as f:
        data = csv.reader(f)

        for i in data:
            mylist.append(i)

        del mylist[0] # 删除标题行的数据
        return mylist


if __name__ == '__main__':
    file = r'E:\pythonfile\redmine\Data\my_csv_1.csv'
    data = parse_csv(file)
    print(data)

