
# livenessProbe

쿠버네티스가 제공하는 self-healing과 재시작 메커님즘

쿠버네티스가 컨테이너 상태를 확인할 수 있도록 pod livenessProbe를 선언하는 방법

kubelet 은 livenessProbe 의 엔드포인트를 체크함으로써 상태를 확인할 수 있음

```yaml
livenessProbe: 
	httpGet: # probe 엔드포인트
		path: /health
		port: 8080 
	initialDelaySeconds: 3  # 컨테이너 시작 후 몇 초후에 probe를 시작할 것인가
	periodSeconds: 1        # probe 실행 주기
	successThreshold: 1     # 몇 개 성공 시 실패 횟수를 초기화할 것인가
	failureThreshold: 1     # 연속으로 몇 번 실패 했을 때 컨테이너를 재시작할 것인가 
	timeoutSeconds: 3       # 응답을 몇 초 만에 받아야 하는가
	

```

비교 대조를 위해 의도 적으로 조작한 unhealthy pod 과 healthy pod 을 생성해

어떻게 행동하는지 파악

```
NAME        READY   STATUS              RESTARTS   AGE
healthy     0/1     ContainerCreating   0          5s
unhealthy   0/1     ContainerCreating   0          5s
unhealthy   1/1     Running             0          12s
healthy     1/1     Running             0          15s
unhealthy   1/1     Running             1 (1s ago)   47s
unhealthy   1/1     Running             2 (2s ago)   82s
unhealthy   1/1     Running             3 (1s ago)   116s
unhealthy   1/1     Running             4 (0s ago)   2m31s
unhealthy   0/1     CrashLoopBackOff    4 (1s ago)   3m6s
unhealthy   1/1     Running             5 (54s ago)   3m59s
unhealthy   1/1     Running             6 (1s ago)    4m31s
unhealthy   0/1     CrashLoopBackOff    6 (1s ago)    5m6s
unhealthy   1/1     Running             7 (2m52s ago)   7m57s
unhealthy   0/1     CrashLoopBackOff    7 (1s ago)      8m31s
```

healthy 한 pod 은 계속 running 중이나

unhealthy 한 pods은 계속 생성과 에러를 반복한다.

오류가 나는 pod 을 describe 

```yaml
kubectl describe pod unhealthy
```

```
Name:         unhealthy
Namespace:    default
Priority:     0
Node:         gke-cluster-1-default-pool-606eed14-1prm/10.128.0.3
Start Time:   Tue, 13 Sep 2022 20:14:29 +0900
Labels:       app=myapp
Annotations:  <none>
Status:       Running
IP:           10.4.2.122
IPs:
  IP:  10.4.2.122
Containers:
  unhealthy:
    Container ID:   containerd://e6e0eb67feaaada5077817af9573b1c602fd507b79b86238bd0111c421c91f08
    Image:          yoonjeong/unhealthy-app:1.0
    Image ID:       docker.io/yoonjeong/unhealthy-app@sha256:8a8fa1b5009ec4f60e51e3cd157552de9b0bd7072b860286825c43d1d8fd2168
    Port:           8080/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       CrashLoopBackOff
    Last State:     Terminated
      Reason:       Error
      Exit Code:    143
      Started:      Tue, 13 Sep 2022 20:19:00 +0900
      Finished:     Tue, 13 Sep 2022 20:19:34 +0900
    Ready:          False
    Restart Count:  6
    Limits:
      cpu:     50m
      memory:  64Mi
    Requests:
      cpu:        50m
      memory:     64Mi
    Liveness:     http-get http://:8080/ delay=30s timeout=10s period=5s #success=1 #failure=1
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-8sgmw (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  kube-api-access-8sgmw:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                    From               Message
  ----     ------     ----                   ----               -------
  Normal   Scheduled  5m39s                  default-scheduler  Successfully assigned default/unhealthy to gke-cluster-1-default-pool-606eed14-1prm
  Normal   Pulling    5m31s                  kubelet            Pulling image "yoonjeong/unhealthy-app:1.0"
  Normal   Pulled     5m28s                  kubelet            Successfully pulled image "yoonjeong/unhealthy-app:1.0" in 3.068976571s
  Normal   Killing    3m9s (x4 over 4m54s)   kubelet            Container unhealthy failed liveness probe, will be restarted
  Normal   Created    3m8s (x5 over 5m28s)   kubelet            Created container unhealthy
  Normal   Started    3m8s (x5 over 5m28s)   kubelet            Started container unhealthy
  Normal   Pulled     3m8s (x4 over 4m53s)   kubelet            Container image "yoonjeong/unhealthy-app:1.0" already present on machine
  Warning  Unhealthy  2m34s (x5 over 4m54s)  kubelet            Liveness probe failed: HTTP probe failed with statuscode: 500
  Warning  BackOff    21s (x8 over 2m33s)    kubelet            Back-off restarting failed container
```

