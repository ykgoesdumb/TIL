# 3. HTTP 메세지

## http 메세지란

- http 애플리캐이션 간에 주고 받는 데이터 블록

---

## 메세지의 흐름

### inbound -> outbound

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FzpDtF%2FbtrsY8vODnF%2FE3skgCgAMBITrExBNan9RK%2Fimg.png)

---

## 메세지의 각 부분

HTTP 메세지는 부분적으로 나뉘어져 있다
- 시작줄 : HTTP Protocol과 status를 명시
- 헤더 : 본문의 conten 종류와 길이
- 본문 : 내용

```
HTTP/1.0 200 OK // 시작줄
---------------------------
Content-type: text/plain // 헤더
Content-length: 10
---------------------------
Hi I'm a message! // 본문

```
---

## 메서드


<br>
|메서드| 설명|	메세지 본문이 있는가?|
|---|---|---|
|GET|서버에서 어떤 문서를 가져온다|	없음|
|HEAD|서버에서 어떤 문서에 대한 헤더만 가져온다|없음
|POST|서버가 처리해야 할 데이터를 보낸다|있음
|PUT|서버에 요청 메세지의 본문을 저장한다|있음
|TRACE|	메세지가 프락시를 거쳐 서버에 도달하는 과정을 추적한다|	없음
|OPTIONS|서버가 어떤 메서드를 수행할 수 있는지 확인한다	|없음
|DELETE|서버에서 문서를 제거한다|없음

  
- 안전한 메서드
  - GET
    - 서버에서 리소스를 요청하기 위한 메서드
  - HEAD
    - GET 처럼 행동하나 헤더만 반환한다


- 그외
  - PUT
    - 요청 URL 대로 새문서를 만들거나 기존의 문서를 교체
  - POST
    - 클라이언트가 서버에 입력 데이터 전송
  - TRACE
    - 진단을 위해 사용, 요청이 어떤 연쇄 요청/응답을 거쳐갔는지 파악
  - OPTIONS
    - 어떤 요청 메서드가 있는지 서버에게 질문하는 용도
  - DELETE
    - 서버에게 요청 URL 을 삭제 요청 , *삭제가 수행되는것을 보장하지는 못함*
  - 확장메서드
    - 엄격하게 보내고, 관대하게 받아들임

---
## 상태코드

- 메서드는 서버에게 무엇을 하라고 말해주는 것
- 상태코드는 서버가 클라이언트에게 무엇이 일어났는지 알려준다






