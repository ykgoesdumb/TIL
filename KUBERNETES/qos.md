## k8s qos (quality of service)

파드 생성시 파드에 세가지중 하나의 qos class 를 할당
- Guaranteed
- Burstable
- BestEffort


### Guranteed

- 파드 내 모든 컨테이너는 memory limit과 memory request 를 가져야한다
- 파드 내 모든 컨테이너는 memory limit과 memory request가 일치해야한다
- 파드 내 모든 컨테이너는 cpu limit과 cpu request 를 가져야한다
- 파드 내 모든 컨테이너는 cpu limit과 cpu request가 일치해야한다


```yaml
apiVersion: v1
kind: Pod
metadata:
  name: qos-demo
  namespace: qos-example
spec:
  containers:
  - name: qos-demo-ctr
    image: nginx
    resources:
      limits:
        memory: "200Mi"
        cpu: "700m"
      requests:
        memory: "200Mi"
        cpu: "700m"

...
status:
  qosClass: Guaranteed
```


### Burstable

- 파드가 Guaranteed QoS 클래스 기준을 만족하지 않는다.
- 파드 내에서 최소한 하나의 컨테이너가 메모리 또는 CPU 요청량/상한을 가진다.

```yaml
spec:
  containers:
  - image: nginx
    imagePullPolicy: Always
    name: qos-demo-2-ctr
    resources:
      limits:
        memory: 200Mi
      requests:
        memory: 100Mi
  ...
status:
  qosClass: Burstable
```

### Best Effort

- 파드에 QoS 클래스 BestEffort를 제공하려면, 파드의 컨테이너에 메모리 또는 CPU의 상한이나 요청량이 없어야 한다.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: qos-demo-3
  namespace: qos-example
spec:
  containers:
  - name: qos-demo-3-ctr
    image: nginx
...
status:
  qosClass: BestEffort
```


## 우선순위

Guaranted > Burstable > Best Effort

- 자원이 부족할때 가장 중요도 낮은 pod 부터 kill 함
