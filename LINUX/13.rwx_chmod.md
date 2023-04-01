## 리눅스의 권한

- i node 에 포함되어있다

```
drwxr-xr-x   5 kylekim1223  staff   160B Jan  8 08:40 AIRFLOW
drwxr-xr-x   4 kylekim1223  staff   128B Feb 23 09:10 BOOK_SUMMARY
drwxr-xr-x  22 kylekim1223  staff   704B Feb 24 11:07 CS_STUDY
drwxr-xr-x   2 kylekim1223  staff    64B Feb 18 23:22 DOCKER
drwxr-xr-x   6 kylekim1223  staff   192B Dec  8 11:32 JAVASCRIPT
drwxr-xr-x  22 kylekim1223  staff   704B Feb 24 14:54 KUBERNETES
drwxr-xr-x  18 kylekim1223  staff   576B Mar  5 21:01 LINUX
drwxr-xr-x   3 kylekim1223  staff    96B Dec 31 23:40 ML
drwxr-xr-x   6 kylekim1223  staff   192B Feb 24 11:45 POSTGRES
drwxr-xr-x   5 kylekim1223  staff   160B Feb 14 11:06 PYTHON
-rw-r--r--@  1 kylekim1223  staff   5.8M Nov 30 20:47 README.md
drwxr-xr-x   3 kylekim1223  staff    96B Dec  8 14:09 SHELL_SCRIPT
drwxr-xr-x   8 kylekim1223  staff   256B Jan 26 21:40 SQL
drwxr-xr-x   3 kylekim1223  staff    96B Nov 30 20:08 TYPESCRIPT
```

- 앞에 drwx ~~ 가 권한을 의미함


![img src](https://2.bp.blogspot.com/-ObA52TdnHw0/XYdKN6k91VI/AAAAAAAABao/-mBEhsbNdIU5QiAfjejomZHn6lPiV4oQgCK4BGAYYCw/s640/rwx.png)


- r(read) : 파일을 read, 파일의 내용을 읽을 수 있는 권한
- w(write) : 파일을 write, 파일을 바꿀 수 있는 권한
- x(excute) : 파일을 excute, 실행할 수 있는 권한


### 디렉토리 파일의 권한

- 일반 파일 과는 의미 정의가 조금 다를 수 있음
- 앞에 i-node 앞에 d 가 붙은 것 들

  - r(read) : 읽겠다, 즉 디렉토리 내부(파일들)을 볼 수 있는 권한
  - w(write) : 쓰겠다, 일반파일과 같은 맥락으로 디렉토리 내부 파일들을 변경할 수 있는 권한
  - x(excute) : 실행하겠다, 디렉토리의 기능(디렉토리 내부로 이동)을 실행할 수 있는 권한 (디렉토리 내부로 들어갈 수 있는 권한)
- 대부분의 일반 user 들이 디렉토리 안으로 들어가는 x 권한을 줘도 큰 문제가 없다
  - 예외적으로 /root/ 디렉토리 같은 것을 제외한다면..

---

## w 권한 주의 사항

- 파일에 w 권한이 없어도 디렉토리에 w 권한이 있을 수 있다
- 그런경우 파일을 불러들인뒤 수정후 :wq! 를 하면 강제로 덮어씌움이 되는 현상이 발생함
- 그리하여 보통 디렉토리를 만들면 소유자를 제외한 w 권한을 제한한다. "drwxr-xr-x"

---

## chmod 와 8진수

![img src](https://2.bp.blogspot.com/-aiokcO-E02c/XYdK5im6iLI/AAAAAAAABa8/j2oDlY-DUGc3y9cTuWGfoa-PPZG3YbJuACK4BGAYYCw/s640/rwx.png)

아래와 같이 불편하게 권한을 줄 수도 있음

```
chmod u+rx,g=rw,o-wx
```

여기서 
- u = user
- g = group
- o = other

를뜻한다


하지만 위의 8진수를 활용하면 더 편하게 직관적으로 권한을 변경할 수 있음

```
## u g o 세그룹에 모든권한 다주기

chmod 777
```

- u g o 순서를 기억하자



