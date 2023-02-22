## connection pool

application 과 db 와의 connection 을 맺을 때는 많은 communication 이 발생한다

- DB 통신 은 TCP 기반이기 때문에 3-way handshaking 발생
- 쿼리 하나당 packet 개수 굉장히 많음
- SSL 이적용 되어 있는 경우 프로세스가 더 많음


## why connection pooler
- login 하는 절차가 사라짐 
- connection 을 connection pooler 가 가지고 있기 때문
- db 는 상당히 중요한 서버기때문에 connection pooler 가 중간에서 트래픽을 막아줌


## Pgbouncer 란?

> Lightweight connection pooler for PostgreSQL

![img](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*zQyR1pXCCgtHjHlSm3NGkQ.png)


명칭 자체가 굉장히 직관적이다
- client side : CL_LOGIN, CL_WAITING_LOGIN, CL_ACTIVE, CL_WAITING
    - client 의 요청이 쌓이는곳
    - db 와 직접적으로 connection 을 맺는곳은 아니고 일종의 queue
- server side : SV_ACTIVE, SV_IDLE, SV_USED, SV_LOGIN, SV_TEST
  - client 의 요청을 받아 DB 에 접속하는 파트
  - db 의 active session 들이 server side status 와 동일하게 움직임

## process 의 상태

client side

- CL_LOGIN : Client가 login 시도하는 상태
- CL_WAITING_LOGIN : Client가 Login하기위해 대기하는 상태
- CL_ACTIVE : Client가 Server Side와 맵핑되어 있는 상태
- CL_WAITING : Client가 Server Side와 맵핑하기 위해 대기하는 상태

server side

- SV_ACTIVE : DB의 active session과 동일하며 CL_ACTIVE와 맵핑되는 상태
- SV_IDLE : SV_ACTIVE로 사용하다가 query가 끝나고 남아 있는 상태. 일종의 Pool. DB에서도 idle로 connection 유지.
- SV_USED : SV_IDLE이 일정 시간(server_check_delay) 이후 미사용되면서 Pool로 전환된 상태. DB에서도 idle로 connection 유지.
- SV_TEST : SV_USED가 일정 시간동안 사용되지 않았던 connection이기 때문에 client에게 할당하기전 test query를 실행하는 상태. 일반적으로 select 1; 을 실행.
- SV_LOGIN : Server Side에서 DB로 login을 시도하는 상태.

## client 요청 process

여분의 pool 이 존재할 경우

1. Client가 DB에 Query를 실행하기 위해 PgBouncer에 query 요청.
2. PgBouncer는 Client가 기입한 login정보가 맞는지 확인.
3. 정보가 맞다면 CL_ACTIVE로 상태가 변경되고 SV_IDLE과 SV_USED가 있는지 확인.
4. SV_IDLE 또는 SV_USED가 있으면 SV_IDLE이 우선 CL_ACTIVE에 맵핑되고 SV_IDLE이 없으면 SV_USED가 맵핑.
5. CL_ACTIVE에 할당된 Pool(SV_IDLE, SV_USED)은 SV_ACTIVE로 전환되DB에 Query를 실행시킴.

여분의 pool 이 존재하지 않을경우

1. Client가 DB에 Query를 실행하기 위해 PgBouncer에 query 요청.
2. PgBouncer는 Client가 기입한 login정보가 맞는지 확인.
3. 정보가 맞다면 CL_ACTIVE로 상태가 변경되고 SV_IDLE과 SV_USED가 있는지 확인.
4. SV_IDLE 또는 SV_USED가 없으면 SV_ACTIVE를 생성하고 CL_ACTIVE에 맵핑시켜서 DB에 Query를 실행시킴.
- ** 얼핏보면 pool이 존재할때보다 과정상 단순해 보일 수 있으나 SV_ACTIVE 생성시키는 과정이  DB 와 login 하는 과정부터 시작하므로 좀 느릴 수 있다.

## pool 의 조절

pool 을 너무 많이 할당하면
- db에 과부하

pool 을 너무 적게 할당하면
- response time 이 늘어난다

default pool : PgBouncer의 database에서 pool을 별도로 설정하지 않았을 때, 적용받는 pool size. 일종의 global variable.

database pool : 목적에 따라 분리해서 생성하는 pool로, database별로 pool size를 조절할 수 있음. 여기서 설정하면 default pool size에 영향을 받지 않음.
- ** 여기서 database 라 함은 pg bouncer 의 목적에 따른 pool 을 분리하는 것을 통칭


## pgbouncer 의 위치

- Application server 안에 위치
  - 관리가 힘들지만, DB 에 부하를 줄일 수 있음
- DB 안에 위치
  - localhost communication 을 통해 빠른 피드백 받고 관리가 용이
    - db 서버내에 cpu 가 영향받음


## min_pool_size
- default pool 설정에 그치지 않고 min_pool_size 설정해야 pool 을 유지한다
- 설정후 connection 을 매저주어야 pool 이 하나씩 늘어남
- 많은 커넥션을 맺으면 그만큼 빠른속도로 pool 생성
- min pool size 의 default 는 0


## server lifetime

- pgbouncer pool 은 기본적으로 소진됨
- default 3600초

## minpool size 를 무조건 크게 잡는것이 좋은것인가?

- Client가 PostgreSQL에 접근하기 위해 PgBouncer로 connect
- PgBouncer는 SV_IDLE이 있는지 확인
- SV_IDLE이 없으면 SV_USED를 확인
- SV_USED가 SV_TEST (server_check_query) 후 성공하면 SV_ACTIVE로 상태 변경

이렇게 server_check_query 를 날리는 도중 client 는 대기를 하게 된다 (CL_WAIT 폭증)
- connection 과부하 일때는 responsetime 이 매우 늦어질것
- SV_USED(오랫동안 사용되지 않은 pool)이 많으면 매번 이런 딜레이에대한 리스크가 있음

## SV_USED BAD? 그러면 SV_IDLE 상태를 어떻게 유지하는가?
  
### server_check_delay
- default 값 30 초
- 0 으로 잡게된다면 계속 idle 상태가 되겠지만 아무런 검증 server check query 없이 SV_IDLE 이 SV_ACTIVE 가 되어버릴 것
- 적당한 값을 workflow 에서 찾아야함


min_pool_size : 앞서 말한 SV_IDLE + SV_USED 값으로, default pool size와 database pool size 안에서 pool을 확보하는 si


ref:https://techblog.yogiyo.co.kr/%EB%84%88%EC%9D%98-%EB%82%98%EC%9D%98-%EC%97%B0%EA%B2%B0%EA%B3%A0%EB%A6%AC-db-connection-pooler-pgbouncer-e43ec536a088