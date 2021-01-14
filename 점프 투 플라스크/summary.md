## Jump to flask

- [Source](https://github.com/pahkey/flaskbook)


## Ch 01 - 플라스크 개발준비

- Python, Flask 설치 및 개발 환경 준비
- Flask Project 생성 및 프로그램 개발
- Flask Server 실행

### 마이크로 웹 프레임워크

- 프레임워크를 간결하게 유지하고 확장할 수 있음.
- (간결함) Flask 웹 프로그램 예시

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__=="__main__":
    app.run()
```

- (확장성) 필요 시 확장 모듈을 포함해가며 개발 진행

### 개발환경 구축

- 가상환경 생성

```bash
python -m venv venv
```

- 가상환경 활성화 (Gitbash)

```bash
source venv/Scripts/activate
```

- 가상환경 비활성화 (Gitbash)

```bash
deactivate
```

- pip 최신 버전 업데이트

```bash
python -m pip install --upgrade pip
```

- Flask 설치

```bash
pip install Flask
```

### Flask Project 생성

- Flask App 변수 선언 (Gitbash)
```bash
export FLASK_APP=pybo
```

- [Flask App](http://127.0.0.1:5000)

## Ch 02 - 플라스크 개발 기초 공사

- 블루프린트 이용 라우트 함수 관리
- 플라스크 ORM 이용 DB 제어
- 게시판 질문 목록 및 상세 조회 기능 개발

### 프로젝트 구조

```bash
├── pybo/
│      ├─ __init__.py
│      ├─ models.py
│      ├─ forms.py
│      ├─ views/
│      │   └─ main_views.py
│      ├─ static/
│      │   └─ style.css
│      └─ templates/
│            └─ index.html
└── config.py
```

- models.py: DB 처리
    - ORM(Object Relational Mapping) 지원하는 SQLAlchemy 사용
- forms.py: 서버로 전송된 폼 처리
    - WTForms 사용
- views: 화면을 구성하는 디렉터리
- static: CSS, JavaScript, Image Files 저장 디렉터리
- templates: HTML 파일 저장 디렉터리
- config.py: 프로젝트 설정 파일
    - 환경변수, DB 등 설정

### 플라스크 애플리케이션 팩토리

- app 객체를 전역으로 사용할 때 발생하는 문제를 예방할 때 사용
- app 객체를 생성하는 함수를 의미

- create_app() 함수

### 블루프린트 라우트 함수 관리

- 새로운 URL이 생길 때 라우트 함수를 create_app 함수 안에 계속 추가해야 하는 불편함 해결 위해 사용


### 모델로 데이터 처리하기

- 질문, 답변 작성 시 데이터 생성됨. 데이터를 저장하거나 조회하거나 수정하는 등의 기능을 구현해야 함. 웹 서비스는 데이터를 처리할 때 대부분 DB를 사용함.

### ORM(Object Relational Mapping)

- 데이터를 관리하는 데 사용하는 ORM 클래스를 모델이라고 함.

### Flask ORM 라이브러리

- SQLAlchemy
- Flask-Migrate
```bash
# 최초 1회 실행
flask db init
# 모델 새로 생성 혹은 변경 시
flask db migrate
# 모델 변경 내용 실제 DB적용 시
flask db upgrade
```

### 모델 생성

- 모델: 모델은 데이터를 다룰 목적으로 만든 파이썬 클래스
- 질문, 답변에 해당하는 모델 필요
- 질문 모델
  - id, subject, content, create_date
- 답변 모델
  - id, question_id, content, create_date

