## REST API 의 구성


- 자원(resource) -> URI
- 행위(verb) -> HTTP Method
- 표현(Representations)


## REST 의 특징

- Uniform
  - uniform interface 는 URI 로 지정된 리소스를 통일, 한정적 인터페이스로 수행하는 아키택처 스타일
- Stateless
  - 무상태성, 세션 정보나 쿠키정보를 별도로 저장 관리하지 않음 -> 구현의 단순화
- Cacheable
  - HTTP 가 가진 캐싱 기능이 적용 가능
  - last-modified, E-tag
- Self-descriptiveness (자체 표현 구조)
  - REST API 메시지만 보고 이해가 가능한 구조
- Client-Server
  - 서버는 api 제공
  - 클라이언트는 사용자 인증이나 컨텍스트 직접관리
  - 서로간 의존성 줄어듬
- 계층형 구조
  - 서버는 다중 계층 구성 가능 (보안, 로드밸런싱, 암호화, proxy, gateway)
  

## REST API 설계의 핵심
1. URI는 정보의 자원을 표현해야한다
2. 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다


```shell
##URI 예시
    GET /members/show/1     (x)
    GET /members/1          (o)
```

- post  -> 리소스 생성
- get   -> 리소스 조회
- put   -> 리소스 수정
- delete -> 리소스 삭제

## URI 설계시 주의할 점
- resource 는 최대한 명사로 


- 슬래시 구분자 (/)
  - 마지막 에는 슬래시 사용하지 않음




ref: https://meetup.nhncloud.com/posts/92

