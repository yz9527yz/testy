import csv

def parse_csv(file):
    mylist = []

    with open(file,'r',encoding='utf8') as f:
        data = csv.reader(f)
        for i in data:
            mylist.append(i)
    del mylist[0]  # 删除标题行的数据
    return mylist

if __name__ == '__main__':
    data = parse_csv('my_csv_.csv')