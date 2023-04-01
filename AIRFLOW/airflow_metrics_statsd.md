## k8s 환경에서 airflow metrics 를 prometheus 로 전달하기

- 꽤 간단한건데 삽질을 조금 오래 하였으므로 기록한다

- airflow 가 metrics 을 prometheus 로 전달하는 방법은 두가지
  - airflow-prometheus-exporter
    - statsd 없이 패키지를 다운받아서 airflow 에서 바로 전달하는 방식
    - 깃헙 스타가.. 영 불안해보인다
    - 각각의 Dag 별로 수집할 메트릭스를 선언해주어야한다..
  - airflow-statsd-exporter
    - 공식 홈페이지에서 권장하는 방법
    - 심지어 airflow official helm chart 에는 statsd 가 포함되어있다
    - airflow-statsd-exporter 를 deployment 형식으로 배포하고 굳이 statsd 를 따로 배포하지 않아도 된다고 한다
<br></br>
- 안전한 두번째 방법을 선택하였고 블로그를 뒤지던중 딱 나의 상황과 맞는 아키텍처를 발견함
  - scheduler 에서 statsd 로 메트릭을 보내고
  - prometheus 가 그 메트릭을 주기적으로 scrape 긁어간다
    - 메트릭을 보내는 port (UDP)
    - 프로메테우스가 긁어갈 port (TCP)
    - 위의 두 port 가 필요하다.

![img src](https://user-images.githubusercontent.com/49462767/226636216-5c7324b7-b0d2-46cc-b562-ec4f11d2636a.png)

---
## 내가 작업한 순서

1. k8s 환경이므로 사용하는 docker image 에 필요한 패키지 설치

```dockerfile
RUN pip3 install apache-airflow[statsd]
```

2. airflow config file 수정

```yaml
## airflow.cfg

[metrics]
statsd_on = True
statsd_host = statsd-exporter
statsd_port = 9125
statsd_prefix = airflow
```

3. statsd-exporter 를 Deployment 로 배포, 그에따른 service 도 배포하였다

- 여기서 annotation 을 붙이는지 수많은 삽질 끝에 알았다...
- selector 또한 통일하지 않았음
- container.args 또한 확실성을 위해 설정해주었다
  - 없이도 동작하는지 아직 검증은 안해봤지만..

```yaml
## statsd-exporter

apiVersion: apps/v1
kind: Deployment
metadata:
  name: statsd-exporter
  namespace: airflow
spec:
  replicas: 1
  selector:
    matchLabels:
      app: statsd-exporter
  template:
    metadata:
      annotations:
        prometheus.io/port: '9102'
        prometheus.io/scrape: 'true'
      labels:
        app: statsd-exporter
    spec:
      imagePullSecrets:
        - name: docker-registry
      containers:
        - args:
            - --statsd.listen-udp=:9125
            - --web.listen-address=:9102
            - --log.level=info
          name: statsd-exporter
          image: prom/statsd-exporter
          imagePullPolicy: Always
          ports:
            - containerPort: 9125
              protocol: UDP
            - containerPort: 9102
              protocol: TCP

---
apiVersion: v1
kind: Service
metadata:
  name: statsd-exporter
  namespace: airflow
  labels:
    app: statsd-exporter
spec:
  ports:
    - name: statsd-ingest
      port: 9125
      protocol: UDP
      targetPort: 9125
    - name: statsd-scrape
      port: 9102
      protocol: TCP
      targetPort: 9102
  selector:
    app: statsd-exporter
```

4. prometheus 에서 service monitor 배포
- 이부분이 제일 어이없었는데
- endpoints 의 port 를 integer 형식으로 9102 로 값을 넘기면 에러가 난다
- 그래서 '9102' 로 str 형식으로 넘겼으나 statsd exporter -> prometheus 로 값이 넘어가지 않는다
- 위에서 선언한 statsd-service 의 port name 을 넘겼더니 동작한다.
  - statsd-scrape

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: airflow-metrics-exporter
  labels:
    app: prometheus
spec:
  selector:
    app: statsd-exporter
  namespaceSelector:
    matchNames:
      - airflow
  endpoints:
    - interval: 30s
      port: statsd-scrape
      path: /metrics
```


## REF
- https://swalloow.github.io/airflow-on-kubernetes-3/
- https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/logging-architecture.html
- https://www.easyaslinux.com/tutorials/run-multiple-statsd-exporter-in-kubernetes-as-a-deployment/