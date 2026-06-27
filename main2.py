from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message":"welcome to my firstAPI!"}
@app.get("/students")
def get_students(course:str=None):
    students=[{"id":1,"name":"Avinash","course":"CSE"},
                {"id":2,"name":"NTR","course":"Law"},
                {"id":3,"name":"Mahesh","course":"Doctor"},
                {"id":4,"name":"Ravi Teja","course":"Cse"}]
    if course:
        filtered=[s for s in students if s["course"]==course]
        return{"students":filtered}
    return {"students":"error"}
