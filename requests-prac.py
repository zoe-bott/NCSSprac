import requests

response = requests.get('https://httpbin.org/get')
print(response.json)

if response.ok:
    print ('Request successful')
else:
    print ('Request unsuccessful')
