
HTTP 요청 대상을 resource 라고 한다
- 문서, 사진 등 어떤것 가능
- HTTP 전체에서 사용되는 URI 로 식별됨


## URI
- uniform resrouce identifier
- 인터넷 자언을 나타내는 고유 식별자

URI 는 다음과 같은 구성을 포함한 구문을 따른다

1. 스키마 or 프로토콜
2. 도메인 이름
3. 포트
4. 경로
5. 쿼리
6. 프래그먼트(Fragment)



### 1. 스키마 혹은 프로토콜

```
http://
```

http 는 브라우저가 사용해야 하는 프로토콜이다


브라우저는 http, https 뿐만 아니라 메일과 파일 전송을 다른 프로토콜 처리 방법도 알고 있다



|스키마	|설명 |
|---|---|
data |Data URL|
file|호스트별 파일 이름
ftp	|File Transfer Protocol
http/https|	하이퍼 텍스트 전송 프로토콜 (보안)
javascript|	URL내 JavaScript 코드
mailto|	전자 메일 주소
ssh	|보안 쉘
tel	|전화
urn	|통합 자원 이름
view-source|리소스의 소스코드
ws/wss|	웹 소켓 연결 (보안)

---
사실상 URL URN 은 URI 의 하위개념이며
- URL 은 자원의 Location
- URN 은 자원의 Name 이다



### 2. 도메인 이름

```
www.google.com
```
요청중인 웹 서버를 나타냄
- IP 주소를 직접사용도 가능하나 편의성 떨어져 웹에선 도메인 사용함


### 3. 포트

```
:80
```

웹 서버의 리소스에 액세스하는데 사용되는 기술적인 "게이트"
- http 표준 :80
- https 표준 :443

### 4. 경로

```
/path/to/myfile.html
```
웹 서버의 리소스 경로
- 요즘에는 물리적 파일을 나타낸느것이 아닌 웹서버에서 처리 요청

### 5. 쿼리
```
?key1=value1&key2=value2
```
웹 서버에 제공되는 & 로 구분된 key,value 쌍 목록

### 6. 프래그먼트

```
#SomewhereInTheDocument
```

리소스 자체의 "북마크"

- HTML 문서에서 앵커가 정의된 지점으로 스크롤 (github 의 883 번째 줄)
- 식별자 '#' 요청과 함께 서버로 전송되지 않음



<br></br>



![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAkL2o%2FbtqJptEQJmu%2FomyDDiWIRr99BFKeVIpTt0%2Fimg.png)

## URL
- uniformed resource locator

```
https://developer.mozilla.org

https://developer.mozilla.org/en-US/docs/Learn/

https://developer.mozilla.org/en-US/search?q=URL

http://www.example.com:80/path/to/myfile.html?key1=value1&    key2=value2#SomewhereInTheDocument
```


## URN
- uniformed resource name

특정 namespace 에서 이름으로 resource 를 식별하는 URI

```
urn:isbn:9780141036144
urn:ietf:rfc:7230
```




참조링크:
- https://programming119.tistory.com/194
- https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/Identifying_resources_on_the_Web