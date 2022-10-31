from pydantic import BaseModel

QUESTIONS = [{'id': 0, 'content': "When were you born?"}, {'id': 1, 'content': "How much do you weigh?"},
             {'id': 2, 'content': "How often do you dye your hair?"}]
USER_ANSWERS = []


class Question(BaseModel):
    id: int
    content: str


class UserAnswer(BaseModel):
    question: Question
    answer: str


class UserAnswerIn(BaseModel):
    question_id: int
    answer: str

    class Config:
        schema_extra = {
            "example": {
                "question_id": 0,
                "answer": "20-04-1997",
            }
        }
