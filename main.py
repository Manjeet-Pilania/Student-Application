from email.mime import application
from typing import List
from xmlrpc.client import APPLICATION_ERROR
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# #  Helper function to get database session
def get_session():
      session = SessionLocal()
      try:
          yield session
      finally:
          session.close()

@app.get("/")
def student():
    return "student application"

@app.post("/students", response_model=schemas.students, status_code=status.HTTP_201_CREATED)
def create_(students: schemas.studentsCreate, session: Session = Depends(get_session)):

    # create an instance of the student database model
    studentdb = models.students(task = students.task)

    # add it to the session and commit it
    session.add(studentdb)
    session.commit()
    session.refresh(studentdb)

    # return the students object
    return studentdb

@app.get("/student/{id}", response_model=schemas.students)
def read_students(id: int, session: Session = Depends(get_session)):

    # get the students item with the given id
    students = session.query(models.students).get(id)

    # check if students item with given id exists. If not, raise exception and return 404 not found response
    if not students:
        raise HTTPException(status_code=404, detail=f"students item with id {id} not found")

    return students

@app.put("/students/{id}", response_model=schemas.students)
def update_students(id: int, task: str, session: Session = Depends(get_session)):

    # get the students item with the given id
    students = session.query(models.students).get(id)

    # update students item with the given task (if an item with the given id was found)
    if students:
        students.task = task
        session.commit()

    # check if students item with given id exists. If not, raise exception and return 404 not found response
    if not students:
        raise HTTPException(status_code=404, detail=f"students item with id {id} not found")

    return students

@app.delete("/students/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_students(id: int, session: Session = Depends(get_session)):

    # get the students item with the given id
    students = session.query(models.students).get(id)

    # if students item with given id exists, delete it from the database. Otherwise raise 404 error
    if students:
        session.delete(students)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"students item with id {id} not found")

    return None

@app.get("/student", response_model = List[schemas.students])
def read_students(session: Session = Depends(get_session)):

    # get all students items
      students = session.query(models.students).all()
      return students 
    