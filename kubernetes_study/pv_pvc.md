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


