import os
import getpathInfo
# import runAll
from readConfig import readConfig

# path = getpathInfo.get_Path()
# report_path = os.path.join(path, 'result')
# resultPath = os.path.join(report_path, 'report.html')
# fp = open(resultPath, 'wb')
# fp.close()

# ss = runAll.AllTest().set_case_list()
# print(ss)
aa = readConfig().get_email('on_off')
print(aa)

