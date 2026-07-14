from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quiz Backend Management API")

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/frontend")
def frontend():
    return FileResponse("app/static/index.html")


@app.get("/")
def root():
    return {"message": "Quiz Backend Management API is running"}


@app.post("/questions", response_model=schemas.QuestionResponse)
def create_question(
    question: schemas.QuestionCreate,
    db: Session = Depends(get_db)
):
    return crud.create_question(db, question)


@app.get("/questions", response_model=list[schemas.QuestionResponse])
def get_questions(db: Session = Depends(get_db)):
    return crud.get_questions(db)


@app.get("/questions/{question_id}", response_model=schemas.QuestionResponse)
def get_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = crud.get_question(db, question_id)

    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    return question


@app.put("/questions/{question_id}", response_model=schemas.QuestionResponse)
def update_question(
    question_id: int,
    question_update: schemas.QuestionUpdate,
    db: Session = Depends(get_db)
):
    question = crud.update_question(db, question_id, question_update)

    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    return question


@app.delete("/questions/{question_id}")
def delete_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = crud.delete_question(db, question_id)

    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    return {"message": "Question deleted successfully"}


@app.post("/choices", response_model=schemas.ChoiceResponse)
def create_choice(
    choice: schemas.ChoiceCreate,
    db: Session = Depends(get_db)
):
    question = crud.get_question(db, choice.question_id)

    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")

    return crud.create_choice(db, choice)


@app.get("/choices", response_model=list[schemas.ChoiceResponse])
def get_choices(db: Session = Depends(get_db)):
    return crud.get_choices(db)


@app.put("/choices/{choice_id}", response_model=schemas.ChoiceResponse)
def update_choice(
    choice_id: int,
    choice_update: schemas.ChoiceUpdate,
    db: Session = Depends(get_db)
):
    choice = crud.update_choice(db, choice_id, choice_update)

    if choice is None:
        raise HTTPException(status_code=404, detail="Choice not found")

    return choice


@app.delete("/choices/{choice_id}")
def delete_choice(
    choice_id: int,
    db: Session = Depends(get_db)
):
    choice = crud.delete_choice(db, choice_id)

    if choice is None:
        raise HTTPException(status_code=404, detail="Choice not found")

    return {"message": "Choice deleted successfully"}