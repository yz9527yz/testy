"""
lambda [参数列表]:表达式
# 英文语法格式
lambda [arg1[,arg2,arg3....argN]]:expression
语法格式中有一些注意事项：

lambda 表达式必须使用 lambda 关键字定义；
lambda 关键字后面，冒号前面是参数列表，参数数量可以从 0 到任意个数。多个参数用逗号分隔，
冒号右边是 lambda 表达式的返回值。
"""
list = [12,12,8,52,1]
fun = lambda x:x+1
print(fun(5))
# 进一步简写
# print((lambda x: x+1)(4))
my_list = [(1, 2), (3, 1), (4, 0), (11, 4)]

my_list.sort(key=lambda x: x[1])

print(my_list)
