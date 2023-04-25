
git-sync 적용을 하던 도중 github 에 ssh 키를 등록하고 연결시키는 간단한 step 에서 상당히 많은 시간을 뺏기며 삽질을 하였다. 시행착오를 줄이기 위해 기록차 남긴다.

- mac은 ssh-keygen 을 하였을때 rsa key 를 생성하지 않고 openSSH 를 생성한다.
  - public key는 rsa
  - private key 는 openssh 의 형식으로 생성됨
  - 이는 git 연동할때 invalid format 에러를 낸다
  - invalid format 이여서 오타가 발생 한것이라 판단하고 무한 삽질을 하였다.
- linux 는 rsa 를 생성한다

  
아래의 링크에서 우연히 해답을 발견하였음
- https://serverfault.com/questions/939909/ssh-keygen-does-not-create-rsa-private-key

- mac에서 rsa key pair 를 만들기위해서 -m PEM 옵션을 사용해주어야한다.

```
ssh-keygen -m PEM -t rsa -b 4096 -C "kylekim1223@gmail.com"
```