s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')


print('--------------------------------------')


s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')




s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

print('--------------------------------------')
s1 = r'\'hello, world!'
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')

print('--------------------------------------')

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

a, b = 5, 10
print(f'{a} * {b} = {a * b}')

list1 = [1, 3, 5, 7, 100]
for index, elem in enumerate(list1):
    if elem == 5:
        print(index, elem)
        break
    print(index, elem)

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

f = (x ** 2 for x in range(1, 1000))
print(f)
list5= [35,25]
set1 = {1,2,3,'s',list5}
print(set1)