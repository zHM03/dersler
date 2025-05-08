from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, bind = engine)
Base = declarative_base()

class TodoModel(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    Base.metadata.create_all(bind=engine)

class Todo(BaseModel):
    title: str

@app.post("/todos")
def create_todo(todo: Todo):
    db = SessionLocal()
    db_todo = TodoModel(title=todo.title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.get("/todos")
def read_todos():
    db = SessionLocal()
    return db.query(TodoModel).all()