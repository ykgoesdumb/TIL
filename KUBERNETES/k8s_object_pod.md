
오브젝트를 생성할때
- 직접생성
- kubectl

 kubernetes api 이용할때 요청 내용안에 JSON 형식으로 정보를  포함시켜줘야함

 대부분의 경우 .yaml 로  kubectl 에 제공 -> kubectl 은 api 요청이 이루어질 때 JSON  형식으로 정보 변환

- kubectl apply



yaml 파일에 요구되는 필드

- apiVersion 
  - 이 오브젝트를 생성하기 위해 사용하고 있는 쿠버네티스 API
- kind 
  - 어떤 종류의 오브젝트
- metadatacod 
  - 이름 문자열 UID
- spec
  - 오브젝트에 대해 어떤 상태를 의도하는지


## pod

- kubernetes 에서 생성하고 관리할 수 있는 가장 작은 컴퓨팅 단위
- pod 는 docker container 와 흡사 
- 쿠버네티스는 컨테이너를 직접 관리하는 것이 아닌 파드를 관리한다
- deployment , job, statefulset (상태 추적), daemonset 같은 워크로드 로 pod 생성 
  - 직접 pod 를 사용자가 생성할일은 거의 없다



### pod os
- pod 실행할 OS 를 명시할 수도 있다.
  - .spec.os.name

### controller

- 하나의 node 가 실패하면  해당 node 의 pod 가 작동을 중지했음을 인식하고 대체 파드를 생성한다
- 스케쥴러는 대체파드를 정상 노드에 배치한다

## pod template

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: hello
spec:
  template:
    # 여기서부터 파드 템플릿이다
    spec:
      containers:
      - name: hello
        image: busybox:1.28
        command: ['sh', '-c', 'echo "Hello, Kubernetes!" && sleep 3600']
      restartPolicy: OnFailure
    # 여기까지 파드 템플릿이다
```


## metadata

pod 의 데한 metadata 는 불변이다

- generation 은 현재 값을 증가시키는 갱신만 허용

파드 갱신은 아래의 필드 외에는 변경하지 않음
- spec.containers.image
- spec.initContainers.image
- spec.activeDeadlineSeconds
- spec.tolerations



## pod networking

pod 는 각 주소에 대해 고유한 IP 주소가 할당됨
- ip 주소 및 네트워크 포트
- pod 에 속한 container 는 localhost 를 사용하여 서로 통신할 수 있음
- 다른 pod 의 컨테이너는 ipc 로 통신 불가
- pod 에 구성된 name 이 pod 내 컨테이너 시스템 호스트 명
