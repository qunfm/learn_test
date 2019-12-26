#coding:utf-8
import requests
import json

payload = {"test":"hello world","pathonQQ群":"1234567890"}
#r = requests.get("https://www.baidu.com")
data_json = json.dumps(payload)
r = requests.post('http://httpbin.org/post',json=data_json)
print(r.encoding)
print(r.content)
print(r.text)

