from fastapi import FastAPI,Response,HTTPException
from pydantic import BaseModel,Field,ConfigDict
app=FastAPI()
class Users(BaseModel):
    model_config=ConfigDict(extra="ignore")
    id:int=Field(le=10)
    userid:int
    name:str=Field(min_length=3)
    age:int | None=None

users=[]
@app.get("/users")
def disp_user(response:Response):
   if len(users)==0:
     response.status_code=204
     return None
   return users

@app.post("/users",status_code=201)
def add_user(user:list[Users]):
    for u in user:
        users.append(u)
    return user

@app.get("/users/{id}",response_model=Users)
def respond_user(id:int):
    for user in users:
            if id ==user.id:
                return user
    raise HTTPException(status_code=404,detail="user not found")

@app.put("/users")
def update_user(id:int, user:Users):
    for i in range(len(users)):
        if users[i].id==id:
           users[i]=user 
           return "User updated Succefully"
    raise HTTPException(status_code=404,detail="user not found")

@app.delete("/users")
def delete_user(id:int):
    for user in users:
            if id==user.id:
               users.remove(user)
               return "User deleted successfully"
    raise HTTPException(status_code=404,detail="user not found")

@app.get("/")
def greet():
    return "....FASTAPI...."