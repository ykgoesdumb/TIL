# 인터넷 네트워크
## 인터넷 통신

결국 HTTP 도 인터넷 망에서 동작

- 인터넷 통신
- IP(Internet Protocol)
- TCP, UDP
- PORT
- DNS


![img src](https://user-images.githubusercontent.com/49462767/227947080-0eaac31d-ac63-4e88-8a33-e56a870dae3a.png)


- 클라이언트 -> 서버로 가기 복잡하게 되어있다면?
  - ip 를 이해해야함

---
## IP 프로토콜

### 인터넷 프로토콜 역할

- 지정한 IP 주소(IP Address)에 데이터 전달
- 패킷(Packet)이라는 통신 단위로 데이터 전달


### IP 프로토콜의 한계
- 비연결성
  - 패킷을 받을 대상이 없거나 서비스 불능 상태여도 패킷 전송
- 비신뢰성
  - 중간에 패킷이 사라지면?
  - 패킷이 순서대로 안오면?
- 프로그램 구분
  - 같은 IP를 사용하는 서버에서 통신하는 애플리케이션이 둘 이상이면?

### 한계의 예시
- 대상이 서비스 불능
- 패킷 소실
- 패킷 전달 순서 문제 발생
  - 1500 byte 이상이면 보통 끊어서 보냄
  - 쪼개진 패킷들이 중간에 다른 노드를 탈 수 있음

### 이러한 것들을 TCP 가 해결해준다 (UDP 는 헤결이라기 보단 도와준다)

---
## TCP, UDP

### 인터넷 프로토콜 스택의 4계층

- 애플리케이션 계층 : HTTP, FTP
- 전송 계층 : TCP, UDP
- 인터넷 계층 : IP
- 네트워크 인터페이스 계층

![img src](https://user-images.githubusercontent.com/49462767/227948488-d168626c-09b3-4a07-9d6e-6b1ce835bc54.png)

- HTTP 를 이해하기위해선 IP 레벨까지 이해하면 더 효율적으로 이해할 수 있음



### IP 패킷 정보

**패킷이란 package + bucket 의 합성어

- 출발지 IP
- 목적지 IP
- 등등

### TCP 세그먼트 정보
- 출발지 PORT, 목적지 PORT
- 전송제어, 순서, 검증정보 ...


## TCP 특징

전송 제어 프로토콜(Transmission Control Protocol)
- 연결지향 - TCP 3 way handshake (가상 연결)
  - 연결을 한뒤 메세지를 보낸다
- 데이터 전달 보증
- 순서 보장
- 신뢰할 수 있는 프로토콜
- 현재는 대부분 TCP 


### 3-way handshake
- syn (접속요청)
- syn+ack
- ack (요청수락)

이 과정이 끝나면 데이터를 전송
- 논리적인 연결


### 데이터 전달 보증
1. 데이터 전송 (클라이언트 -> 서버)
2. 데이터 잘 받았음 (서버 -> 클라이언트)

### 순서 보장

![img src](https://user-images.githubusercontent.com/49462767/227951590-7dbbabc6-2a4b-46fe-9567-a8fd9e7a45bc.png)

- 기본적으로 순서가 맞지 않는다면 맞지 않는 부분 뒤로는 다 버리고 재요청함
- 물론 서버에서 최적화 가능하지만..

## UDP

사용자 데이터그램 프로토콜(User Datagram Protocol)

- TCP 와 같은 계층에있는 프로토콜
- 하얀 도화지에 비유(기능이 거의 없음)
- 연결지향 - TCP 3 way handshake X
- 데이터 전달 보증 X
- 순서 보장 X
- 데이터 전달 및 순서가 보장되지 않지만, 단순하고 빠름
- 정리
  - IP와 거의 같다. +PORT +체크섬 정도만 추가
  - 애플리케이션에서 추가 작업 필요



### UDP 왜 씀?

- TCP 
  - 시간 오래걸린다
  - 전송속도 느림
  - 데이터 큼
- UDP
  - HTTP3
  - 3-way handshake 의 시간도 최적화 해보자

---
## Port
### 한번에 둘 이상 연결하려면?

- 하나의 ip 에서 여러 애플리케이션의 패킷들이 들어온다
  - 그것을 기능별로 구분하는 영역 (port)
  - 같은 IP 내에서 프로세스 구분
  - IP = 아파트
  - port = 몇동 몇호

![img src](https://user-images.githubusercontent.com/49462767/227959763-90b654a1-9b48-493a-aee3-629a3d607c3d.png)


- 0 ~ 65535 할당 가능
- 0 ~ 1023: 잘 알려진 포트, 사용하지 않는 것이 좋음
  - FTP - 20, 21
  - TELNET - 23
  - HTTP - 80
  - HTTPS - 443


---
## DNS

- IP는 기억하기 어렵다
- IP는 변경될 수 있다.


### Domain Name System

- 전화번호부
- 도메인 명을 IP 주소로 변환
- 위의 두 문제를 해결할 수 있음

