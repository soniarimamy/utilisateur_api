from fastapi import FastAPI
app = FastAPI()
data = [{"id": 1, "name": "Rakoto", "age": 23}]
@app.get("/")
def get_users():
    return {"status": "success", "msg": "displayed", "data": data}
