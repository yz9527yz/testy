"""
time        时钟时间与处理器运行时间都可以获取
datetime    时间模块：模块提供了日期与时间的高级接口
calendar    日历模块：模块微同意日历相关函数，用于创建周，数月，数年的周期性事件

date 类
优先展示部分该类的属性和方法，都是记忆层面的知识。

min、max：date 对象能表示的最大、最小日期；
resolution：date 对象表示日期的最小单位，返回天；
today()：返回表示当前本地日期的 date 对象；
fromtimestamp(timestamp)：根据时间戳，返回一个 date 对象。

"""
import datetime
import time
from datetime import date,datetime

# print(time.gmtime())
# print(time.time())
# localtime = time.localtime((time.time()))
# print("本地时间：",localtime)
#

print('date.min:', date.min)
print('date.max:', date.max)
print('date.resolution:', date.resolution)
print('date.today():', date.today())
print('date.fromtimestamp():', date.fromtimestamp(time.time()))



print(datetime.now)