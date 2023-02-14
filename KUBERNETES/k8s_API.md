


---
**controll plane 의 핵심은 kubernetes apiserver 이다**
---

kuberentes api object
- pod
- namespace
- configmap
- event

등등을 query 가능하다


작업하는 방식은  아래와 같다
- kubectl CLI
- kubeadm
- REST API

---

## OpenAPI

- k8s 는 openapi v2 스펙을 제공
- 클러스터 내부 통신을 위해 protobuf 에 기반한 직렬화 형식 구현


## kubernetes API 의 확장

- CustomResourceDefinition
- Aggregation Layer

## custom resource
- 이것은 k8s api 의 extension
- 기본 쿠버네티스 설치에서 반드시 사용할 수 있는것은 아니나 많은 핵심 쿠버네티스 기능은 custome resoure 로 인해 구현됨
- kubectl 로 생성 접근 가능

## custome controller
- custom controller 와 customresource 가 결합하면 선언적 api 제공


## Aggregation layer
- 코어 쿠버네티스 api 를 확장한 추가 api 
  - metric server 혹은 사용자 개발 api 일 수 있다
- kube-apiserver 프로세스 안에서 구동됨
- api 등록 위해서 사용자는 URL 경로를 요구하는 APIService 오브젝트를 추가해야 한다.
- pod 내에서 extension API server 를 실행하는 것이 가장 일반적
- apiserver-builder library
- extension apiserver 는 kube apiserver 로 오가는 연결 latency 가 낮아야함

---

추가 할 부분:
https://kubernetes.io/ko/docs/concepts/extend-kubernetes/api-extension/custom-resources/