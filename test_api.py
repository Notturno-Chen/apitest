# 本地测试的接口服务demo

import flask
import json
from flask import request

'''
flask: web框架，提供的装饰器@server.route()可以将普通函数转换成服务
'''

# 创建一个服务，把当前的python文件当做一个服务
server = flask.Flask(__name__)
# @server.route()可以将普通函数转变为服务，参数为接口路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
	# 获取通过url请求传参的数据（username、pwd）
	username = request.values.get('name')
	pwd = request.values.get('pwd')
	# 判断用户名密码
	if username and pwd:
		if username == 'chen' and pwd == '123':
			resu = {'code': 200, 'message': '登录成功！'}
			# 将字典转换成字符串
			return json.dumps(resu, ensure_ascii=False)
		else:
			resu = {'code': -1, 'message': '账号密码错误！'}
			return json.dumps(resu, ensure_ascii=False)
	else:
		resu = {'code': 10001, 'message': '参数不能为空！'}
		return json.dumps(resu, ensure_ascii=False)

if __name__ == '__main__':
	server.run(debug=True, port=8888, host='127.0.0.1')
