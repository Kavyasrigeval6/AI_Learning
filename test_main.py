from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_disp():
    response=client.get("/users")
    assert response.status_code==204

def test_add():
    response=client.post("/users",json=[{
    "id": 1,
    "userid": 100,
    "name": "Ria",
    "age": 24
     },
    {
    "id": 2,
    "userid": 101,
    "name": "Helen"
  },
  {
    "id": 3,
    "userid": 102,
    "name": "John",
    "age": 52
   }])
    assert response.status_code==201

def test_getuser():
    response=client.get("/users/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Helen"
def test_update():
    response=client.put("/users?id=3", json={"id": 3,
        "userid": 102,
        "name": "Stephy",
        "age": 32

    })
    assert response.status_code==200
    assert response.json() == "User updated Succefully"

def test_delete():
    response=client.delete("/users?id=4")
    assert response.status_code!=404
    assert response.json()["detail"] == "user not found"

   
 