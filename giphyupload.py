import requests

url = ""
response = requests.post("", params={
    'api_key':"",
    'source_url_img': url,
    'tags':'octotim'
})

print(response)
print(response.content)
print(respose.json())