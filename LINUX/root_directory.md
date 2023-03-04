## 상위 디렉토리로

## /bin

```
lrwxrwxrwx   1 root root     7 Aug  9  2022 bin -> usr/bin/
```
- bin 유저가 리눅스를 사용할 때 필수적으로 필요한 바이너리 파일들(명령어 파일) 이 들어있는 디렉토리
- 컴파일된 실행파일들

- / 디렉토리에 있는 bin 은 링크 파일이며 실제 bin 은 usr/bin 에 들어가있음

## /dev

```
### 깨알 명령어 상식
-d 옵션은 디렉토리 파일 그자체를 보는 옵션

ll -d dev

drwxr-xr-x 19 root root 4620 Feb 14 06:06 dev/

```

- 디바이스를 나타내는 특수 파일들이 있는 디렉토리
- SATA 방식의 disk 는 /dev/ "sda" 로 존재

```
brw-rw----  1 root disk      8,     0 Feb 14 06:06 sda
```
<br>

가상의 장치들도 있다
- dev/random
    - 랜덤한 수 생성
- dev/null
    - 무언가 넣으면 사라지는 장치

## /lib

- lib(library)
- bin 과 sbin 디렉토리의 파일들이 실행될 때마다 즉시 필요한 파일들이 들어있음

```
lrwxrwxrwx 1 root root 7 Aug  9  2022 lib -> usr/lib/
```

## /lib64

- lib 의 64 비트 버전


## /mnt

```
drwxr-xr-x 2 root root 4096 Aug  9  2022 mnt/
```

- mount
  - 파일을 어떤 공간과 연결한다는 것
- 시스템 관리자들이 보통 임시적으로 파일시스템을 마운팅할 때 쓰는 디렉토리
  - 파일 시스템 : 디스크를 관리하는 소프트웨어

## /proc

- proc
  - 시스템에서 운영되고 있는 커널이나 프로세스들에 대한내용이나 프로그램들을 가지고 있는 디렉토리

```
dr-xr-xr-x 937 root root 0 Feb 14 06:06 proc/
```

## /run

- 실행되고있는 프로세스들이 들어있는 파일

## /srv

- srv(service data)은 시스템으로부터 제공되는 특정사이트들의 데이터,
- ftp, rsync, www와 같은 프로토콜 데이터들이 기본적으로 저장되는 디렉토리

- 이제 www나 ftp 프로토콜을 이용해 사이트에서 뭔가 활동을 하면 사이트에서 얻는 정보들이 보통 이 디렉토리에 쌓인다

```
drwxr-xr-x 2 root root 4096 Aug  9  2022 srv/
```

## /tmp

- temporary files
  - 인터넷을 열때 그 인터넷에대한 정보를 다운받는데 다운받은 파일을 바로 삭제하지 않고 임시적으로 놔두는 파일
  - tmp file 은 초록색이다
  - 누구나 이 디렉토리를 쓰고 읽고 실행할 수 있음

- sticky bit t
  - i node 끝에 t 가 붙음
  - 모든 유저가 접근가능하나 각 유저가 만든 건 자기만 삭제 수정 할수 있게 되어잇음

```

drwxrwxrwt 11 root root 4096 Mar  3 06:13 tmp/

         ^ : sticky bit

```

## /usr

- universal system resource & read-only files

- 시스템, 리드 온리 파일들이 있는 디렉토리
- window c drive 의 program files

```
drwxr-xr-x 14 root root 4096 Aug  9  2022 usr/
```

- 링크파일이던 /bin /lib /lib64 /sbin 의 원본이 여기있다


## /var

- variable data files
- 수정할 수 있는 /usr
- 가장 대표적으로 var 안에 log 가 있다

```
var directory 안에 있는 것 들

ls
backups  cache  crash  lib  local  lock  log  mail  opt  run  snap  spool  tmp
```

## /boot

- boot files
- 시스템 부팅에 필요한 파일들이 있는 곳


## /etc
- etcetra 이지만 시스템과 관련된 설정파일들이 있는 곳
- 특정 유저만 쓰는 설정파일은 그 유저의 홈 디렉토리에 생김

## /media
- 매개가 되는 장치들 파일을 가는 디렉토리
- CD-ROM 이나 플로피디스크 같은 제거가능한 미디어(매개체)들을 리눅스에 사용할 때 마운트 지점으로 사용하는 곳

- /mnt 와 다른점
  - /mnt 는 시스템 관리자들이 파일시스템을 마운팅 할때 사용
  - /media 는 매개체 사용시 마운트 하는 지점

## /opt
- optional pacakages
- 파일 시스템에 종속되지 않는 개개인 소프트웨어 파일
- 응용프로그램들이 보통 이 디렉토리에 설치됨

## /root

- root(root home)는 이름 그대로 root의 홈 디렉토리

```
drwx------ 7 root root 4096 Feb 14 08:38 root/
```

## sbin

- system binaries
- root계정으로 활동하는 시스템관리자를 위한 /bin 디렉토리

## sys

- sys(sysfs)란 sysfs가 마운팅 된 디렉토리
- sysfs 란?
  - /proc 디렉토리에 안 무질서하게 있던 디바이스 관련 파일들을 체계적으로 정리해주는 역할
  

```
ls
block  bus  class  dev  devices  firmware  fs  hypervisor  kernel  module  power
```

---

1. 명령어가 들어있는 곳
   - bin / sbin
   - bin 과 sbin 은 /usr 에 있다

2. 어떤 시스템에 관련된 프로그램 설정을 바꿔야할 것 같다면?
   - /etc

3. A 라는 유저가 게임을 깔았다면 그 파일은 어디에 있나?
   - A 만 쓰는 프로그램이므로 A 유저 홈 디렉토리에있다
   - /opt 가 아님

4. 커널이나 프로세스에 대한 파일들은 어디있나?
   - /proc 에 있음

5. wireshark 프로그램을 root권한으로 깔았을 때 어디에 저장될까?
   -  /usr에 저장이 될 것이다

6.  wireshark의 log파일 같이 수정가능한 파일은 어디에 저장될까?
   - /var에 저장이 될 것이다.

7. root계정으로 로그인해서 홈에서 만든 파일들은 어디에 저장이 될까?
   - /root디렉토리에 저장 될 것이다.
