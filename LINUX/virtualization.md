## 가상화

- 단순히 VM 을 만들수 있게 해주는 기술 이 아님
- 와이파이, 즉 "NAT(Network Address Translation)"도 바로 가상화 기술
- 그외에도 여러가지 다방면으로 가상화 기술이 쓰이고있음

## 서버 가상화

- CPU 나 메모리 같은 하드웨어 자원을 10~20% 만 사용한다
- 서버에서 사용되는 서버 프로그램에 비교해 하드웨어의 진보로 서버 자원이 남아돈다
- 이것을 최대한 사용할 수 있게 해주는 기술이 "서버 가상화"


한개의 컴퓨터에 여러개의 서버를 가상화로 구현해도 전력과 공간을 배로 아낄 수 있다

서버 가상화는 어떤식으로 구현하느냐에 따라
- 전 가상화 (bare-metal/ hypervisor)
- 반가상화 (part-virtualization)
- 호스트 기반 가상화

로 나눌 수 있다.

---

## 전 가상화

bare-metal 은 어떠한 프로그램이나 OS 가 설치되지 않은  순수한 하드웨어를 의미함


### hypervisor
- 여러개의 vm 들을 보고 관리하는 역할

- 전 가상화는 OS 가 아닌 hypervisor 가 설치되어 여러 vm 들을 관리하는 구조

---

## 반 가상화

- para-virtualization
- 전 가상화보다 높은 성능을 보여준다
- vm 들이 직접 일부 하드웨어 자원을 사용할 수 잇음
- 98% 까지 실제 컴퓨터처럼 성능 향상이 가능
- VM 에 dlTsms 게스트 OS  의 커널 일부분을 수정해줘야 하는 번거로움 존재

---

## 호스트 기반 가상화

- 호스트를 기반으로 가상화
  - 여기서 호스트란 일반 컴퓨터가 사용하는 운영체제 "window, macos"

![img src](https://2.bp.blogspot.com/-DYgH30jYtPQ/XonVRmZk-jI/AAAAAAAAENo/OX3NziFFjycr99RtMWBFVfr7FTpuHk1agCK4BGAYYCw/s400/21.png)


윈도우 운영체제에서 vmware 를  깔아서 VM 을 구현하는 형태

