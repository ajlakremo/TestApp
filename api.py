from datetime import datetime, date
from typing import List

from fastapi import HTTPException, APIRouter

from schemas import USER_ANSWERS, QUESTIONS, UserAnswerIn, UserAnswer, Question

router = APIRouter(
    prefix="/api",
    tags=["api"]
)


@router.get("/question", status_code=200, response_model=Question)
async def get_question():
    question = QUESTIONS[0]

    user_answers = [answer for answer in USER_ANSWERS if answer.question.id == 0]
    if user_answers and user_answers[0]:
        answer = datetime.strptime(user_answers[0].answer, "%d-%m-%Y")
        age = date.today().year - answer.year

        if age > 35:
            question = QUESTIONS[1]
        else:
            question = QUESTIONS[2]
    return question


@router.get("/questions", status_code=200, response_model=List[Question])
async def get_questions():
    return QUESTIONS


@router.get("/user/answers", status_code=200, response_model=List[UserAnswer])
async def get_user_answers():
    return USER_ANSWERS


@router.post("/answer", status_code=200, response_model=UserAnswer)
async def answer_question(*, user_answer_in: UserAnswerIn):
    if user_answer_in.question_id == 0:
        # validation done only for the first question
        try:
            datetime.strptime(user_answer_in.answer, "%d-%m-%Y")
        except ValueError:
            raise HTTPException(status_code=418, detail="Incorrect date format, should be DD-MM-YYYY.")

    question = [q for q in QUESTIONS if q.get('id', None) == user_answer_in.question_id]

    if not question:
        raise HTTPException(status_code=404, detail="Question does not exist!")

    question = question[0]
    user_answer = UserAnswer(question=Question(**question),
                             answer=user_answer_in.answer)

    idx = next((i for i, x in enumerate(USER_ANSWERS) if x.question.id == question.get('id', None)), -1)
    if idx != -1:
        USER_ANSWERS[idx] = user_answer
    else:
        USER_ANSWERS.append(user_answer)
    return user_answer

