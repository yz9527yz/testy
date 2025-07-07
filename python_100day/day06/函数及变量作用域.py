
"""
格式化输出
方式一
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

方式二
a, b = 5, 10
print(f'{a} * {b} = {a * b}')
"""

def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False

print(is_prime(6))