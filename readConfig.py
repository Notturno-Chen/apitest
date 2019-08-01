# 读取配置文件的方法，并返回文件内容

import configparser
import os
import getpathInfo  # 引入获取路径的类

# 调用实例化
path = getpathInfo.get_Path()
# 在path路径下加一级路径，变成...\path\config.ini
config_path = os.path.join(path, 'config.ini')
# 调用读取配置文件的方法
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

class readConfig():

	def get_http(self, name):
		value = config.get('HTTP', name)
		return value

	def get_email(self, name):
		value = config.get('EMAIL', name)
		return value

	# 数据库读取，扩展备用
	def get_mysql(self, name):
		value = config.get('DATABASE', name)
		return value

if __name__ == '__main__':
	print('HTTP中的baseurl值为：', readConfig().get_http('baseurl'))
	print('EMAIL中的开关on_off值为：', readConfig().get_email('on_off'))

