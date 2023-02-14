## Cluster
- 최초 k8s 배포될때 cluster 를 얻는다 (dot, aot, dev 클러스터등 각자 회사마다 명칭은 상이하다)

---
## Node
각 클러스터는 최소 한개의 node를 가진다 (현재 회사의 경우 클러스터당 3개의 노드가 있음)
- 각 node 는 pod 를 호스트 한다
- node 안에는 아래와 같은 것들이 있다.
  - kubelet
  - kube-proxy 
  - container runtime
    - containerd
    - CRI-O


### 1. **kubelet**
   - pod 에서 컨테이너가 확실하게 동작하도록 관리 (pod Spec)

### 2. **kube-proxy**
    - 각 node 에서 실행되는 네트워크 프록시
    - svc 개념의 구현부
   - service(svc) = 네트워크 서비스로 pod 집합에서  실행중인 애플리케이션 노출시키는 방법
### 3. **container runtime**
   - 컨테이너 실행을 담당하는 소프트웨어
   - 대표적으로 docker

---
## Control Plane
클러스터의 전반적인 결정을 수행, 이벤트를 감지하고 반응한다

구성은 이러하다

- kube-apiserver
- etcd
- kube-scheduler
- kube-controller-manager
- cloud-controller-manager


### 1. **kube-apiserver**
apiserver는 controll plane 의 front-end 이다
- 수평으로 확장 가능, 인스턴스 추가 가능

### 2. etcd
- 모든 클러스터 데이터를 담는 쿠버네티스 뒷단의 저장소 key-value storage

### 3. kube-scheduler
- 노드가 배정되지 않는 pods 를 감지하고 실행할 노드를 선택
- 스케쥴링 결정을 위해서 아래와 같은것들을 고려함
    - affinity
    - anti-affinity
    - 데이터 지역성
    - 워크로드 간 간섭
    - 등등

### 4. kube-controller-manager
controller 프로세스를 실행하는 control plane 의 component


### controller 란?
- apiserver 를 통해 상태 감시, 현재 상태를 원하는 상태로 이행시키는 루프

    - node-controller
      - node 다운시 대응
    - job-controller
      - 일회성 job object 감시
    - endpoint controller
      - 서비스와 파드 연결
    - service account & token controller
      - 새로운 네임스페이스에 대한 기본계정과 api 접근 토큰을 생성


### 5. cloud-controller-manager

- cluster 를 cloud 공급자의 API 를 연결하고, 해당 클라우드 플랫폼과 상호작용하는 컴포넌트와 클러스터와만 상호작용하는 컴포넌트를 구분 

---


## addons

애드온은 쿠버네티스의 기능을 확장한다. 대표적으로 많이 사용되는 addon 은 아래와 같다

- DNS
- 웹 UI (대시보드)
- 컨테이너 리소스 모니터링
- 클러스터 레벨 로깅








