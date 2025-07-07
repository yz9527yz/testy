# 函数语法

# def 参数名称([参数列表])
#     函数体
#     [return 值]

# 无参函数
# 无返回值
def a():
    print("你好中国")


# 函数调用
#  a()
# 有返回值

def c():
    a = int(input("请输入a的值"))
    b = int(input("请输入b的值"))
    return a + b


# print(c())

def e(a, b, c=3):
    return a + b + c


print(e(2, 3,1))
