## Pre-Requisite
- CS_STUDY/stdin.md

---


## CGI

- 사용자가 정적인 페이지 index.html 을 요청한다면 그대로 반환하면 된다
- 만약 요청이 동적인경우?

- 서버로 들어온 요청을 웹 앱으로 넘겨줄 수 있어야함
- 서버마다, 앱마다 다른 형태를 가진다면 매우 번거로움
- '가능한 공통의 표준 인터페이스'
- Common Gateway Interface 이다

---
## WSGI

- Web Server Gateway Interface
- 파이썬에서 사용되는 개념
- CGI 의 단점을 개선한다
  - 요청이 들어올 때마다 새로운 프로세스 생성
  - CGI 는 STDIN 으로 처리하나 WSGI 는 Callableobject, 함수, 객체로 처리한다
- 서버 -> callable object -> 정보, callback 함수 전달 -> 애플리케이션 요청 처리, 함수 실행


### WSGI Middleware
- 중간에서 인증, 쿠키 관리 역할
- WSGI application 의 일종
- gunicorn 이 포함

---
## ASGI

- WSGI 개선
  - 비동기적 요청 처리 단점
  - 길게 유지되어야 하는 연결 (long-poll HTTP, 웹소켓) 과 맞지 않음
- WSGI 에 대한 호환성을 가지면서 비동기적인 요청을 처리할 수 있는 인터페이스
- Uvicorn

---
ref:
- https://kangbk0120.github.io/articles/2022-02/cgi-wcgi-asgi