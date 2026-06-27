from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"message":"welcome to my firstAPI!"}
@app.get("/students")
def get_students():
    return{"student":[{"id":1,"name":"Avinash","course":"CSE"},
                    {"id":2,"name":"NTR","course":"Law"},
                    {"id":3,"name":"Mahesh","course":"Doctor"}]}
@app.get("/about")
def get_about():
    return{"api":"student API","version":"1.0","author":"Avinash"}
