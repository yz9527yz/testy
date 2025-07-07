"""
语法
[表达式 for 迭代变量 in 可迭代对象 [if 条件表达式]]

"""
# my_list = [1,2,3]
# # new_list = []
# # for i in my_list:
# #     new_list.append(i**2)
# #
#
# new_list =[i**2 for i in my_list]
# print(new_list)

# my_list = [1, 2, 3,4,8]
# new_list = [item * 2 for item in my_list]
# new_list1 = [item for item in my_list if item >2]
# print(new_list)
# print(new_list1)
# my_dict = {key: value for key in range(2) for value in range(4)}
# print(my_dict)
class Animal:
    def __enter__(self):
        print("__enter__()")

    def __exit__(self, type, value, trace):
        print("__exit__()")


with Animal() as animal:
    pass
