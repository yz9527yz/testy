"""
python中，字符串格式化有三种方式
1.%占位符格式化
2.format（）方法格式化
3.f-string
"""
# 2
my_str = "小爱同学，今天天气"
hai_str= '你好！我是：{}，请多多指教'.format('小明')
print(hai_str)


answer_str = '今天上午的天气是：{},下午的天气是：{}'.format('晴', '大雨')
print(answer_str)

# 3
answer_str = '今天上午的天气是：{shangwu},下午的天气是：{xiawu}'.format(shangwu='晴',xiawu = '大雨')
print(answer_str)