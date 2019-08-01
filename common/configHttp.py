# 通过get、post、put、delete等方法来进行http请求，并获得请求响应

import requests
import json

class RunMain():

	def send_post(self, url, data):
		# 参数必须按url、data顺序传入
		result = requests.post(url=url, data=data).json()
		# 输出为中文，按字母排序，缩进为2个字符
		res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
		return res

	def send_get(self, url, data):
		result = requests.get(url=url, data=data)
		res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
		return res

	# 通过传过来的method判断进行的是get或post请求，其中url和data是默认参数
	def run_main(self, method, url=None, data=None):
		result = None
		if method == 'post':
			result = self.send_post(url, data)
		elif method == 'get':
			result = self.send_get(url, data)
		else:
			print('method值错误！')
		return result

if __name__ == '__main__':
	# 用写死的参数验证请求是否正确，注意先运行test_api.py文件
	result = RunMain().run_main('post', 'http://127.0.0.1:8888/login', 'name=chen&pwd=123456')
	print(result)