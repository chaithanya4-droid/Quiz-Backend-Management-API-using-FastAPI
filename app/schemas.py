from pydantic import BaseModel


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool = False


class ChoiceCreate(ChoiceBase):
    question_id: int


class ChoiceUpdate(BaseModel):
    choice_text: str | None = None
    is_correct: bool | None = None


class ChoiceResponse(ChoiceBase):
    id: int
    question_id: int

    class Config:
        from_attributes = True


class QuestionBase(BaseModel):
    question_text: str
    category: str | None = None


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(BaseModel):
    question_text: str | None = None
    category: str | None = None


class QuestionResponse(QuestionBase):
    id: int
    choices: list[ChoiceResponse] = []

    class Config:
        from_attributes = True