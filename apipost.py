import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "user id":1,
    "username":"John",
    "body":"quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
response=requests.post(url,json=data)
print(f"statuscode:{response.status_code}")
print(response.json())
###########################################################################
url="https://jsonplaceholder.typicode.com/posts"
params={
    'userId':2,
    'id':12
}
data={
    "title":"Python API",
    "body":"Post method using params and data"
}
response=requests.post(url,params=params,json=data)
print(response.status_code)
print(response.json())
