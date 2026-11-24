import requests
url="https://jsonplaceholder.typicode.com/posts/1"
data={
    "user id":1,
        "username":"John",
        "title": "Learning Python API",
         "body": "I am practising PUT method using Python requests."
    }
response=requests.put(url,json=data)
print(f"statuscode:{response.status_code}")
print(response.text)
