

# HTTP

- HTTP(Hypertext Transfer Protocol)는 웹에서 쓰이는 통신 프로토콜. 
- 프로토콜이란 상호간에 정의한 규칙을 의미.


- HTTP 프로토콜은 TCP/IP 프로토콜 위의 레이어(Application layer)에서 동작합니다. 
- 각 프로토콜 별 layer 계층은 다음과 같이 간략히 표현됩니다.


![img](https://1.bp.blogspot.com/-YGgmbhSy1W8/XWodfUw_80I/AAAAAAAABrY/iynG65dE74ADmbEfuFAElE9KaSkG-Gd2ACLcBGAs/s1600/%25EC%25BA%25A1%25EC%25B2%2598.JPG)

## stateless
- 데이터를 주고 받기 위한 각각의 데이터 요청이 서로 독립적으로 관리
- 이전 데이터 요청과 다음 데이터 요청이 서로 관련이 없다


## HTTP Method
HTTP 요청 메소드는 4개.

- Get: 존재하는 자원에 대한 요청
- POST: 새로운 자원을 생성
- PUT: 존재하는 자원에대한 변경
- DELETE: 존재하는 자원에 대한 삭제


## HTTP 동작

- 클라이언트에서 서버로 요청을 보냄, 이 요청은 HTTP 메시지 형식을 따름
- 서버는 클라이언트 요청에 대한 응답을 생성, HTTP 메시지 형식을 따르도록 함
- 서버는 생성된 응답을 클라이언트로 보냄.
- 클라이언트는 서버에서 받은 응답을 처리하고, 필요한 경우 추가 요청을 보냄.


## HTTP 1.1
- pieplining 이라고도 부른다

![img](https://user-images.githubusercontent.com/31475037/89241056-d77c9480-d638-11ea-8ef4-7d9d475ac560.png)

### 단점
-  기본적으로 연결당 하나의 Request과 Response를 처리하기 때문에 동시전송 문제와 다수의 리소스를 처리하기에 속도 및 성능 이슈 있음

- HOLB(Head Of Line Blocking) 특정 응답 지연
  - 첫번째 이미지에 대한 Response가 지연되면 두, 세번째 이미지는 첫번째 이미지의 응답처리가 완료되기 전까지 대기

- RTT (Round Trip Time)증가
  - 하나의 connection 하나의 request 이므로 매 connection 마다 tcp 연결 -> 매번 (시작시) threeway handshake, 종료시 (4-way handshake)

- heavy header
  - 매 request 마다 중복된 header,
  - cookie

## HTTP2.0

HTTP2.0은 HTTP1.1의 프로토콜을 계승해 동일한 API면서 성능 향상에 초점

- Multiplexed Streams
  - 한 connection으로 동시에 여러개 메시지를 주고 받을 수 있으며, Response는 순서에 상관없이 stream으로 주고받음

- Stream Prioritization
  - 리소스간 우선순위를 설정해 클라이언트가 먼저 필요한 리소스

- Server Push
  - 서버는 클라이언트의 요청에대해 요청하지 않은 리소스를 마음대로 보내줄 수 있다

- Header Compression
  - http1.1 에서 문제가 되었던 heavy header 를 Header table과 Huffman Encoding 기법(HPACK 압축방식)을 이용해 압축






ref: 
- https://chacha95.github.io/2020-06-15-gRPC1/
- https://goddaehee.tistory.com/169
- https://developer.mozilla.org/ko/docs/Web/HTTP/Overview