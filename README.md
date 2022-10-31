# TestApp

## Live

https://fast-api-testapp.herokuapp.com/docs

## Getting Started

#### 1. Clone the git repo:
```
git clone https://github.com/ajlakremo/TestApp.git
```

#### 2. Download and install Python
To download python - [link](https://www.python.org/downloads/).

#### 3. Create a python virtual envrionment:
To create a virtual env - [link](https://docs.python.org/3.9/library/venv.html).

#### 4. Install the required packages
```
pip install requirement.txt
```
#### 5. Executing program

To start the API use the following command:
````
uvicorn main:app --reload
````
This should start a server listening on http://127.0.0.1:8000

After starting the server you can visit (API Docs):
http://127.0.0.1:8000/docs

This projects contains unit tests. To execute the tests, use the following command:
````
pytest
````

Also, this project contains a [Postman Collection](https://www.getpostman.com/collections/26311428e192e0af4a62)
