import requests
import json

word=input('input your name>>>')
url='http://www.tuling123.com/openapi/api?'
params={}
params['key']='ec961279f453459b9248f0aeb6600bbe'
params['info']=word
res=requests.get(url=url,params=json.dumps(params))
print(res.text)