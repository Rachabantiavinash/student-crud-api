from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
students=[{"id":1,"name":"Avinash","course":"CSE"},
                {"id":2,"name":"NTR","course":"Law"},
                {"id":3,"name":"Mahesh","course":"Doctor"},
                {"id":4,"name":"Ravi Teja","course":"Cse"}]
class Student(BaseModel):
    id:int
    name:str
    course:str
@app.get("/")
def home():
    return{"message":"welcome to my firstAPI!"}
@app.get("/students")
def get_students():
    return students
@app.post("/students")
def add_student(student:Student):
    students.append(student.model_dump())
    return students
@app.put("/students/{id}")
def update_student(id:int,updated_student:Student):
    for student in students:
        if student["id"]==id:
            student["name"]=updated_student.name
            student["course"]=updated_student.course
            return student
    return {"error":"something error happend"}
@app.delete("/students/{id}")
def delete_student(id:int):
    for student in students:
        if student["id"]==id:
            students.remove(student)
            return {"student removed":id}
    return "student id not found"