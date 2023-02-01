
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
- metadata
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