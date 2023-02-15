## container runtime

컨테이너 런타임(Container Runtime)은 컨테이너 이미지를 실행하는 소프트웨어

- 컨테이너 이미지 관리: 컨테이너 런타임은 컨테이너 이미지를 관리하고, 컨테이너를 실행하는 데 필요한 레이어를 다운로드.
- 컨테이너 실행: 컨테이너 런타임은 컨테이너를 실행하고, 네트워크 및 스토리지와 같은 리소스를 할당.
- 컨테이너 관리: 컨테이너 런타임은 컨테이너의 생명주기를 관리하며, 중지, 삭제 및 업데이트와 같은 작업을 수행.
- 컨테이너 보안: 컨테이너 런타임은 컨테이너의 보안을 강화하는 기능을 제공. 예를 들어, 컨테이너를 격리하고, 호스트 시스템과의 상호 작용을 제한할 수 있습니다.

## container runtime 중 하나인 cri-o
- CRI (container runtime interface)
- CRI-O 는 Kubernetes 용 Open Container Initiative (OCI) 컨테이너 런타임이다
- Kubernetes 에서 주로 사용되었던 Docker 를 대체하는 것에 목적
- CRI-O는 runc, the OCI runtime, conmon, and other low-level container tools를 기반으로 컨테이너 실행 및 관리를 수행
- opensource

## cri-o functions
- OCI 컨테이너 런타임 지원: CRI-O는 OCI 컨테이너 런타임을 지원하며, Docker와 호환된다. 이를 통해, CRI-O를 사용하여 기존의 Docker 이미지와 컨테이너를 실행할 수 있다.
- 컨테이너 생명주기 관리: CRI-O는 컨테이너의 생성, 시작, 중지 및 제거와 같은 생명주기 관리를 수행. 또한, 컨테이너의 리소스 사용량을 모니터링하고, 리소스 제한을 적용할 수 있다.
- CNI 네트워크 지원: CRI-O는 CNI(Container Network Interface)를 준수하며, 다양한 네트워크 플러그인을 지원. 이를 통해, CRI-O를 사용하여 다양한 네트워크 환경에서 컨테이너를 실행할 수 있다.
- SELinux 및 AppArmor 보안 지원: CRI-O는 SELinux 및 AppArmor와 같은 보안 기술을 지원. 이를 통해, 컨테이너를 보호하고, 안전한 환경에서 실행할 수 있다.
- 빠른 시작 시간: CRI-O는 빠른 시작 시간을 제공, 대규모 컨테이너 클러스터에서도 안정적으로 동작한다.


ref:http://www.opennaru.com/kubernetes/cri-o/