# 11. CPU 스케쥴링
## 11-1 CPU 스케쥴링 개요
> 운영체제는 cpu 를 어떻게 분배하는가?
- cpu 스케쥴링
- 우선순위
- 스케쥴링 큐
- 대기 큐
- 준비 큐
- 선점형 스케쥴링
- 비선점형 스케쥴링
---

프로세스마다 cpu 집중 이거나 입출력 집중 등 필요로하는 자원이 다를 수 있음
- I/O bound process
  - 대기상태에 더 많이 머무름
  - I/O burst
- CPU bound process
  - 실행상테에 더 많이 머무름
  - CPU burst
- 프로세스 별로 우선순위를 두어서 빠르게 처리하는것이 효율적
  - PCB 에 우선순위를 명시
  - 아래의 명령어로 확인 가능
```
ps -el
  UID   PID  PPID        F CPU PRI NI       SZ    RSS WCHAN     S             ADDR TTY           TIME CMD
    0     1     0     4004   0  37  0 408826528  16336 -      Ss                  0 ??         0:18.73 /sbin/launchd
    0    90     1     4004   0  31  0 408599664  32752 -      Ss                  0 ??         0:20.09 /usr/libexec/logd
    0    91     1     4004   0  31  0 408267104   9088 -      Ss                  0 ??         0:00.77 /usr/libexec/UserEventAgent (System)
    0    93     1     4004   0  20  0 408048816   2208 -      Ss                  0 ??         0:00.10 /System/Library/PrivateFrameworks/Uninstall.framework/Resources/uninstalld
    0    94     1  1004004   0  50  0 408243904   7632 -      Ss                  0 ??         0:21.23 /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/FSEvents.
    0    95     1     4004   0   4  0 408267904  15488 -      Ss                  0 ??         0:00.28 /System/Library/PrivateFrameworks/MediaRemote.framework/Support/mediaremoted
    0    97     1     4004   0  31  0 408779968   2304 -      Ss                  0 ??         0:02.72 /Library/Application Support/org.pqrs/Karabiner-DriverKit-VirtualHIDDevice/Applic
    0    98     1     4004   0  20  0 408823808   4672 -      Ss                  0 ??         0:13.72 /Library/Application Support/org.pqrs/Karabiner-Elements/bin/karabiner_observer
    0   100     1     4004   0  31  0 409233168   7664 -      Ss                  0 ??         0:28.19 /Library/Application Support/org.pqrs/Karabiner-Elements/bin/karabiner_grabber
    0   103     1     4004   0   4  0 408274560  13648 -      Ss                  0 ??         0:01.58 /usr/sbin/
```
- nice 명령어를 통해 우선순위 교체 가능

### 스케쥴링 큐

- 다음 우선순위를 찾기위해 모든 PCB 를 뒤지는것은 비효율적
- queue 를 만들어 대기시킴
- scheduling queue 는  꼭 FIFO 일 필요가 없음

![img src](https://user-images.githubusercontent.com/49462767/226086528-b5a47770-bdb1-48b6-9d5b-b03e87999236.png)


- ready queue
  - cpu 줄
- waiting queue
  - 입출력 장치 줄
  - 입출력 인터럽트 발생시 대기 큐에서 작업이 완료된 PCB 찾고 준비 큐로 올려보냄 그리고 대기큐에서 제거

### 선점형 스케쥴링 (preemptive scheduling)
- 운영체제가 프로세스로부터 자원을 강제로 빼앗아 다른 프로세스에게 할당 하는 것
- 자원의 독점 불가
- 정해진 시간이 끝나면 timer interrupt 발생

### 비선점형 스케쥴링 (non-preemptive scheduling)
- 프로세스가 끝나거나 스스로 대기상태로 변하지 않는한 중간 개입 허용하지 않음
- 자원 독점
- context switch 가 적지만 그만큼 프로세스간 비효율 발생할 수 있음
---

## 11-2 CPU 스케쥴링 알고리즘
- FCFS (first come first served)
  - 선착순, 비선점형 스케쥴링
  - convoy effect (앞의 프로세스 모두 끝나는 시간 + 현재 프로세스 소요 시간)
  - 짧은 프로세스더라도 오래걸리는 프로세스가 앞에 있다면 무조건 기다려야함
- SJF (shortest job first) 스케쥴링
  - 가장 짧은 job 부터 끝마치는 방식
  - convoy effect 를 방지
  - 비선점형으로 구성되나 선점형으로 구성될 수도 있음
- RoundRobin scheduling
  - FCFS 에 timeslice 를적용한 방식
  - time slice = 정해진 cpu 사용 시간
  - time slice 를 정할때 적정량으로 정해야함
    - time slice 너무 크면 envoy effect 그대로 발생할 것
    - time slice 너무 작으면 context switching 이 너무 자주 일어날 것
  
- SRT (shortest remaining time)
  - roundrobin + SJT 
  - timeslice 만큼 cpu 사용하되 그 다음 순서는 가장 잔여소요시간이 적은 job 을 우선순위로 배치


### 우선순위의 근본적인 문제

- 우선순위대로 작업을 할당하면 우선순위가 낮은 작업들은 계속 자원을 할당받지 못하는
- 'Starvation' 기아 현상이 발생할 수도 있음
- 이에따라 대기열에 오래 있으면 점진적으로 우선순위가 높아지는 'aging' 이라는 시스템 생김


### 다단계 큐 스케쥴링

- 우선순위에 따라 큐를 여러개 배치
  - 우선순위 0순위 큐, 1순위 큐 ...
- 큐별로 time slice 를 다르게 설정 가능
- 큐별로 알고리즘 다르게 설정도 가능


### 다단계 피드백 큐 스케쥴링

- 우선순위 큐 간 프로세스 이동 가능
- cpu 사용기간이 길면 우선순위 점진적으로 낮혀 밑의 큐로 보냄
- 우선순위 낮은 큐에서 장시간 대기한 프로세스의 경우 점진적으로 우선순위 높이는 에이징 적용
- 알고리즘 복잡하지만 가장 일반적인 cpu 알고리즘