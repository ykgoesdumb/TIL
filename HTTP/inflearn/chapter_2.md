# URI 와 웹 브라우저 요청 흐름

## URI URL URN

>"URI는 로케이터(locator), 이름(name) 또는 둘 다 추가로 분류될 수 있다

- 사실상 거의 URL 만 쓴다
- URN 은 이름같이 부여됨 Mapping 이 힘들다

![img src](https://user-images.githubusercontent.com/49462767/227964907-a34bfb87-ca44-4d83-a49f-6712a5c81fd7.png)

URI
- Uniform: 리소스 식별하는 통일된 방식
- Resource: 자원, URI로 식별할 수 있는 모든 것(제한 없음)
- Identifier: 다른 항목과 구분하는데 필요한 정보


URL, URN
- URL - Locator: 리소스가 있는 위치를 지정
- URN - Name: 리소스에 이름을 부여
  - 위치는 변할 수 있지만, 이름은 변하지 않는다 (mapping 이 힘들다)
  - urn:isbn:8960777331 (어떤 책의 isbn URN)
  - URN 이름만으로 실제 리소스를 찾을 수 있는 방법이 보편화 되지 않음

- URI 와 URL 은 거의 같은의미로 해석됨 (그만큼 URN 이 쓰이지 않음)


---
## URL 문법

- scheme://[userinfo@]host[:port][/path][?query][#fragment]
- https://www.google.com:443/search?q=hello&hl=ko
<br></br>
- 프로토콜(https)
- 호스트명(www.google.com)
- 포트 번호(443)
- 패스(/search)
- 쿼리 파라미터(q=hello&hl=ko)

### Scheme

- scheme://[userinfo@]host[:port][/path][?query][#fragment]
- https://www.google.com:443/search?q=hello&hl=ko
- 주로 프로토콜 사용
- 프로토콜: 어떤 방식으로 자원에 접근할 것인가 하는 약속 규칙
  - 예) http, https, ftp 등등
- http는 80 포트, https는 443 포트를 주로 사용, 포트는 생략 가능
- https는 http에 보안 추가 (HTTP Secure)
  - 대부분의 웹사이트들이 HTTPs 로 동작


### userinfo
- scheme://[userinfo@]host[:port][/path][?query][#fragment]
- https://www.google.com:443/search?q=hello&hl=ko
- URL에 사용자정보를 포함해서 인증
- 웹상에서 거의 사용하지 않음
  - jdbc, sqlalchemy 주소 등 에서는 명시한다

### host
- scheme://[userinfo@]host[:port][/path][?query][#fragment]
- https://www.google.com:443/search?q=hello&hl=ko
- 호스트명
- 도메인명 또는 IP 주소를 직접 사용가능


### PORT
- scheme://[userinfo@]host[:port][/path][?query][#fragment]
- https://www.google.com:443/search?q=hello&hl=ko
- 포트(PORT)
- 접속 포트
- 일반적으로 생략, 생략시 http는 80, https는 443

### path
- scheme://[userinfo@]host[:port][/path][?query][#fragment]
- https://www.google.com:443/search?q=hello&hl=ko
- 리소스 경로(path), 계층적 구조
- 예)
  - /home/file1.jpg
  - /members
  - /members/100, /items/iphone12

### query
- scheme://[userinfo@]host[:port][/path][?query][#fragment]
- https://www.google.com:443/search?q=hello&hl=ko
- key=value 형태
- ?로 시작, &로 추가 가능 ?keyA=valueA&keyB=valueB
- query parameter, query string 등으로 불림, 웹서버에 제공하는 파라미터, 문자 형태

## fragment
- scheme://[userinfo@]host[:port][/path][?query][#fragment]
- https://docs.spring.io/spring-boot/docs/current/reference/html/gettingstarted.html#getting-started-introducing-spring-boot
- fragment
- html 내부 북마크 등에 사용
  - 문서의 몇번째 row 등을 지정할 수 있음
- 서버에 전송하는 정보 아님

---
## 웹 브라우저 요청 흐름

- http 메세지 전송한다 
![img src](https://user-images.githubusercontent.com/49462767/227976491-e702f17e-59d5-4986-8a80-f95771c7b9b1.png)

- http version 도 들어가있음

### HTTP 메시지 전송 과정

![img src](https://user-images.githubusercontent.com/49462767/227996731-a109a6b4-8ef7-4ff7-b700-f7e05d5590e2.png)
- socket library 를 거칠때 three way handshake 
- 데이터 전달

<br></br>
- 이렇게 보낸 요청 패킷이 서버에 도달하면
- tcp ip 패킷을 깜 -> 안에 메세지 확인
- 서버에서 http 응답 패킷 안에 응답 메시지를 감싸서 클라이언트로 보냄
  - 응답 메세지 안에 
    - http 버전
    - 상태
    - content-type, content-length ....


![img src](https://user-images.githubusercontent.com/49462767/227997288-e0e787d8-5b21-4fa9-992c-915b6d2dd53b.png)

<br></br>

- 받은 후에 웹 브라우저가 HTML 렌더링
- 렌더링 된 결과가 우리가 구글 검색탭 쳤을때 보는 화면
