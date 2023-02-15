# cilium overview
Cilium은 쿠버네티스 및 기타 컨테이너 오케스트레이션 플랫폼에서 사용할 수 있는 네트워크 및 보안 솔루션

- Cilium은 eBPF (extended Berkeley Packet Filter)를 기반으로 하여, 커널 수준에서 빠르고 안전한 패킷 필터링을 제공
- L7 레이어에서의 보안 기능을 제공하여, 애플리케이션 수준에서의 보안을 강화

# cilium function

- L7 보안: Cilium은 L7 레이어에서의 보안 기능을 제공합니다. 이를 통해, HTTP, gRPC 등의 프로토콜에서의 보안을 강화
- 서비스 검색: Cilium은 컨테이너를 기반으로 한 서비스 검색을 제공. 이를 통해, 컨테이너 간의 통신을 쉽게 설정
- 서비스 메시: Cilium은 서비스 메시를 제공하여, 마이크로서비스 간의 통신을 단순화하고 보안을 강화할 수 있다.
- 로드 밸런싱: Cilium은 로드 밸런싱 기능을 제공하여, 컨테이너 간의 부하 분산을 수행할 수 있다. 이를 통해, 서비스의 가용성을 높이고, 성능을 개선한다
- 네트워크 가시성: Cilium은 모든 컨테이너 간의 트래픽을 추적할 수 있도록 해줌. 이를 통해 네트워크 문제를 신속하게 진단하고 해결
- 분산 카운터: Cilium은 분산 카운터를 제공하여, 네트워크의 성능을 모니터링할 수 있다. 이를 통해, 네트워크의 병목 현상을 식별하고, 성능 문제를 해결한다
- 보안 정책: Cilium은 컨테이너 간의 통신을 제어하는 보안 정책을 구현할 수 있다. 예를 들어, 컨테이너 간의 트래픽을 허용할지 거부할지를 결정
- 보안 검사: Cilium은 컨테이너 간의 통신을 검사하여, 보안 위협을 탐지할 수 있다. 예를 들어, Cilium은 DNS 쿼리를 검사하여, 악성 코드가 DNS 서버를 공격하는 것을 방지

# cilium example

```yaml
namespace: kube-system

helmCharts:
  - name: cilium
    includeCRDs: true
    repo: https://helm.cilium.io
    releaseName: cilium
    version: 1.13.0-rc5
    valuesInline:
      k8sServiceHost: 192.168.200.99
      k8sServicePort: 8443
      tunnel: disabled
      kubeProxyReplacement: strict
      autoDirectNodeRoutes: true
      installIptablesRules: true
      l7Proxy: false
      enableCnpStatusUpdates: false
      endpointRoutes:
        enabled: true
      bpf:
        masquerade: true
      masquerade: true
      localRedirectPolicy: true
      ipv4NativeRoutingCIDR: 10.0.0.0/8
      ipam:
        mode: cluster-pool
        operator:
          clusterPoolIPv4PodCIDRList: ['10.0.0.0/8']
          clusterPoolIPv4MaskSize: 24
```