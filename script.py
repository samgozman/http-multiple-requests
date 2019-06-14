import http.client, ssl, tqdm
from time import sleep

print("Enter domain (like google.com):")
domain = input()
print("Enter page (like /search):")
page = input()
print("Enter iterations range (like 10 or 5000):")
count = int(input())
print("Enter delay in sec (like 0.1 or 5):")
delay = float(input())

if domain is None or page is None or count is None:
    exit()

conn = http.client.HTTPSConnection(domain, context = ssl._create_unverified_context())

headers = {
    'cache-control': "no-cache",
    'Accept': 'text/html',
    'Accept-Language': 'ru, ru-RU',
    'Accept-Charset': 'windows-1251',
    }


for i in tqdm.tqdm(range(count)):
    conn.request("GET", page, headers=headers)
    res = conn.getresponse()
    if res.status != 200:
        print("Error " + res.status)
        break
    conn.close()
    sleep(delay)