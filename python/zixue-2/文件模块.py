import os
print(os.getcwd())
ret = os.path.abspath('函数.py')
print(os.path.getsize('函数.py'))
print(ret)
print(os.listdir('.'))

# 文件地址，注意提前在当前目录新建一愕test.txt文件
file = "test.txt"
# 打开文件
f = open(file,encoding='utf-8')
# 读取文件全部内容
read_str = f.read()
# 关闭文件
f.close()
print(read_str)
path = os.getcwd()

with open(file,mode='w',encoding='utf-8') as e:
    # 写人文件内容
    e.write("我是即将被写人的内容")

print(read_str)