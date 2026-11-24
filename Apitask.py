import requests,json
url="https://jsonplaceholder.typicode.com/posts/2"
data={
    "user Id":2,
    "id":12,
    "title":"Python API",
    "body":"Put method using params and data"
}
try:
    response=requests.put(url,json=data)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("API call was unsuccessful")
    print(e)
with open("file.json","w")as file:
    json.dump(response.json(),file)