from fastapi import FastAPI,Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal,engine,Base
from models import StudentDB
Base.metadata.create_all(bind=engine)
app=FastAPI()
class Student(BaseModel):
    id:int
    name:str
    course:str
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/students")
def get_students(db:Session=Depends(get_db)):
    students=db.query(StudentDB).all()
    return {"students":students}
@app.get("/students/{id}")
def get_one_student(id:int,db:Session=Depends(get_db)):
    student=db.query(StudentDB).filter(StudentDB.id==id).first()
    if student:
        return student
    return {"error":"Student not found"}
@app.post("/students")
def add_student(student:Student,db:Session=Depends(get_db)):
    db_student=StudentDB(id=student.id,name=student.name,course=student.course)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"message":"Student added","student":db_student}
@app.put("/students/{id}")
def update_student(id:int,updated_student:Student,db:Session=Depends(get_db)):
    student=db.query(StudentDB).filter(StudentDB.id==id).first()
    if not student:
        return {"return":"Student not found"}
    student.name=updated_student.name
    student.course=updated_student.course
    db.commit()
    db.refresh(student)
    return {"message":"Student updated","student":student}
@app.delete("/students/{id}")
def delete_student(id:int,db:Session=Depends(get_db)):
    student=db.query(StudentDB).filter(StudentDB.id==id).first()
    if not student:
        return {"error":"Student not found"}
    db.delete(student)
    db.commit()
    return {"message":"Student deleted","id":id}