from sqlalchemy.orm import Session

from app import models, schemas


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(**question.model_dump())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def get_questions(db: Session):
    return db.query(models.Question).all()


def get_question(db: Session, question_id: int):
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def update_question(
    db: Session,
    question_id: int,
    question_update: schemas.QuestionUpdate
):
    db_question = get_question(db, question_id)

    if db_question is None:
        return None

    update_data = question_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_question, key, value)

    db.commit()
    db.refresh(db_question)
    return db_question


def delete_question(db: Session, question_id: int):
    db_question = get_question(db, question_id)

    if db_question is None:
        return None

    db.delete(db_question)
    db.commit()
    return db_question


def create_choice(db: Session, choice: schemas.ChoiceCreate):
    db_choice = models.Choice(**choice.model_dump())
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice


def get_choices(db: Session):
    return db.query(models.Choice).all()


def get_choice(db: Session, choice_id: int):
    return db.query(models.Choice).filter(models.Choice.id == choice_id).first()


def update_choice(
    db: Session,
    choice_id: int,
    choice_update: schemas.ChoiceUpdate
):
    db_choice = get_choice(db, choice_id)

    if db_choice is None:
        return None

    update_data = choice_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_choice, key, value)

    db.commit()
    db.refresh(db_choice)
    return db_choice


def delete_choice(db: Session, choice_id: int):
    db_choice = get_choice(db, choice_id)

    if db_choice is None:
        return None

    db.delete(db_choice)
    db.commit()
    return db_choice