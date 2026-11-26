from fastapi import FastAPI,HTTPException
app=FastAPI()
@app.get("/divide")
def div(a:int,b:int):
    if b==0:
        raise HTTPException(status_code=400,detail="Division by Zero restricted")
    return a/b