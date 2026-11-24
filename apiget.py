import requests
'''r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"statuscode: {r.status_code}")
print(f"headers: {r.headers}")
print(f"body: {r.json()}")
#print(f"content type: {r.headers['Content-Type']}")
#print(r.headers.get('Content-Type'))
print(r.encoding)
print(r.text)
###########################################################################
url="https://jsonplaceholder.typicode.com/posts?userId=2"
response=requests.get(url)
print(response.status_code)
print(response.json())'''
###########################################################################
url="https://jsonplaceholder.typicode.com/posts"
params={
    "userId":2,
    "id":12
}
response=requests.get(url,params=params)
print(response.status_code)
print(response.json())