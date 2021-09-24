import requests
import random
import json
from hashlib import md5

def make_md5(s,encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

appid = '****************' #百度翻译API申请的appid  https://api.fanyi.baidu.com/
appkey = '************'
from_lang = 'en'
to_lang = 'zh'
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path
query = input('请输入需要翻译的单词或语句：')
#query = 'apple'

salt = random.randint(32768, 65536)

sign = make_md5(appid + query + str(salt) + appkey)
#print(sign,len(sign))

headers = {'Content-Type':'application/x-www-form-urlencoded'}
payload = {'appid':appid,'q':query,'from':from_lang,'to':to_lang,'salt':salt,'sign':sign}
r = requests.post(url,params=payload,headers=headers)
result = r.json()
print('翻译结果为:',result['trans_result'][0]['dst'])
