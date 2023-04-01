# HTTP 기본

## 모든 것이 HTTP
- 클라이언트 서버 구조
- Stateful, Stateless
- 비 연결성(connectionless)
- HTTP 메시지

## Hyper Text Transfer Protocol
>하이퍼 텍스트 기반 프로토콜이였으나 현대사회에선 사용처가 매우매우 확장됨
HTTP 메시지에 모든 것을 전송
- HTML, TEXT
- IMAGE, 음성, 영상, 파일
- JSON, XML (API)
- 거의 모든 형태의 데이터 전송 가능
- 서버간에 데이터를 주고 받을 때도 대부분 HTTP 사용


## HTTP 역사

> 사실상 1.1 이 전세계적으로 제일 많이 쓰임 (강의 내용도 1.1 중심임)

- HTTP/0.9 1991년: GET 메서드만 지원, HTTP 헤더X
- HTTP/1.0 1996년: 메서드, 헤더 추가
- HTTP/1.1 1997년: 가장 많이 사용, 우리에게 가장 중요한 버전
- RFC2068 (1997) -> RFC2616 (1999) -> RFC7230~7235 (2014)
- HTTP/2 2015년: 성능 개선
- HTTP/3 진행중: TCP 대신에 UDP 사용, 성능 개선


## 기반 프로토콜

- TCP: HTTP/1.1, HTTP/2
- UDP: HTTP/3
- 현재 HTTP/1.1 주로 사용
  - HTTP/2, HTTP/3 도 점점 증가

- 개발자 도구에서 network tap 에서 모든 URI 의 프로토콜을 볼 수 있음


## 클라이언트 서버 구조
- request response 구조
- 클라이언트는 서버에 요청을 보내고 응답을 대기
- 서버가 요청에 대한 결과를 만들어서 응답
- 양측이 독립됨으로써 개별적 진화가 가능함

---

## STATEFUL, STATELESS

> HTTP 는 STATELESS 를 지향한다

- 서버가 클라이언트의 상태를 보존X
- 장점: 서버 확장성 높음(스케일 아웃)
- 단점: 클라이언트가 추가 데이터 전송


### Stateful, Stateless 차이

> 강좌에선 차이점을 설명하기위해 고객(client) 점원(server) 로 예시를 들었다.

stateful 은 
- 상태 유지: 중간에 다른 서버(점원)으로 바뀌면 안된다.
(중간에 다른 서버(점원)으로 바뀔 때 상태 정보를 다른 점원에게 미리 알려줘야 한다.)
- 중간의 서버가 장애가 난다면?
  - 처음부터 다른서버로 다시 request 해야함

stateless 는 
- 무상태: 중간에 다른 점원으로 바뀌어도 된다. (점원이 바뀌어도 context 를 다 담아서 클라이언트가 요청하기때문)
- 갑자기 고객이 증가해도 점원을 대거 투입할 수 있다.
- 갑자기 클라이언트 요청이 증가해도 서버를 대거 투입할 수 있다 (클라이언트가 추가 데이터를 전송하기 때문)
- 무상태는 응답 서버를 쉽게 바꿀 수 있다. -> 무한한 서버 증설 가능 (scale-out)


## Stateless 의 실무 한계

- 모든 것을 무상태로 설계 할 수 있는 경우도 있고 없는 경우도 있다.
- 무상태
  - 예) 로그인이 필요 없는 단순한 서비스 소개 화면
- 상태 유지
  - 예) 로그인
- 로그인한 사용자의 경우 로그인 했다는 상태를 서버에 유지 (stateful 하게 작동해야함)
- 일반적으로 브라우저 쿠키와 서버 세션등을 사용해서 상태 유지
- 상태 유지는 최소한만 사용
- 데이터를 너무 많이 보내야한다

---

## connectionless

![img src](https://user-images.githubusercontent.com/49462767/228104512-1f16c76a-9784-4d40-9a1e-69507882ad68.png)


- 연결을 유지하는 모델의 단점은 명확하다
  - 클라이언트가 놀고있어도 연결을 유지하기위해 서버자원을 소모한다 


비 연결성
- HTTP는 기본이 연결을 유지하지 않는 모델
- 일반적으로 초 단위의 이하의 빠른 속도로 응답
- 1시간 동안 수천명이 서비스를 사용해도 실제 서버에서 동시에 처리하는 요청은 수십개 이하로 매우 작음
  - 예) 웹 브라우저에서 계속 연속해서 검색 버튼을 누르지는 않는다.
- 서버 자원을 매우 효율적으로 사용할 수 있음
  - 최소한의 자원을 사용, 서버 연결 유지 하지 않음


비 연결성의 한계와 극복

