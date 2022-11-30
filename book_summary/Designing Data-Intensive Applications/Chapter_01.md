## 01. 신뢰할 수 있고 확장 가능하며 유지보수하기 쉬운 애플리케이션
---

### 전통적인 애플리케이션은 아래와 같은 구조를 요구한다

- 데이터베이스

- 캐시

- 검색 색인 (search index)

- 스트림 처리 (stream processing)

- 일괄 처리 (batch processing)




하지만 현실은 꽤나 복잡하다. 데이터 저장,처리의 도구들은 용도에 따라 제각기 다른 성능을 내고
(redis, elastic search, kafka 등등) 

더 많은 애플리케이션이 ‘단일 도구’로는 요구를 만족시키지 못함 

 
```
이러한 맥락 속 개발자들은 ‘데이터 시스템 설계자’ 역할도 을 짊어져야 한다고 이 책은 말하고 있다.
```
 

### 소프트웨어 시스템의 핵심인 3가지 요소를 설명하였고 이것이 이책의 내용의 전반적인 핵심

- 신뢰성

- 확장성

- 유지보수성

 
---
# 신뢰성

- 애플리케이션은 사용자가 기대한 기능을 수행한다

    - 시스템은 사용자가 범한 실수나 예상치 못한 소프트웨어 사용법을 허용할 수 있다

    - 시스템 성능은 예상된 부하와 데이터 양에서 필수적인 사용 사례를 충분히 만족한다

    - 시스템은 허가되지 않은 접근과 오남용을 방지한다.

 



## 결함(fault)과 장애(failure) 그리고 내결함성(fault-tolerant)

- 결함 : 잘못될 수 있는일

- 장애: 필요한 서비스를 제공하지 못하고 시스템 전체가 멈춤

- 내결함성: 결함을 예측하고 대처할 수 있는 성질(시스템)

 

## 하드웨어 결함

```
하드웨어 결함은 일상이다. 최근 카카오 사태 처럼 화재, 대규모 정전, 램 결함 등등 이유는 수없이 많다

어플리케이션  계산 요구가 증가 (앱의 발전) 하면서 하드웨어 결함률 도 올라갔다.
```


대응책 = 중복(redundancy)

- 디스크 RAID 구성 설치 (RAID : 복수의 HDD 를 하나의 디스크 처럼 인식 시키는 기술)

     - 참고: https://www.elecom.co.jp.k.gj.hp.transer.com/pickup/column/storage_column/00003/index.html

- hot-swap 가능한 CPU

    - hot -swap : 전원이 켜져있는(작동중인) 시스템을 끄지 않고 부품을 교체 할수 있는 방식이다.

    - 참고: https://kk-7790.tistory.com/29

- 데이터 센터 예비 전원 발전기

## 소프트웨어 결함

- 하드웨어 결함보다 더 예측 힘들고 상관관계가 많아 시스템 오류를 더 많이 유발함

- 메모리,CPU 시간, 디스크 공간

- 시스템 속도 저하로 인한 잘못된 응답 반환

- 2012 리눅스 커널 버그 (윤초) 로 수많은 애플리케이션 중단 사례

    - 참고: https://blog-tech.tadatada.com/2016-12-28-struggling-with-the-leap-second

    신속한 해결책은 없다

    테스트, 프로세스 격리, 모니터링 ,분석 등등을 면밀히 실행해야 시스템에서 보장을 기대할 수 있음

 

## 인적오류
- 사람은 미덥지 않다 (하드웨어 결함율 10~ 25% 에 그친다)

- 사람이 못미더운데 시스템을 어떻게 신뢰성 있게 만들까?

- 오류의 가능성 최소화 하게 설계 (추상화, api, 관리 인터페이스)

- 사람이 가장 많이 실수하는 부분에서 사람의 실수로 장애 발생 부분을 분리 (sandbox 제공)

- 단위 테스트부너 전체 시스템 통합 테스트, 수동 테스트 등 모든 수준의 테스트를 철저히

- 장애 발생 영향 최소화 (rollback rollout) 하고  데이터 재계산 도구 제공

- 상세하고 명확한 모니터링 대책 마련 

- 조작 교육과 실습을 시행

--- 

# 확장성

```
오늘 잘돌아가는게 내일 잘돌아간다는 보장이 없다

유저가 1만명에서 10만명 으로 늘어날 수도있다.
```
 
엔지니어로써 바람직한 확장성의 고민은 이러하다

- 시스템이 특정 방식으로 커지면 대처하는 방식은? 
- 추가 부하를 다루기 위해 계산자원을 어떻게 투입? ….


## 부하 매개변수

- 웹 서버의 초당 요청 수

- 데이터베이스의 읽기 대 쓰기 비율

- 대화방의 동시 활성 사용자
- 캐시 적중률
  -  