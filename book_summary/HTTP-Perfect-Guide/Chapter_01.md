## 1. HTTP 웹의 기초
---

### 웹 리소스

>웹에 콘텐츠를 제공하는 모든 것

웹 서버는 모든 HTTP 객체 데이터에 MIME(Mutltipurpose Internet Mail Extension) 타입을 설정한다.

### multipurpose internet mail extensions (MIME)
- 파일변환
- 웹을 통하여 여러 형태이 파일을 전달하는데 사용됨
- MIME 으로 encoding 을 하게 된다면 content-type 을 앞에 붙임
- HTTP 헤더에 보내지는 자원의 content-type 을 포함시킴
- MIME 으로 인코딩한 파일은 content-type 정보를 담게되며 content-type은 여러가지 타입이 있다.

---
### URI

Uniform Resource Identifier

- 자원의 식별자

>https://www.naver.com/special/download.gif


- 첫번째로 오는 https:// 가 scheme 이 되고,

- 두번째로 오는 www.naver.com 이 인터넷 서버의 주소,

- 마지막인 /special/download.gif 가 리소스

보다 정확한 설명은 CS_STUDY/URI_URL_URN 에 정리해 두었음

---

### 트랜잭션

HTTP Protocol을 통해서 요청 명령과 응답 결과로 이루어진 하나의 상호작용.

---
### TCP connection

보통 TCP를 기반으로 HTTP가 동작

최근엔 HTTP 1.0 은 거의 쓰이지 않으며 HTTP 2.0, QUIC 등으로 많이 대체되었다

---
### ETC
- proxy: client와 server 사이에 위치한 HTTP 중개자
- cache: 많이 찾는 웹페이지를 client 가까이에 보관하는 HTTP 저장소
- gateway: 다른 Application과 연결된 특별한 웹 서버
- Tunnel: 단순히 HTTP 통신을 전달하기만 하는 특별한 proxy
- Agent: 자동화된 HTTP 요청을 만드는 준지능적 웹 클라이언트
