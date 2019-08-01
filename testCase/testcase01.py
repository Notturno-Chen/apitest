# 读取userCase.xlsx中的用例，使用unittest进行断言校验

import json
import unittest
import urllib.parse

import geturlParams
import paramunittest
import readExcel
from common.configHttp import RunMain

url = geturlParams.geturlParams().get_url()
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')

@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):

	def setParameters(self, case_name, path, query, method):
		'''
		set params
		:param case_name:
		:param path:
		:param query:
		:param method:
		:return:
		'''
		self.case_name = str(case_name)
		self.path = str(path)
		self.query = str(query)
		self.method = str(method)

	def description(self):
		'''
		test report description
		:return:
		'''
		self.case_name

	def setUp(self):
		'''

		:return:
		'''
		print(self.case_name + '测试开始前准备')

	def testcase01(self):
		self.checkResult()

	def tearDown(self):
		print('测试结束，输出log完结\n\n')

	# 断言,待理解
	def checkResult(self):  #这个函数待理解
		'''
		check test result
		:return:
		'''
		url1 = 'http://www.xxx.com/login?' # 是否随意一个地址？
		new_url = url1 + self.query
		data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
		info = RunMain().run_main(self.method, url, data1)
		rs = json.loads(info)
		if self.case_name == 'login':
			self.assertEqual(rs['code'], 200)
		if self.case_name == 'login_error':
			self.assertEqual(rs['code'], -2)
		if self.case_name == 'login_null':
			self.assertEqual(rs['code'], 10001)

if __name__ == '__main__':
	print(url)
	print(login_xls)
