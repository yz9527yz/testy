# 循环结构
# for in循环
# while循环
# range (a,b,c)

#      每秒打印一次“hello word”，持续一小时
"""
#  1-100求和
sum = 0
for i in range(101):
    sum += i
    if i == 100:
        print('1-100求和：='+str(sum))
    else:
        continue

# 1-100偶数求和
sum2 = 0
for i in range(0,101,2):
    sum2 +=i
    if i == 100:
        print('1-100偶数求和：='+str(sum2))


# 1-100奇数求和
sum3 = 0
for i in range(1,101,2):
    sum3 += i
    if i == 99:
        print('1-100奇数求和：='+str(sum3))

sum4 = 0
for i in range(101):
    if i % 2 == 0:
        sum4 += i
        if i == 100:
            print('1-100偶数求和：='+str(sum4))

"""
import random

"""
猜数字游戏
加算计出一个1-100之间的随机数由人来猜
计算机根据人猜数字分别给出提示大一点、小一点、猜对了


import random

answer = random.randint(1,100)
print(answer)
counter = 0
while True:
    counter += 1
    number = int(input("请输入："))
    if number > answer :
        print("小一点")
    elif number < answer:
        print("大一点")
    else:
        print("猜对啦")
        break

if counter > 7:
    print("你一共猜了{}次,你的智商明显不足啊".format(counter))
elif counter > 3:
    print("你一共猜了{}次,你的智商一般啦".format(counter))
else:
    print("你{}次就猜对啦,真是天才啊".format(counter))

# 输出九九乘法表

for i in range(1,10):
    for j in range(1,i + 1):
        print('{}*{}={}\t'.format(j,i,i*j),end='')
    print()
"""
# 输入一个正整数判断是不是素数
# 素数指的是只能被1和自身整除的大于1的整数。
num = int(input("请输入一个正整数："))
n = 0
atatus = True
for i in range(2,num+1):

    if num % i == 0 :
        atatus = False
        break
if atatus and num != 1:

    print(f'{num}是一个素数')
else:

    print(f'{num}不是一个素数')

# from math import sqrt
#
# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))
# print(end)
# is_prime = True
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         print(x)
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)