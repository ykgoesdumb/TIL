

## what is swap?

- 스왑(swap)이란 물리 메모리(RAM)의 용량이 부족할 때 하드 디스크의 일부 공간을 메모리 처럼 사용하는 것
- kuberenetes 는 default 로 swap 이 disabled


## swap out , swap in

현재 메모리에 최대 100개의 프로세스가 올라갈수 있는데 이때, 101번째 프로세스가 추가로 올라가야 할 경우

- swap out
  - 100개의 실행된 프로세스중 특정 프로세스를 잠시 Swap Partition으로 이동시켜 놓는 것

- swap in
  - 스왑으로 이동했던 프로세스에서 이벤트가 올 경우, 다시 메모리 영역으로 이동시키는 것

Swap 기능은 본래 가용된 메모리보다 더 큰 메모리 할당을 가능하도록 하기 위함
- 쿠버네티스 철학은 주어진 인스턴스의 자원을 100% 가깝게 사용하는 것이 목표인데
- 스왑 메모리를 켜놓으면 인스턴스 자원이 일관되지 않아 이러한 철학에 부합되지 않는 것

예전에는 node 에서 swap 이 감지되면 kubelet 이 시작이 되지 않았다 (현재는 지원)

### 메모리 기반 workload가 너무 많으므로 swap 을 잘 사용하면 유용할 것


---
## 사용방법

- node 별로 swap behavior 를 설정할 수 있다
- limited 와 unlimited


```yaml
memorySwap:
  swapBehavior: LimitedSwap
```
- default 값이 limited
- burstable 과 guranteed 를 swap 을 안쓰게 함으로써 불확실성을 낮춤
- 쿠버네티스 에서 관리되지 않는 workload 는 swap 을 쓸 수 있음

```yaml
memorySwap:
  swapBehavior: UnlimitedSwap
```
- system limit 까지 사용가능



