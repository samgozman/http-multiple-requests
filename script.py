import http.client
from time import sleep

conn = http.client.HTTPSConnection("cont.ws")

headers = {
    'cache-control': "no-cache",
    'Accept': 'text/html',
    'Accept-Language': 'ru, ru-RU',
    'Accept-Charset': 'windows-1251',
    }


for i in range(2):
    conn.request("GET", "/@id547696745/1356350", headers=headers)
    res = conn.getresponse()
    if res.status != 200:
        print("Error " + res.status)
        break
    sleep(1)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))