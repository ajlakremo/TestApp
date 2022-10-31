from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_answer_question():
    response = client.post("/api/answer", json={"question_id": 0, "answer": "20-04-1997"})
    assert response.status_code == 200
    assert response.json() == {"question": {"id": 0, "content": "When were you born?"}, "answer": "20-04-1997"}


def test_answer_inexistent_question():
    response = client.post("/api/answer", json={"question_id": 1000, "answer": "Test Answer"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Question does not exist!"}


def test_answer_incorrect_date_format():
    response = client.post("/api/answer", json={"question_id": 0, "answer": "1997-04-20"})
    assert response.status_code == 418
    assert response.json() == {"detail": "Incorrect date format, should be DD-MM-YYYY."}

