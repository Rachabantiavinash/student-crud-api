import sqlite3
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
conn=sqlite3.connect("students.db",check_same_thread=False)
cursor=conn.cursor()
app=FastAPI()
'''cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY,
               name TEXT,
               course TEXT
)""")
conn.commit()
print("table created successfully")'''
#cursor.execute("""INSERT INTO students(id,name,course) VALUES(2,'MAHESH','CSE'),(3,'GOPI','ECE'),(4,'NTR','MECH')""")
#conn.commit()
#print("student added")
'''cursor.execute("SELECT * FROM students")
results=cursor.fetchall()
for i in results:
    print(i)'''
class Student(BaseModel):
    id:int
    name:str
    course:str
@app.get("/students")
def get_studentss():
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    students=[]
    for row in rows:
        students.append({"id":row[0],"name":row[1],"course":row[2]})
    return {"students":students}
@app.post("/students")
def add_studentss(student:Student):
    cursor.execute("INSERT INTO students VALUES(?,?,?)",(student.id,student.name,student.course))
    conn.commit()
    return {"message":"Student added","student":student}

@app.get("/students/{id}")
def get_student_withid(id:int):
    cursor.execute("SELECT * FROM students WHERE id=?",(id,))
    row=cursor.fetchone()
    if row:
        return{"row":{"id":row[0],"name":row[1],"course":row[2]},"roww":row}
    return {"error":"row not found"}
@app.put("/students/{id}")
def update_data(id:int,updated_student:Student):
    cursor.execute("UPDATE students SET name=?,course=?,id=? WHERE id=?",(updated_student.name,updated_student.course,updated_student.id,id))
    conn.commit()
    if cursor.rowcount==0:
        return {"error":"Student not found"}
    return {"message":"Student updated","student":updated_student}
@app.delete("/students/{id}")
def delete_student(id:int):
    cursor.execute("DELETE FROM students WHERE id=?",(id,))
    conn.commit()
    if cursor.rowcount==0:
        return{"errror":"Student not found"}
    return {"message":"Student deleted","id":id}