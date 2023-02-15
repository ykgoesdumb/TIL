## Kubernetes 에서 node 하나를 빼서 test server 로 따로 구축 하는 시나리오이다.

production cluster 에 4개의 node 중 하나를 분리해서 1개의 node 를 test 용으로 운영

밑의 예시는 ansible playbook으로 cluster 설치를 하고있다.


```yaml
all:
  vars:
    ansible_user: user
    ansible_password: password
    ansible_become_password: password
    k8s_swap_size: 128G
    k8s_limits_config: limits.conf
  hosts:
    proxy0:
      ansible_host: 192.168.200.254
    proxy1:
      ansible_host: 192.168.200.50
    node0:
      ansible_host: 192.168.200.50
    node1:
      ansible_host: 192.168.200.51
    node2:
      ansible_host: 192.168.200.52
    node3:
      ansible_host: 192.168.200.53
  children:
    keepalived:
      hosts:
        proxy0:
          k8s_keepalived_config: configs/dot/keepalived0.conf
        proxy1:
          k8s_keepalived_config: configs/dot/keepalived1.conf
    haproxy:
      hosts:
        proxy0:
        proxy1:
      vars:
        k8s_haproxy_config: configs/dot/haproxy.cfg
    master:
      hosts:
        node0:
      vars:
        k8s_kubeadm_config: configs/dot/master.yaml
        k8s_format_blkdevices: ['nvme1n1', 'sda']
        k8s_delete_blkdevices: ['nvme1n1', 'sda']
        k8s_audit_policy: configs/dot/audit.yaml
    slave:
      hosts:
        node1:
        node2:
      vars:
        k8s_kubeadm_config: configs/dot/slave.yaml
        k8s_format_blkdevices: ['nvme1n1', 'sda']
        k8s_delete_blkdevices: ['nvme1n1', 'sda']
        k8s_audit_policy: configs/dot/audit.yaml
    worker:
      hosts:
        node3:
      vars:
        k8s_kubeadm_config: configs/dot/worker.yaml
        k8s_format_blkdevices: ['nvme1n1', 'sda']
        k8s_delete_blkdevices: ['nvme1n1', 'sda']
        k8s_audit_policy: configs/dot/audit.yaml
```

- 위의 설정에서 떼어낼 node 와 host 를 지운다 (여기선 node3 를 지움)
- 지우는 node 에 할당되어있던 haproxy도 지워준다

새로 구축하는 server 의 config 를 생성해준다

- audit.yaml
  
```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  - level: None
    verbs: ['get', 'watch', 'list']

  - level: None
    resources:
      - group: ''
        resources: ['events']

  - level: None
    users:
      - 'system:kube-scheduler'
      - 'system:kube-proxy'
      - 'system:apiserver'
      - 'system:kube-controller-manager'

  - level: RequestResponse
    userGroups: ['system:serviceaccounts']

```

- master.yaml

```yaml
apiVersion: kubeadm.k8s.io/v1beta3
kind: InitConfiguration
bootstrapTokens:
  - groups:
      - system:bootstrappers:kubeadm:default-node-token
    token: abcdef.0123456789abcdef
    ttl: 24h0m0s
    usages:
      - signing
      - authentication
nodeRegistration:
  criSocket: unix:///var/run/crio/crio.sock
  imagePullPolicy: IfNotPresent
  taints: []
certificateKey: 0faec066c7b58657b6e9879c79d32b7ab1e7208a3c93dff6f6de0b4b4412d5ff
skipPhases:
  - addon/kube-proxy
---
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
apiServer:
  extraArgs:
    oidc-issuer-url: https://keycloak.manager.ingkle.com/realms/k8s
    oidc-client-id: dot
    oidc-username-claim: email
    oidc-groups-claim: groups
  timeoutForControlPlane: 4m0s
certificatesDir: /etc/kubernetes/pki
clusterName: dot.testing
controllerManager: {}
dns: {}
etcd:
  local:
    dataDir: /var/lib/etcd
imageRepository: registry.k8s.io
kubernetesVersion: 1.26.1
networking:
  dnsDomain: cluster.local
  serviceSubnet: 172.16.0.0/16
  podSubnet: 10.0.0.0/8
scheduler: {}
---
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
featureGates:
  NodeSwap: true
failSwapOn: false
memorySwap:
  swapBehavior: UnlimitedSwap
maxPods: 200
```

그외에 external secret 등등을 디렉토리에 맞게 적용한뒤 services 를 올리면 된다