- TCP/IP 연결을 새로 맺어야 함 - 3 way handshake 시간 추가
- 웹 브라우저로 사이트를 요청하면 HTML 뿐만 아니라 자바스크립트, css, 추가 이미지 등등 수 많은 자원이 함께 다운로드

- 초기의 HTTP 는 연결->응답->종료 를 계속 반복하였음
  - 연결, html 요청-> 응답, 종료 / 연결, js 요청 -> 응답, 종료 / 연결, 이미지 요청 -> 응답, 종료/ ....
- 지금은 HTTP 지속 연결(Persistent Connections)로 문제 해결
  - HTML 자바스크립트 이미지 등등 페이지 안에있는 혹은 일정부분의 요청에대한 응답이 다 완료할때 까지 연결을 유지
- HTTP/2, HTTP/3에서 더 많은 최적화


### 스테이스리스를 기억하자
서버 개발자들이 어려워하는 업무
- 정말 같은 시간에 딱 맞추어 발생하는 대용량 트래픽
- 예) 선착순 이벤트, 명절 KTX 예약, 학과 수업 등록
- 예) 저녁 6:00 선착순 1000명 치킨 할인 이벤트 -> 수만명 동시 요청

---

## HTTP 메시지

HTTP 메시지에 모든 것을 전송
- HTML, TEXT
- IMAGE, 음성, 영상, 파일
- JSON, XML
- 거의 모든 형태의 데이터 전송 가능
- 서버간에 데이터를 주고 받을 때도 대부분 HTTP 사용


## HTTP 메세지 구조

<img width="500" src="https://user-images.githubusercontent.com/49462767/228118271-495db256-818c-434f-8588-655068ac4972.png">

- 시작라인
- 헤더
- 공백라인
- 메세지 본문 (요청메세지에도 있을 수 있음!)


## 시작라인
### 요청메세지 의 시작라인
- start-line(시작라인) = request-line 

<img width="263" src="https://user-images.githubusercontent.com/49462767/228117431-a585beae-d1a1-4307-a1f7-ec1e86cac452.png">

  
- request-line = method request-target HTTP-version CRLF(엔터)
  - 위와 같은 형식으로 되어있음
  - HTTP 메서드 (GET: 조회)
  - 요청 대상 (/search?q=hello&hl=ko)
  - HTTP Version

### 요청 메시지 - HTTP 메서드
<img width="280" src="https://user-images.githubusercontent.com/49462767/228116276-10b9b7f6-ff20-4f20-bd08-c150b8eed1f6.png">

- 종류: GET, POST, PUT, DELETE...
- 서버가 수행해야 할 동작 지정
- GET: 리소스 조회
- POST: 요청 내역 처리

### 요청 메세지 - 요청 대상

<img width="308" src="https://user-images.githubusercontent.com/49462767/228118765-2c0340c3-435d-4b4d-8ed1-fefd215cef58.png">

- absolute-path[?query] (절대경로[?쿼리])
- 절대경로= "/" 로 시작하는 경로
- 참고: *, http://...?x=y 와 같이 다른 유형의 경로지정 방법도 있다.


### 요청메세지 - HTTP 버전

- 요청대상 뒤에 버전 명시



### 응답메세지의 시작라인
- start-line = status-line
  - status-line = HTTP-version  status-code  reason-phrase CRLF



- HTTP 버전
- HTTP 상태 코드: 요청 성공, 실패를 나타냄
  - 200: 성공
  - 400: 클라이언트 요청 오류
  - 500: 서버 내부 오류
- 이유 문구(reason phrase): 사람이 이해할 수 있는 짧은 상태 코드 설명 글

---

## HTTP 헤더
- header-field = field-name: 내용 (OWS optional white space : 띄어쓰기 허용)
- field-name 은 대소문자 구분없음

- 요청 http 헤더 예시
  - Host: www.google.com
- 응답 http 헤더 예시
  - Content-type: text/html;charset=UTF-8

## HTTP 헤더의 용도

- HTTP 전송에 필요한 모든 부가정보(메타데이터)
  - 메세지 바디를 제외한 필요한 모든 메타데이터가 다 들어있다
  - 예) 메시지 바디의 내용, 메시지 바디의 크기, 압축, 인증, 요청 클라이언트(브라우저) 정보,

서버 애플리케이션 정보, 캐시 관리 정보...
- 표준 헤더가 너무 많음
  - https://en.wikipedia.org/wiki/List_of_HTTP_header_fields
- 필요시 임의의 헤더 추가 가능
  - helloworld: hihi


## HTTP 메시지 바디
- 실제 전송할 데이터
- HTML 문서, 이미지, 영상, JSON 등등 byte로 표현할 수 있는 모든 데이터 전송 가능

## HTTP는 단순하며 확장 가능하다
- HTTP 메세지도 매우 단순
- 단순하지만 확장가능한 기술이 표준이 되었음

