"""
项目公共内容配置，以及读取配置文件中的配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import logging
import os

import redmine.Common.config
from redmine.Common.file_reader import YamlReader
import time
# 所有相关文件的路径

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'Data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'Logs')
REPORT_PATH = os.path.join(BASE_PATH, 'Report')
print('BASE_PATH = ' +BASE_PATH)
print('LOG_PATH = '+LOG_PATH)



rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
print('rq ='+rq)
log_path = os.path.dirname(os.getcwd()) + '/Logs/'
print('log_path = '+log_path)
file_name = log_path + rq + '.log'

config_log = logging.getLogger('redmine.Common.config')


class Config:
    def __init__(self, config=CONFIG_FILE):
        # print('配置文件地址：',config)
        self.config = YamlReader(config).data
        self.logger = logging.getLogger('redmine.Common.config.config')

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        self.logger.info('读取config.yml配置信息')
        return self.config[index].get(element)
