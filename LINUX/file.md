## file
---

linux 에서 모든 데이터를 파일로 표현
- 평범한 파일"부터, 우리가 터미널에서 사용하는 "명령어", 심지어
"디스크나 하드웨어"까지 모두 파일로 인식하고 파일로 다룬다


## file type
---
## 1. 특수 파일


리눅스가 지우너하는 특수 파일에는 "파이프" "주변장치" "소켓" 등이 있음

- 파이프 : |
- 소켓 : 네트워크 접속을 위한 연결장치 역할을 하는 소프트웨어


- LINUX/inode 참조
  - i node 의 첫번째 순서가 파일형식
  - 파일형식 7 개중 4개가 특수 파일 형식
  - b,c,p,s


### b 

- 블록(운영체제가 사용하는 용량단위)형 특수 장치파일

```
629 brw-r-----  1 root         operator   0x1000001 Feb 20 18:20 disk0s1
631 brw-r-----  1 root         operator   0x1000002 Feb 20 18:20 disk0s2
```

### c

- 문자형 특수 파일 (입출력에 사용하는 콘솔등...)
```
335 crw-------  1 kylekim1223  staff              0 Feb 20 18:22 console
```

### p

- 프로세스간 통신에 쓰이는 파이프 
![img src](https://4.bp.blogspot.com/--XM4C06or68/XUFAlNV8g8I/AAAAAAAAAd8/RqkQ_bXxiPEQNbVSeLnftMfCCDAUxP98wCK4BGAYYCw/s640/14.png)


### s

- 소켓파일 : 네트워크 통신에 필요한 파일
  - 두 호스트 컴퓨터 사이의 정보를 전달


![img src](https://3.bp.blogspot.com/--8aZ1-6o4wM/XUFArKJvZkI/AAAAAAAAAeE/o0aq3iWRhJ8M-BBjrsdQw2sm8HcdiUYHACK4BGAYYCw/s640/13.png)

---

앞서 말한 주변장치도 리눅스에서 파일로 다루어진다는 개념의 예시를 들자면

윈도우는  C 드라이브 -> D 드라이브 ... 이런식으로 알파벳  순으로 디스크 번호가 증가한다면

리눅스는 /dev 디렉토리 안에 sda -> sdb -> sdc 이러한 식으로 파일형식으로 존재한다

![img src](https://4.bp.blogspot.com/-DKK5C2oZnIs/XUEc3bz7dvI/AAAAAAAAAcU/JjFIXKIAUH8-b5eO7r-3Qs9GNe4BDC7-QCK4BGAYYCw/s640/5.png)


- 그외 다른 장치도 파일로써 존재하는것을 볼 수 있다 (cpu, disk 등등)

---

## 2. 디렉토리 파일 

디렉토리로 부르나 엄밀히 말하자면 "디렉토리 파일" 이다

i-node 를 검색하였을 때 앞에 'd' 인경우 디렉토리 파일 인 것

```
342 dr-xr-xr-x  1 root         wheel              0 Feb 20 18:20 fd
```

---

## 3. 일반 파일

(특수파일이 아닌)일반 파일일 경우 앞에 - 가 붙음

```
  380657 -rw-r--r--    1 kylekim1223  admin    207 Jun 15  2022 CHANGELOG.md
  380658 -rw-r--r--    1 kylekim1223  admin    829 Jun 15  2022 CONTRIBUTING.md
```

- 텍스트 파일, 이미지 파일, 프로그램 소스파일, 실행파일 이 여기에 속한다
- 실행파일, 이미지 파일은 cat, vi 명령어로 읽을 수 없다
    - binary 파일이기 때문


file 명령어를 쳤을 때 해당 파일의 종류를 알려줌


- 대상이 binary 인 경우

```
file ps

ps: setuid Mach-O universal binary with 2 architectures: [x86_64:Mach-O 64-bit executable x86_64] [arm64e:Mach-O 64-bit executable arm64e]
ps (for architecture x86_64):	Mach-O 64-bit executable x86_64
ps (for architecture arm64e):	Mach-O 64-bit executable arm64e


cat ps

Apple Inc.1&0$U
0pple Ro*H CA0"0pple Certification Authority10U
䑩	�GP��y-�WLU��Kl"0�>P	�A�f$kУ�*�z
�5#KY�XP ˬ, op?0C�=�I(�ε��=:�              G[�73�M�i�r]�_�UM]
�qGSU/A��LE~LkPA�b           !.t�
                  A30X�2h�sg^eI�3ew�z0v0U0U00U+�Gv	�.@G^0U#0+�Gv	�.@G^0U00	*Hcd0�+https://www.apple.com/appleca/0+0Reliance on this certificate by any party assumes accept\6L-x팛�w��0OG7�,Աؾ��d�O4آ>xk��9S �ıOterms and conditions of use, certificate policy and certification practice statements.0
��Sj[dc3w:,V�!ںsO�U٧2B�q~R$*�M^c�P���7uu!10001  /DH�8=&g 3j
```

- 대상이 binary 가 아니고 텍스트인 경우


```
file CHANGELOG.md

CHANGELOG.md: ASCII text

cat CHANGELOG.md

See Homebrew's [releases on GitHub](https://github.com/Homebrew/brew/releases) for the changelog.

Release notes for major and minor releases can also be found in the [Homebrew blog](https://brew.sh/blog/).

```

---

## 4. 링크 파일

- 연결 역할을 하는 파일 이며 두종류가 있음
  - 소프트링크
  - 하드링크


### 소프트 링크

```
lr-xr-xr-x  1 root         wheel              0 Feb 20 18:20 stderr -> fd/2
lr-xr-xr-x  1 root         wheel              0 Feb 20 18:20 stdin -> fd/0
```

- 이것처럼 i node 맨 앞이 l 로 되어있다
- 심볼릭링크와 동의어다

- ln -s  커맨드로 소프트 링크 생성 가능하다

```
ln -s test softlink


67277334 lrwxr-xr-x  1 kylekim1223  staff  4 Mar  3 01:15 softlink -> test
67276844 -rw-r--r--  2 kylekim1223  staff  0 Mar  3 01:14 test
```

- 소프트 링크는 윈도우의 바로가기 와 같다
- 바탕화면에 링크만 만들어두고 클릭하면 원본이 실행되는 형식
- 원본을 삭제한다고해서 링크파일 자체가 없어지진 않으나 제기능을 발휘하지 못함


### 하드링크

- 같은 i-node 번호를 가지고 있는 이름만 다른 똑같은 파일이다
- 복사와는 다른게 복사는 이름이 같을 수 있고 i-node 번호가 다른 "객체" 이다
- 복사는 복사본을 바꿔도 원본은 그대로
- 하드링크는 원본을 바꾸면 하드링크 파일도 똑같이 바뀜

```
ln test harlink

67276844 -rw-r--r--  2 kylekim1223  staff  0 Mar  3 01:14 hardlink
67276844 -rw-r--r--  2 kylekim1223  staff  0 Mar  3 01:14 test
```


아래와 같이 복사본은 i-node 가 다른것을 볼 수 있다

```
cp  hardlink hardlink_copy

67276844 -rw-r--r--  2 kylekim1223  staff  0 Mar  3 01:14 hardlink
67293643 -rw-r--r--  1 kylekim1223  staff  0 Mar  3 01:45 hardlink_copy
67276844 -rw-r--r--  2 kylekim1223  staff  0 Mar  3 01:14 test

```

파일시스템에 혼란을 야기하는 하드링크는 디렉토리로 사용할 수 없다
- 동일 i-node 이므로 뭘 찾아야할지 파일시스템에서 모름

---

## 파일 이름 & 확장자

- 리눅스에는 파일 확장자가 없음
- 다만 구분을 위해서 일관성있는 네이밍이 중요함
- conf, repos, d 등등
