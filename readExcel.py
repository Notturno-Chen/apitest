# 读取Excel中case的方法

import os

import getpathInfo
# 调用第三方库xlrd
from xlrd import open_workbook

# 获取项目的绝对路径
path = getpathInfo.get_Path()

class readExcel():

	def get_xls(self, xls_name, sheet_name):
		cls = []
		# 获取case文件路径
		xlsPath = os.path.join(path, 'testFile', xls_name)
		# 打开case文件
		file = open_workbook(xlsPath)
		# 获得case文件的sheet
		sheet = file.sheet_by_name(sheet_name)
		# 获取sheet行数
		nrows = sheet.nrows
		for i in range(nrows):
			if sheet.row_values(i)[0] != u'case_name':
				cls.append(sheet.row_values(i))
		return cls

if __name__ == '__main__':
	print(readExcel().get_xls('userCase.xlsx', 'login'))
	print(readExcel().get_xls('userCase.xlsx', 'login')[0][1])
	# print(readExcel().get_xls('userCase.xlsx', 'login')[1][2])

