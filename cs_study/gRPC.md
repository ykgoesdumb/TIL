# gRPC
- gRPC는 Google에서 개발한 오픈소스 RPC(Remote Procedure Call) 프레임워크
- gRPC는 프로그래밍 언어 간에 클라이언트 및 서버 애플리케이션을 구축하고 실행하는 데 사용.
- TCP/IP, HTTP2.0, IDL(Interface Definition language)로 protocol buffer를 사용


# pre-requisite
- protocol buffer
- RPC
- networking
- server & application dev
- multi-threading



# gRPC의 주요 특징.

간단한 인터페이스 정의: gRPC는 Protocol Buffers를 사용하여 간단한 인터페이스 정의를 제공합니다. 이를 통해, 클라이언트 및 서버 개발자는 서비스 및 메서드를 쉽게 정의하고 구현할 수 있습니다.

다양한 언어 지원: gRPC는 다양한 프로그래밍 언어를 지원합니다. 이를 통해, 서로 다른 언어로 작성된 클라이언트와 서버 간에 통신할 수 있습니다.

높은 성능: gRPC는 HTTP/2 프로토콜을 기반으로 하며, 바이너리 프로토콜 버퍼를 사용합니다. 이를 통해, 높은 성능 및 효율성을 제공합니다.

스트리밍: gRPC는 스트리밍을 지원합니다. 이를 통해, 클라이언트 및 서버 간에 양방향 스트리밍 및 단방향 스트리밍을 수행할 수 있습니다.

인증 및 보안: gRPC는 TLS 및 SSL과 같은 보안 프로토콜을 지원하며, OAuth2와 같은 인증 기술도 지원합니다.

gRPC는 클라이언트 및 서버 간에 안전하고 효율적인 통신을 가능하게 하는 강력한 RPC 프레임워크입니다. gRPC는 단순한 인터페이스 정의와 다양한 언어 지원, 높은 성능 및 스트리밍 기능 등을 제공하여, 클라이언트 및 서버 애플리케이션 개발을 더욱 쉽고 효율적으로 만듭니다.


ref:https://chacha95.github.io/2020-06-15-gRPC1/