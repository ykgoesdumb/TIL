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
- 제한적인 컴퓨팅 자원의 문제
  - Cgroup(pod)에 충분한 메모리를 할당하지 않을 때
    - jvm oom [Xmx]
    - cgroup oom by kernel [memory max]
  - 시스템에 물리 메모리 부족
    - k8s pod eviction
    - spark executor timeout
    - k8s node not ready

- 실험의 결과는 이러했다
  - spark job 의경우 heap memory 를 계속 땡겨 쓰다가 남은 메모리를 강제로 사용, 그다음 page cache 의 영역도 뺏는다 그러다가 system down 
  - 쿠버네티스라 system down 이후 복원의 자동화가 잘되었지만 얼마나 빨리 복원될지는 미지수

  - *kubernetes eviction 이 잘 설정되어있으면 리소스를 확보를 이론상 가능했겠지만 threshold 를 크게 잡기 애매하다 (default 로 10초에 한번씩 pod eviction 을 수행)


### k8s 1.22 부터 스왑지원

기술들이 좋아졌다.

- 스토리지 성능 개선 (HDD -> ssd -> nvme)
- 리눅스 커널 스왑, 캐시 관리 성능 개선 (MGLRU)

### 스왑을 사용하여 문제점 개선
- 메모리 사용량 -> 성능저하 없음
  - spark batchduration 을 main 지표로 삼고 평가함
- swap in out 지표
  - swap out 이 상대적으로 많음
  - 다시 사용하지 않을 메모리를 잘 반환하였음
- sparkExecutor 가 사용하는 메모리도 안정화 됨

###


---

## 새로이 알게된 것들

- spark executor 는 주기적으로 heartbeat 를 driver 에게 보냄
- heartbeat 가 일정 시간 이상 오지 않으면 강제 재시작
- k8s node not ready
  - 일정시간 이상 노드 상태 확인이 안되면 해당 노드 pod 추출

- Graal VM 과 openjdk
  - JR java runtime engine 에서 jvm heap 관리, 지시 함
  - open source 에서 openjdk 를 많이 쓴다
  - java runtime code 들이 C++ 로 되어있어서 진입장벽이 높음
  - java runtime 을 java 로 개발한 것이 GraalVM 이다
  - open jdk 는 JVM heap 은 process heap 위에서 동작하지만 process heap 을 커널에게 반환하지않음
  - GraalVM 은 이를 반환함
    - allocation 과 해제를 반환하면서 단편화가 생기긴한다
- spark tmpfs


## Related to
- LINUX/dirtypage
- KUBERNETES/qos