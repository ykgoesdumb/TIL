## chown

### 리눅스 소유자, 그룹을 왜 변경하는가?

- 소유자 = 처음에 파일을 만든 사람
- 그룹 = 처음에 파일을 만든 사람이 속한 메인 그룹

- 기본적으로 유저를 만들면 유저는 자기이름과 동일한 똑같은 그룹에 자동적으로 속하게 되어있음
- 리눅스는 파일이든 유저든 "모든 것" 이 소유자 또는 그룹에 속하게 만든다

- 다수가 사용하는 시스템에서 다른 사람의 소유물을 함부로 다루는 것을 방지하기위해 자동적으로 소유자, 그룹 을 나눈다
- 근데 내가 만든 파일이지만 소유권을 이전하고 싶다면?
- chown 을 쓰면 된다

## 소유자를  바꾸는 chown

```
chown [옵션] [소유자:그룹] [파일]
chown [옵션] [소유자.그룹] [파일]
```

```
## hey 라는 파일을 만들었다

touch hey

## default 로 staff 라는 그룹으로 들어감 (MacOS)
ll
-rw-r--r--  1 kylekim1223  staff     0B Mar  5 20:31 hey

## 그룹명을 바꿔보았다
sudo chown kylekim1223:owner hey

ll
-rw-r--r--  1 kylekim1223  owner     0B Mar  5 20:31 hey
```

```
## 이번엔 사용자를 변경하였다.

sudo chown root hey

-rw-r--r--  1 root  owner     0B Mar  5 20:31 hey
```

- ' : ' 앞뒤로 주의를 해야한다
  - chown root: hey 이런식으로 ':' 뒤에 공백을 남기니, 그룹이름이 ':' 앞에 있는 유저와 같은 root라서 생략된 것 같은 여지를 주어 "hey" 의 소유자와 소유그룹이 모두 "root"로 바뀌어버림
  - chown :root hey 이런식으로 ':' 앞에 공백을 남기면 그룹이름만 바뀐다.


- R 옵션 
  - 하위 그룹의 권한까지 다 바뀌어버림


## 소유자 그룹을 바꾸는 chgrp

- change group

```
chgrp [옵션] [바꿀 그룹소유자이름] [파일]
```

- chown 과 마찬가지로 -R 옵션 존재


```
sudo chgrp owner hey

-rw-r--r--  1 root  owner     0B Mar  5 20:31 hey
```
