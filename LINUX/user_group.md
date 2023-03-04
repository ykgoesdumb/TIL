## user group

- window 와 마찬가지로 linux도 user, group, other 의 개념이 있다
- window 는 personal Computer 에 특화되어있지만 linux 는 multi-user 서버용 운영체제
- 권한에 더 민감하다
  

---

## useradd

- useradd [옵션] [유저이름]
- useradd 로 만든 유저는 password가 없음


## passwd

- passwd [옵션] [유저이름]
- 관리자 (root)는 모든 유저의 패스워드를 변경할 수 있고 8개 문자보다 짧게만들수 있음
- 일반 유저는 자신의 비밀번호만 변경가능하고 8개보다 짧게 못 만든다

## su

- su 만 치면 root 로 로그인 하겠다는 뜻
- su -[유저아이디]
---
## /etc/passwd

- 컴퓨터 전역에 영향을 미치는 설정파일이 들어있는 /etc
- 리눅스 유저 데이터베이스 파일

```
cat passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
```

### 계정 ID: Password : UID : GID: comment: 홈디렉토리: 쉘 환경 순서이다

- 패스워드 부분은 노출이되면 안되기 때문에 x 로 표시된다
- 패스워드는 etc/shadow 라는 파일에서 관리

- UID
  - user ID 식별번호
- GID
  - group ID 그룹 식별번호
- comment
  - description 보통 user 이름과 똑같은게 적혀있음
- 홈 디렉토리
  - 각 유저의 홈 디렉토리
- 쉘 환경
  - 각 유저가 쓰는 쉘이 뭔지 나타냄


## /etc/shadow


```
[sudo] password for kyk:
root:*:19213:0:99999:7:::
daemon:*:19213:0:99999:7:::
```
- 원래 패스워드는 1~4096 중 랜덤한 숫자로 암호화 되었음
- 모든 경우의수를 다 따지는 dictionary attack 에 취약
- root 만 접근 가능한 /etc/shadow 에다가 복잡한 방식으로 암호화
---

## usermod

- user 의 정보를 바꾸는 명령어

usermod 옵션

            -u(user id)
            -g(group id)
            -c(comments)
            -d(home directory)
            -s(shell)
            -L(LOCK,잠금)
            -U(UNLOCK)


- 모든 유저는 하나의 그룹에 속하게 되어있음
- 새로만든 유저는 그 "유저의 이름" 으로 그룹이 자동으로 생기고 그 그룹에 속하게 된다


- usermod -L
  - user 잠금해서 로그인 유저목록에 사라진다
- usermod -U
  - unlock

기존에 설정된걸 바꿀 때는 옵션을 하나하나 띄어서 써줘야한다 예를들어

- usermod -Lcd bob
    - 이런식으로 옵션을 붙여쓰면 동작하지 않음
- usermod -c hey -g 1004 -u 1004 hello
  - 이런식으로 작성해야함

---
## userdel

유저를 지우는 명령어

- userdel 로만 유저를 지운다면 유저만 사라지고 user의 home directory 라던지 하위 정보들이 남아있다
- userdel -r 옵션을 써야 모두 지울 수 있음


