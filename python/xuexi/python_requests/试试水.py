import requests

url = 'http://47.106.169.149:8285/api/Admin/Login'

data = {
  "schoolNum": "0002",
  "account": "admin",
  "pwd": "digiin.123"
}
res = requests.post(url=url,json=data)
# print(res)
print(res.text)
msg = '账号密码不正确1'
assert msg == res.json()['msg'], '测试不通过'