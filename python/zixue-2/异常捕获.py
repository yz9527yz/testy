print(8/0)

try:
    print(8/0)
except ZeroDivisionError as z:
    print("jixu")


try:
    pass
except ZeroDivisionError as z:
    pass
except SyntaxError as s:
    pass
else:
    pass
finally:
    print("必须执行")