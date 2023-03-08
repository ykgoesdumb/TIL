## 특수 권한

- 특수권한에 세가지 종류가 있음
  - SetUID {s}
  - SetGID {s}
  - StickyBit {t}

- 3가지  모두 파일의 실행에 관련된 기능으로 사용됨 
  - 권한의 '실행' 자리에 생김
  - 예를들어 특수 권한을 가진 i-node 는 이런식 'drwsrwsrwt'

- 'drwsrwsrwt' 는 모든 특수권한을 다 준 예시이다
  - x 의 자리에 각각 s, s, t 가 들어간 것
  - 이 옵션은 'chmod 7777' 이다

- 기존의 알고있던 chmod 777 은 사실 chmod 0777 이라고 볼 수 있다

![img src](https://2.bp.blogspot.com/-Etb4E_Bplqk/XZm99NqmzII/AAAAAAAAB4Y/LFOGUaI1GSgU_ChTMiyE8F0NH_4V98TyACK4BGAYYCw/s640/%25ED%258A%25B9%25EC%2588%2598%25EA%25B6%258C%25ED%2595%259C%2Brwx.png)


- 한가지 예시를 들어보자
  - 기존에 권한이 777 이던 파일에 StickyBit {t} 의 권한을 주고싶다면?
  - chmod 1777

- x 권한이 없을때 특수권한을 부여해보자

```
touch prac

-rw-r--r--  1 kylekim1223  staff     0B Mar  5 22:42 prac


chmod 7644 prac

-rwSr-Sr-T  1 kylekim1223  staff     0B Mar  5 22:42 prac
```
이렇게 대문자로 권한이 부여된걸 볼 수 있다 

<br>

- x 권한이 없을때 특수권한 과 x 권한을 동시에 부여 해보자
  
```
touch prac

-rw-r--r--  1 kylekim1223  staff     0B Mar  5 22:42 prac

chmod 7777 prac

-rwsrwsrwt  1 kylekim1223  staff     0B Mar  5 22:48 prac
```
---

## SetUID

- setUID가 설정되어있는 root 의 파일을 실행하면 실행이 끝날 때 까지 실행하는 사람의 UID가 root 의 UID '0' 아 되어 root 의 권한을 갖는다
- 조심히 다뤄야 한다
  
- find command 로 SetUID 가 얼마나 사용되는지 볼 수 있음

```
find / -perm -4000

/usr/bin/top
/usr/bin/atq
/usr/bin/crontab
/usr/bin/atrm
/usr/bin/newgrp
/usr/bin/su
/usr/bin/batch
/usr/bin/at
/usr/bin/quota
/usr/bin/sudo
/usr/bin/login
/usr/libexec/security_authtrampoline
/usr/libexec/authopen

```
## SetUID 사용 예시

```
ll -d etc/passwd

-rw-r--r--  1 root  root   7.7K Mar 14  2022 passwd
```
- w 권한은 소유주인 root 밖에없다
- 근데 root 가 아닌 다른계정에서도 passwd 라는 명령어로 바꿨었다 왜일까?


- /usr/bin/passwd 에 특수권한이 부여되었기 때문이다

```
ll -d /usr/bin/passwd
-rwsr-xr-x  1 root  root   169K Feb  7  2022 /usr/bin/passwd
```

- "리눅스는 모든 것을 파일로 취급한다"
- linux 혹은 macos 를 쓰면서 사용하는 터미널 명령어들은 사실상 "실행파일" 인것
- 그 실행파일에 other 에 read 와 execute 권한이 있었기 때문에 모든 유저가 사용 가능했던 것

- mkdir 을 터미널에치는것이 사실상
  - /usr/bin/mkdir 
  - 파일을 실행시키는 것 이다


---

## SetGID

```
find / -perm -2000

/usr/bin/write
find: /usr/sbin/authserver
/usr/sbin/postqueue
/usr/sbin/postdrop

```

### wall 명령어

wall 은 벽이 아니라 (write to all임)
- 누구나 사용 가능하다
- n 옵션은 root 만 사용가능

```
usage: wall [-g group] [file]

 -g, --group <group>     only send message to group
 -n, --nobanner          do not print banner, works only for root
```

```
wall hi

Broadcast message from haruband@node0 (pts/2) (Sun Mar  5 14:58:54 2023):

hi
```

- usr/bin/wall 실행파일 권한을 봐보자

```
ll -d /usr/bin/wall

-rwxr-sr-x 1 root tty 22904 Feb 21  2022 /usr/bin/wall*
```
- SetGID 가 설정되어있다
- tty 란 그룹으로 설정되어있음 (UID 1000 이하는 시스템에 원래 존재하는 유저아이디)

### tty
- TeleTYpewriter 의 줄임말 (전기식 타자기)
- tty = 터미널

```
ll -d /dev/tty

crw-rw-rw- 1 root tty 5, 0 Mar  5 09:11 /dev/tty
```

- 아이노드의 c "character special" 
- 그룹 tty 는 "터미널 을 사용하기 위한 그룹"


### wall again

- 그렇다면 wall 은 모든 터미널에게 메세지를 보내야하므로 상위 권한이 필요함
- SetGID
- /usr/bin/wall 을 실행할때 그 파일의 GID 즉 'tty' 가 되어서 "/dev/tty" 를 사용할 수 있게 되는 것!
- "SetGID"는 실행을 할 때 그 파일의 그룹의 GID로 적용


### directory file 에 SetGID 가 설정된다면?
- 디렉터리 내부에 파일을 만들면 디렉터리 기능이 실행 되는 것이므로
- 내부 파일들에도 모두 SetGID가 적용된다


### directory file 에 SetUID 가 설정되면 SetGID 처럼 일괄 적용되나?
- 리눅스에선 소유자를 바꾸는 건 "root"만 가능하게 설정되어 있기 때문에 
- 디렉터리에 "SetUID"를 설정해도 그 디렉터리 안에 만드는 파일들의 소유자가 바뀌는 일이 없다.
- 디렉터리의 "SetUID"의 기능을 실행하는 건 "root"가 아니라 "일반유저"


---

## StickyBit

- 원래 유닉스 운영체제에서 실행파일의 실행속도 향상을 위해 사용되던 개념
