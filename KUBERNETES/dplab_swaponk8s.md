## Memory Intensive 한 workload
- 물리 메모리의 크기와 속도가 점점더 중요해짐 
  - 데이터의 크기가 커질수록 스토리지와 네트워크의 느린 속도 문제가 심각해짐
  - 이를 해결하기 위해 적극적인 메모리 활용 (cache) (그동안의 big data 주된 해결방식)
  - cpu 입장에서 memory 도 느림 -> l1 l2 l3 cache
  - 스토리지의 느린속도를 cover 하기위해 memory page cache 사용
- 제한적 컴퓨팅 자원 발전 속도
  - processor (cpu) 는 compressable 한 자원 -> 관리 쉬움
  - memory는 uncompressable 한 자원 -> 관리 어려움
    - 할당은 쉽지만 해제가 어렵다

### 메모리가 가장 다루기 어렵다
자원의 종류가 크게 네가지 
- 프로세서
- memory
- storage
- network
라고 하면 

제일 다루기 어려운 것이 "memory"

memory 자원의 할당은 쉽지만 프로세스처럼 해제하고 자원 회수하기가 어렵다
- unevictable (축출불가)
- *dirtypage
- swapout

정확한 워킹셋 예측 어렵다 -> 메모리 활용률 저하 -> 구축/운영 비용 증가


### 메모리가 다루기 어려운 이유들
- 페이지 캐시
  - 수정되지 않은 페이지 캐시는 반환 가능하나, 수정된 캐시는 writeback(반영) 훛 반환가능
- *버퍼캐시
  - 디렉토리 파일 목록, *아이노드(Inode) 등을 메모리에 보관
- 익명페이지
  - Heap 의 영역 (JVM Heap 포함)
    - JVM heap 이 프로세스 heap 위에서 동작
  - 스왑이 꺼져있다면 기본적으로 heap 영역은 반환이 불가능, 있다면 write back 후 반환
- 커널 메모리
  - 커널 스택, 페이지 테이블, *슬랩(Slab)

### 스왑이 꺼져있다면?
- spark job 같은 heap memory 사용하는 job 들 모두 반환 불가능
- 한번만 쓰고 접근 안하는 memory 조차 반환 불가
- memory 사용량이 증가하다가 시스템이 꺼짐


---
## Related to
- LINUX/dirtypage
- 