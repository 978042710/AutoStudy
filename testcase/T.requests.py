import  requests

r = requests.get('https://www.baidu.com')
print(r.status_code)
print(r.headers)
#print(r.json())
print(r.url)
print(r.cookies)
print(r.text)