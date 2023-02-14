## kustomize

kustomization 파일을 포함하는 디렉터리 내의 리소스 확인 방법

```
kubectl apply kustomize <kustomization 디렉토리>
```

kustomize 리소스 적용
```
kubectl apply --kustomize <디렉토리>
kubectl apply -k <디렉토리>
```


kustomization 파일구성 예시

- kustomization.yaml
- service.yaml
- deployment.yaml

수정할 부분은 patch로 관리한다.
두가지의 방법이 있음

- pachesStrategicMerge
  - 패치하려는 대상을 Kustomization 에 병합하여 패치를 수행 (대상은 파편화, 조각화된 패치)
  - 패치하려는  patch manifest 내부의 object 네임은 반드시 대상으로 지정한 리소스 네임과 기본 템플릿과 일치해야함
- patchesJson6902
  - kubernetes object의 변경을 JSONPatch 규약을 따름
  - 패치하려는 대상의 정보는 patch manifest 내부의 object path 에 맞춰서 value 값을 입력
  - json 패치의 정확한 리소스를 찾기 위해 리소스를 version, kind,name 을 kustomzation.yaml 에 명시



### patchesStrategicMerge
- replace
  - replace를 포함하는 요소가 병합되는 대신 대체
  ```YAML
  containers:
    - name: nginx
    image: nginx-1.0
    - $patch: replace
    ```

- merge
  - merge를 포함하는 요소가 대체되는 대신 병합

- delete
  - delete를 포함하는 요소가 삭제


### 예시
- 원본 deployment.yaml에 수정사항 patch 를 두개를 붙인다
- apiVersion, kind, metadata, spec 등을 맞추어 준다


kustomization.yaml
```YAML
resources: deployment.yaml
patchesStrategicMerge:
- incr_replica.yaml
- set_memory.yaml
```

deployment.yaml
```YAML
apiVersion: apps/v1
kind: Deployment
metadata:
    name: my-nginx
spec:
    selector:
        matchLabels:
            run: my-nginx
    replicas:2
    template:
        metadata:
            labels:
                run:my-nginx
        spec:
            containers:
            - name: my-nginx
              image: nginx
              ports:
              - containerPort: 80
```

set_memory.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: my-nginx
spec:
    template:
      spec:
        containers:
        - name: my-nginx
         resources:
          limits:
            memory: 512Mi
```

incr_replica.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
    name: my-nginx
spec:
    replicas: 3
```

### patchesJson6902

path에 명시된 value 추가, 대체, 제거

- add
  ```yaml
  - op: add
  path: /spec/replicas
  value: 2
  ```
- replace
  ```yaml
  - op: replace
  path: /spec/replicas
  value: 3
  ```
- remove
  ```yaml
  - op: remove
  path: /spec/replicas
  ```


### 예시

kustomization.yaml

```yaml
resources:
- deployment.yaml
  
patchesJson6902:
- target:
    group: apps
    version: v1
    kind: Deployment
    name: my-nginx
  path: patch.yaml
```

patch.yaml

```yaml
- op: replace
 path: /spec/replicas
 value: 3
```

deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
 metadata:
    name: my-nginx
 spec:
    selector:
        matchLabels:
            run: my-nginx
    replicas:2
    template:
        metadata:
            labels:
                run:my-nginx
        spec:
            containers:
            - name: my-nginx
              image: nginx
              ports:
              - containerPort: 80
```


디렉토리는 
```
/someApp

   |_ base
   |_ dev
   |_ prod
```

이런식

공통적으로 배포할 리소스들을 base 에
  
- 클러스터 별 다른 설정값을 가진 리소스들은 각자의 디렉토리에 넣는다 위의 예시는 (dev, prod) 클러스터로 나눈 예
- bases: ~~~ 로 base 디렉토리를 참조하여야한다
- kubectl apply -k prod/ 하면 base+prod의 리소스가 한번에 배포된다



