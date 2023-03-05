## group


- : 으로 구별된 네개의 영역

```
head etc/group

root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:kylekim,syslog
tty:x:5:
```

### 그룹일름: 패스워드 : GID : 그룹에 속한 유저

- 그룹이름과 똑같은  유저는 안 써있게 리눅스 시스템이 설계됨


## 왜 group 을 사용하나

- 리눅스만 특별히 사용하는게 아니라 대부분의 OS 에서 사용한다
- 리눅스엔 Root 가 있듯이 윈도우에도  "SYSTEM", 관리자 권한을 가진 "Administrators" 가 있음
- 리눅스는 대다수가 (특히 회사에서) 사용하는것을 목표로 하기 때문에 관리적인 측면에서 group 화가 필수적임


---

## group 추가

- 최근에 추가된 그룹은 끝에 추가됨 (tail 로 조회하는것이 편함)


```
groupadd [옵션] [그룹이름]

```

## group password

gpasswd [옵션] [옵션값] [그룹]


### option

- -a [유저] [그룹] 
  - [유저]를 [그룹] 에 넣는다

- -d [유저] [그룹] 
  - 삭제


## id

```
id kylekim

uid=1000(kylekim) gid=1000(kylekim) groups=1000(kylekim),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd)
```

id 를 지정하면 지정한 유저의 uid, gid, groups 를 나타냄
- groups 는 이 아이디가 속한 모든 그룹
- gid가 표시된 그룹이 메인그룹
- 나머지는 보조 그룹


## wheel group

- 10(wheel) group
- 리눅스 gid 999 이하는 시스템에서 원래 만들어져있는 그룹
  - ssh 는 바로 root 로 접근 안됨 (su 명령어를 사용해야됨)
  - 10(wheel) group 에 속한사람들만 su 명령어 사용해서 root 계정에 접근할 수 있음

## group mode

- 그룹정보를 변경

```
groupmod [옵션] [옵션값] [그룹명]

```
 
- -g [변경할 gid]
  - gid 를 변경한다
  - [변경할 gid] 가 위의 식의 [옵션 값이 된다]

```

## kylekim 의 gid를 333 으로 변경한다

groupmod -g 333 kylekim
```

- -n [변경할 이름]
  - 그룹의 이름을 변경한다


```
## 그룹이름을 kylekim -> kylekim_replica

groupmod -n kylekim_replica kylekim
```

---

### gpasswd vs groupmod

- 뒤에 'mod'로 끝나는 것은 '이미 있는 정보'를 modify 하는것
- gpasswd 혹은 passwd는 파일에 없는 정보들을 수정할 때 쓰는 명령어


