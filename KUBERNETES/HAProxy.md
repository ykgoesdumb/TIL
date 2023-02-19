## HAProxy

> HAProxy는 Scale-out을 위해 로드밸런싱을 해주는 SW 로드 밸런서이다

### Scale-up , Scale out

- scale up
  - 서버 사양을 높이는 것
  - 하나의 서버가 한번에 더 많은 응답을 처리할 수 있음

- scale out
  - 부하를 여러서버에게 분산하는경우
  - 이를 load balancing

### SW Loadbalancer? HW Loadalancer?

HW Load Balancer

- 이전에는 값 비싼 L4 HW load balancer 를 사용하였고 MSA의 등장으로 L7 load balancing 도 많이 사용하고 SW 를 사용하는 추세


SW Load Balancer
- AWS ELB, NginX, HaProxy 등등 다양한 소프트웨어 존재

## Haproxy 특징
- L4, L7 HW Load balancer 대체하기 위한 *Reverse Proxy 기반 open source 
- *Active Heath Check
- HTTP 통신의 경우 Web-Server (Nginx, Apache 등)를 이중화 시켜줄수 있으며 HTTP와 같은 표준 프로토콜이 아닌 TCP Socket 통신에 대해서도 *이중화처리가 가능
- HA 구성하기위해 *KeepAlived 사용


### Reverse Proxy
- 실제 서버 앞단에 존재하며 서버로 오는 요청을 대신 받아 뒷단의 서버에 전달하고 결과를 리턴받아 요청한 곳에 다시 전달하는 역할


## HA?
- High Availablity
- 단일 실패 지점(SPOF) 이 없는 인프라 구성을 의미 합니다. 아키텍처의 모든 계층에서 중복성을 추가/유지 하여 단일 서버/시스템의 오류가 다운 타임이 되는 것을 방지 하는데 목적
- 로드 밸런서는 백엔드 계층(웹/앱/API/DB 시스템 등) 에 대한 중복성을 용이하게 하지만 진정한 고가용성 설정을 위해서는 로드 밸런서도 중복으로 있어야 함




## Haproxy setting example

```yaml
- hosts: "{{ group | default('haproxy') }}"
  become: true
  tasks:
    - name: Install haproxy packages
      apt:
        name: '{{ item }}'
        state: latest
        update_cache: yes
      with_items:
        - haproxy

    - name: Copy the haproxy configuration to server location
      copy: src={{ k8s_haproxy_config }} dest=/etc/haproxy/haproxy.cfg mode=0644

    - name: Start haproxy service
      service: name=haproxy state=restarted enabled=yes
```

## haproxy cfg

haproxy.cfg 는 5가지 영역

- global    : 전체 영역에 걸쳐서 적용되는 설정
- defaults  : 다음에 오는 section 에 적용되는 공통 설정 내역
- frontend  : 클라이언트 연결
- backend   : frontend 에서 접속된 트래픽을 전달할 프록시 서버에 대한 설정 과 healthcheck
- listen    : 프론트엔드와 백엔드의 기능이 결합된 완전한 프록시를 정의
            애플리케이션 점점 더 커질경우 개별 frontend backedn 섹션을 사용해야함

```
global
    log /dev/log local0
    log /dev/log local1 notice
    daemon

defaults
    mode http
    log global
    option httplog
    option dontlognull
    option http-server-close
    option forwardfor except 127.0.0.0/8
    option redispatch
    retries 1
    timeout http-request 10s
    timeout queue 20s
    timeout connect 5s
    timeout client 30m
    timeout server 30m
    timeout http-keep-alive 10s
    timeout check 10s

frontend grafana
    bind *:20930
    default_backend grafana

backend grafana
    balance roundrobin
        server node0 192.168.200.50:30930 check
        server node1 192.168.200.51:30930 check
        server node2 192.168.200.52:30930 check

```


---
## Reltated to
- CS_STUDY/LOAD_BALANCER
- Keepalived



ref: 
- https://dev-youngjun.tistory.com/97
- https://jaehoney.tistory.com/73