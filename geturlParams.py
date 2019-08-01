# 定一个类，获取接口的URL、参数、method等，并进行参数动态化

import readConfig

# 实例化
readConfig = readConfig.readConfig()

# 从配置文件读取内容并拼接
class geturlParams():

	def get_url(self):
		# 其中/login可以通过readExcel进行读取
		new_url = readConfig.get_http('scheme') + '://' + readConfig.get_http('baseurl') + ':' \
				  + readConfig.get_http('port') + '/login' + '?'
		return new_url

if __name__ == '__main__':
	new_url = geturlParams().get_url()
	print(new_url)