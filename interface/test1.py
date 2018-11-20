#coding:utf-8
import requests
import json
#r = requests.get('http://www.cnblogs.com/yoyoketang/')
#par = {"Keywords":"yoyoketang"}
#r = requests.get('http://zzk.cnblogs.com/s/blogpost?Keywords=yoyoketang',params=par)
payload = {"yoyo":"hello world","pathonQQ群":"226296743"}
#r = requests.get("https://www.baidu.com")
data_json = json.dumps(payload)
r = requests.post('http://httpbin.org/post',json=data_json)
print(r.encoding)
print(r.content)
print(r.text)

