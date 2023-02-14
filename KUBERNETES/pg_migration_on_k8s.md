postgres 버전 업으로 인하여 기존 버전의 posgres 를 migration 할일이 생겼다


migration 을 하기전에 우선 기존 버전의 db pod 과 migration 을 할 새로운 db pod 이 k8s상에서 띄워져있어야한다

- 이름 겹치지 않게 주의하자


1. 해당 pod으로 들어가서 백업파일을 생성한다

```
kubectl -n {namespace} exec -it {podname} --bash
```

2. /var/lib/postgresql 디렉토리로 이동하여 백업파일을 생성한다

```
cd /var/lib/postgresql
pg_dumpall -U postgres > backup.sql
```

3. 컨테이너 내부에 생성된 백업파일 복사해온다

```
kubectl -n {namespace} cp {podname}:/var/lib/postgresql/backup.sql backup.sql
```

4. 복원할 pod 에 backup file 복사

```bash
kubectl -n {namespace} cp backup.sql {target podname}:/var/lib/postgresql/backup.sql

### 타 클러스터에 있을 경우
scp backup.sql {user}@{ip}:{path}
```

5. 복원할 pod exec 후 복원 실행

```bash
kubectl -n {namespace} exec -it {podname} --bash
psql -f backup.sql -U postgres
```