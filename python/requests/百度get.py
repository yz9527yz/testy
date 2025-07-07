import requests
url = "https://www.baidu.com/"
params1 = {"id":1001}
params2 = {"id":"1001,1003"}
params3 = {"id":1001,"kw":"北京"}
response = requests.get(url,params=params3)
response.encoding = "utf-8"
print("请求的URL:",response.url)
print("请求的返回状态码:",response.status_code)
print("获取请求编码：",response.encoding)
print("请求的请求头:",response.headers)
print("请求的请求头Cache-Control:",response.headers['Cache-Control'])

print(type(response.headers))
#print(response.json)
print("请求的cookies:",response.cookies)
print("以text获取响应：",response.text)