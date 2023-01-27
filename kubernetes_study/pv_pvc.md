## PV

persistent volume
- pv 는 볼륨 그자체 cluster 안에서 자원으로 다룸
  

## PVC

persistent volume clainm
- 사용자가 PV 에게 하는 요청
- 사용하고 싶은 용량, 모드

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: airflow-logs
spec:
  storageClassName: local-path-sda
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 16G
```

### 쿠버네티스는 중간에 PVC 를 두어 파드간 사용할 스토리지를 분리 시킬 수 있음
- manifest 분리
- 각 pod 는 어떠한 볼륨인지 신경쓸 필요 없다
- kubectl get pv (namespace 와 무관하게 그 storage 에서 전체가 출력됨)



## PV 와 PVC 의 생명주기

provisioning -> binding -> using -> reclaiming


- provisioning
  - pv 를 생성하는 단계
  - static, dynamic 방식 존재
    - static 은 클러스터 관리자가 미리 적정 용량의  pv 를 만들어 놓음
    - dynamic 은 사용자가 pvc를 거쳐서 pv를 요청했을 때 생성해 storage class정의된 storage 로 제공
- binding
  - provisioning 으로 만든 pvc 와 pv 를 연결하는 단계
  - 1 대 1 매핑 (여러개 될 수 없음)
- using
  - pvc 는 pods 에 설정하고  pod 는 pvc 르르 볼륨으로 인식하여 사용
  - 할당된 pvc 는  pod을 유지하는동안 계속 사용하여서 시스템에서 임의로 삭제 불가
    - storage object in use protection

- reclaiming
  - 사용 끝난 pvc 는 삭제되고 pv는 초기화 하는 과정을 거침
  - 초기화 전략에는 retain, delete, recycle 이 있음
    - retain
      - pv를 그대로 보존
    - recycle
      - pv의 데이터들을 삭제하고 다시 새로운 pvc에서 pv를 사용할 수 있도록 함
    - delete
      - pv를 삭제하고 연결된 외부 스토리지 쪽의 볼륨도 삭제

## access mode

- ReadWriteOnce: 노드 하나에만 볼륨을 읽기/쓰기하도록 마운트할 수 있음
- ReadOnlyMany: 여러 개 노드에서 읽기 전용으로 마운트할 수 있음
- ReadWriteMany: 여러 개 노드에서 읽기/쓰기 가능하도록 마운트할 수 있음




참조 링크: https://kimjingo.tistory.com/153