container 에서는 에러 코드가 뜨고 events 한 항목항목이 다 뜬다.



# readinessProbe

- 준비가 안된 파드를 제외하여 클라이언트에게 불편한 경험을 주지 않을 수 있다
- 쿠버네티스가 컨테이너 준비정도를 확인할 수 있도록 pod readinessProbe를 선언하는 방법


준비성을 검사하기위한 장치

- 일정 수준이상 연속해서 실패하면 서비스 엔드포인트에서 파드를 제거한다

failureThreshold 를 안넘고 success 가 뜬다면 쌓였던 error count 초기화 한다

failureThreshold 값 만큼 연속으로 실패할 경우에만 pod를 제거한다.

pod-readinessProbe-probe

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: unhealthy
  labels:
    app: myapp
spec:
  containers:
  - name: unhealthy
    image: yoonjeong/unhealthy-app:1.0
    ports:
      - containerPort: 8080
    readinessProbe:
      exec:
        command:
          - ls 
          - /var/ready
      initialDelaySeconds: 60
      periodSeconds: 5
      successThreshold: 1 
      failureThreshold: 1
      timeoutSeconds: 10
    resources:  
      limits:
        memory: "64Mi"
        cpu: "50m"
```

service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
```

```bash
# LoadBalancer 타입의 서비스 생성
kubectl apply -f service.yaml

# 서비스 ExternalIP 확인
kubectl get svc -w

# 서비스 엔드포인트를 환경변수 SERVICE로 저장
export SERVICE=$(kubectl get svc myapp -o jsonpath="{.status.loadBalancer.ingress[0].ip}")

# healthy, unhealthy 파드 생성 
kubectl apply -f pod-readinessProbe-probe.yaml

# 서비스 엔드포인트를 관찰
kubectl get endpoints -w

# 파드 READY를 관찰, 몇 초가 흐른 뒤...
kubectl get pod -o wide -w

# Pod 이벤트를 확인하여 문제 원인 확인
## Events
## 파드 Conditions
#   Type              Status
#   Initialized       True 
#   Ready             False 
#   ContainersReady   False 
#   PodScheduled      True 
kubectl describe pod/unhealthy

# 서비스 엔드포인트로 요청 실행
for i in {0..5};
do curl -v $SERVICE;
done

# unhealthy 파드에 접속하여 /var/ready 디렉토리 생성
kubectl exec -it unhealthy -- mkdir /var/ready 

# 서비스 엔드포인트, 파드 READY 상태를 관찰

# 서비스, 파드 삭제
kubectl delete all -l app=myapp
```

결과 값

```
endpoints

NAME         ENDPOINTS            AGE
kubernetes   34.172.176.111:443   41d
myapp        <none>               179m
myapp                             179m

pods

NAME        READY   STATUS    RESTARTS   AGE
unhealthy   0/1     Pending   0          0s
unhealthy   0/1     Pending   0          1s
unhealthy   0/1     ContainerCreating   0          2s
unhealthy   0/1     Running             0          29s
```

describe 했을때

```
Events:
  Type     Reason     Age                From               Message
  ----     ------     ----               ----               -------
  Normal   Scheduled  2m28s              default-scheduler  Successfully assigned default/unhealthy to gke-cluster-1-default-pool-606eed14-5dqq
  Normal   Pulling    2m18s              kubelet            Pulling image "yoonjeong/unhealthy-app:1.0"
  Normal   Pulled     2m3s               kubelet            Successfully pulled image "yoonjeong/unhealthy-app:1.0" in 15.097580883s
  Normal   Created    2m3s               kubelet            Created container unhealthy
  Normal   Started    2m2s               kubelet            Started container unhealthy
  Warning  Unhealthy  3s (x13 over 58s)  kubelet            Readiness probe failed: ls: /var/ready: No such file or directory

```

/var/ready 디렉토리가 없기 때문에 fail 이 뜸



ref: https://medium.com/finda-tech/kubernetes-pod%EC%9D%98-%EC%A7%84%EB%8B%A8%EC%9D%84-%EB%8B%B4%EB%8B%B9%ED%95%98%EB%8A%94-%EC%84%9C%EB%B9%84%EC%8A%A4-probe-7872cec9e568