## i-node


linux 에서 모든 데이터를 파일로 표현
- 평범한 파일"부터, 우리가 터미널에서 사용하는 "명령어", 심지어
"디스크나 하드웨어"까지 모두 파일로 인식하고 파일로 다룬다


i stands for Index

- I(index) Node의 줄임말
  
Node?

- 데이터의 지점이나 장치


i-node?

- 데이터를 갖고있는 것을 빠르게 찾기위해 순서대로 정리한 정보


command
```
ls -l 
```
- 위의 명령어를 쳤을때 나오는것들이 inode

```
drwxr-xr-x   5 kylekim1223  staff      160 Jan  8 08:40 AIRFLOW
drwxr-xr-x   4 kylekim1223  staff      128 Feb 23 09:10 BOOK_SUMMARY
drwxr-xr-x  22 kylekim1223  staff      704 Feb 24 11:07 CS_STUDY
drwxr-xr-x   2 kylekim1223  staff       64 Feb 18 23:22 DOCKER
drwxr-xr-x   6 kylekim1223  staff      192 Dec  8 11:32 JAVASCRIPT
drwxr-xr-x  22 kylekim1223  staff      704 Feb 24 14:54 KUBERNETES
drwxr-xr-x   8 kylekim1223  staff      256 Mar  2 14:33 LINUX
drwxr-xr-x   3 kylekim1223  staff       96 Dec 31 23:40 ML
drwxr-xr-x   6 kylekim1223  staff      192 Feb 24 11:45 POSTGRES
drwxr-xr-x   5 kylekim1223  staff      160 Feb 14 11:06 PYTHON
-rw-r--r--@  1 kylekim1223  staff  6129399 Nov 30 20:47 README.md
drwxr-xr-x   3 kylekim1223  staff       96 Dec  8 14:09 SHELL_SCRIPT
drwxr-xr-x   8 kylekim1223  staff      256 Jan 26 21:40 SQL
drwxr-xr-x   3 kylekim1223  staff       96 Nov 30 20:08 TYPESCRIPT
```

이 부분이 i node 이며 순서대로 아래의 구성으로 되어있다.


![img src](https://1.bp.blogspot.com/-lm6ZMz468H4/XUFAOpAbiVI/AAAAAAAAAdc/55vztd9a2aYi-B3MNfQbgOF12knWYcA_gCK4BGAYYCw/s640/10.png)


1.파일형식(- , d , l, b , c, p, s)

2.파일권한(소유자|그룹 |그 외사람들)

3.링크 수

4.파일 소유주

5.파일 그룹

6.파일크기

7.파일이 만들어진 시간


이처럼 리눅스에서 다루는 모든 파일은 i-node 를 가지고 있고 새로운 파일이 생성될때 i-node 도 같이 생성된다
- i-node 를 모아두는 i-node list table 도 있다

i-node 번호가 각 파일마다 고유하게 있음

```
ls -li

#결과

42350308 drwxr-xr-x   5 kylekim1223  staff      160 Jan  8 08:40 AIRFLOW
19567991 drwxr-xr-x   4 kylekim1223  staff      128 Feb 23 09:10 BOOK_SUMMARY
52203369 drwxr-xr-x  22 kylekim1223  staff      704 Feb 24 11:07 CS_STUDY
61847562 drwxr-xr-x   2 kylekim1223  staff       64 Feb 18 23:22 DOCKER
24424333 drwxr-xr-x   6 kylekim1223  staff      192 Dec  8 11:32 JAVASCRIPT
37149079 drwxr-xr-x  22 kylekim1223  staff      704 Feb 24 14:54 KUBERNETES
63188230 drwxr-xr-x   8 kylekim1223  staff      256 Mar  2 14:33 LINUX
41180142 drwxr-xr-x   3 kylekim1223  staff       96 Dec 31 23:40 ML
63577658 drwxr-xr-x   6 kylekim1223  staff      192 Feb 24 11:45 POSTGRES
59434384 drwxr-xr-x   5 kylekim1223  staff      160 Feb 14 11:06 PYTHON
23861458 -rw-r--r--@  1 kylekim1223  staff  6129399 Nov 30 20:47 README.md
28778128 drwxr-xr-x   3 kylekim1223  staff       96 Dec  8 14:09 SHELL_SCRIPT
41180144 drwxr-xr-x   8 kylekim1223  staff      256 Jan 26 21:40 SQL
23841200 drwxr-xr-x   3 kylekim1223  staff       96 Nov 30 20:08 TYPESCRIPT
```



