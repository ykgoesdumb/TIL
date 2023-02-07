## 컨테이너 Probe 비활성화 또는 제거

- container  Probe: kubelet 에 의해 주기적으로 수행되는 진단(diagnostic)
  - stateful 한 db 서비스와는 맞지 않다
  - connection, DB lock 등에 의해서 재구동 되는 상황이 발생함

## kubectl exec 으로 장기간 수행된는 명령

- 백업 압축 업로드 등에서 장기간 kubectl exec 으로 수행중 정상종료 되지않음
  - kubectl 은 끊겨도, 컨테이너 프로세스는 동작하고있음
  - 백업이 다 완료되지 않은 상태에서 압축이 진행
  - 완료됬다고 뜨지만 실제 파일은 엉망
- kubectl exec 은 네트워크가 불안정하거나 사용량 많으면 끊길 수 있음