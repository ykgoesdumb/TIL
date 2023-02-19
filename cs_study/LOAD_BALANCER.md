## Load Balancing Layer

- L2 : Mac 주소 기반 로드밸런싱
- L3 : IP 주소 기반 로드밸런싱
- L4 : Transport Layer(IP와 Port) Level - Load Balancing(TCP, UDP)
- L7 : Application Layer(사용자의 Request) Level - Load Balancing(HTTP, HTTPS, FTP)
- 가장 흔한 것은 L4, L7 load balancing


## Load Balancer 기능
- *NAT(Network Address Translation)
사설 IP 주소를 공인 IP 주소로 바꾸는 데 사용하는 통신망의 주소 변조기

- DSR(Dynamic Source Routing protocol)
로드 밸런서 사용 시 서버에서 클라이언트로 되돌아가는 경우 목적지 주소를 스위치의 IP 주소가 아닌 클라이언트의 IP 주소로 전달해서 네트워크 스위치를 거치지 않고 바로 클라이언트를 찾아가는 개념

- Tunneling
인터넷상에서 눈에 보이지 않는 통로를 만들어 통신할 수 있게 하는 개념으로, 데이터를 캡슐화해서 연결된 상호 간에만 캡슐화된 패킷을 구별해 캡슐화를 해제할 수 있다.


## L4 LB vs L7 LB

### L4

- IP, port 기준 으로 스케쥴링 알로기름으로 인해 부하 분산
  - 요청하는 서비스 종류와 무관
  - 클라이언트에서 DNS 로 요청 보낼때 최적의 서버로 요청 전송


### L7
- URI, *Payload, Http Header, Cookie 내용 기준
- 콘텐츠 기반 스위칭
  - 악의적 비정상적인 콘텐츠 감지 가능
  - 보안 지점 구축 가능
  - 자원소모 큼



<br></br>
**payload : 전송되는 데이터 (데이터 그자체)


아래의 json data 를 제외한 모든 데이터는 전부 통신에 필요한 것 이기 때문에 payload 가 아니다
```json
{
	"status" : 
	"from": "localhost",
	"to": "http://melonicedlatte.com/chatroom/1",
	"method": "GET",
	"data":{ "message" : "There is a cutty dog!" }
}
```


## Related To
- Kuberentes/HAproxy
- NAT