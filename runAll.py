# 接口自动化执行文件，待理解

import os
import getpathInfo
import readConfig
from common.configEmail import send_mail
import unittest
import common.HTMLTestRunner as HTMLTestRunner
import common.Log

# 项目根目录
path = getpathInfo.get_Path()
# 根目录/result
report_path = os.path.join(path, 'result')
on_off = readConfig.readConfig().get_email('on_off')
log = common.Log.logger

class AllTest:

	def __init__(self):
		global  resultPath
		resultPath = os.path.join(report_path, 'report.html')
		self.caseListFile = os.path.join(path, 'caselist.txt')
		self.caseFile = os.path.join(path, 'testCase')
		self.caseList = []
		# log.info('resultPath', resultPath)
		# log.info('caseListFile', self.caseListFile)
		# log.info('caseList', self.caseList)
		# log.info('resultPath'.format(resultPath))

	def set_case_list(self):
		'''
		读取caselist.txt文件中的用例名称，并加到caselist列表
		:return:
		'''
		print('******Test Start!******')
		fb = open(self.caseListFile, encoding='utf-8')   # 加上编码参数，很重要！！！不然报错
		for value in fb.readlines():
			data = str(value)
			if data != '' and not data.startswith('#'):
				self.caseList.append(data.replace('\n', ''))
		print(self.caseList)
		fb.close()

	def set_case_suite(self):
		'''

		:return:
		'''
		self.set_case_list()
		test_suite = unittest.TestSuite()
		suite_module = []
		for case in self.caseList:
			case_name = case.split('/')[-1]
			print(case_name + '.py')
			discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
			suite_module.append(discover)
			print('suite module:' + str(suite_module))

		if len(suite_module) > 0:
			for suite in suite_module:
				for test_name in suite:
					test_suite.addTest(test_name)
		else:
			print('else: this casefile is empty!')
			return None
		return test_suite

	def run(self):
		'''
		run test
		:return:
		'''
		try:
			suit = self.set_case_suite()
			print('try')
			print(str(suit))
			if suit is not None:
				print('if-suit')
				fp = open(resultPath, 'wb')
				runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
				runner.run(suit)
			else:
				print('There is no case to run!')
		except Exception as e:
			print(e)

		finally:
			print('******Test End!******')
			fp.close()

		if on_off == 'on':
			send_mail()
		else:
			print('Please check email config to send test report! ')

if __name__ == '__main__':
	AllTest().run()