## gpg key 

- github 에 gpg key 를 등록해 git-secret 이용한 것을 기록한다


- 우선 같은 이메일로 여러 키가 생성이 되어있어서 삭제조치 하였다

```
gpg --list-secret-keys
```

```
sec   ed25519 2023-04-17 [SC] [expires: 2025-04-16]
      2894BCBA28B2433CEFE135091C3BCD521A9441A3
uid           [ultimate] Yongkyun Kim <kylekim1223@gmail.com>
ssb   cv25519 2023-04-17 [E] [expires: 2025-04-16]
```

```
gpg --delete-secret-key 
```

```
B795A4CB82C9E043D8B6D4A7237F86931D2512A6
gpg (GnuPG) 2.3.8; Copyright (C) 2021 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


sec  ed25519/237F86931D2512A6 2023-04-17 Yongkyun Kim <kylekim1223@gmail.com>

Delete this key from the keyring? (y/N) y
This is a secret key! - really delete? (y/N) y
```


## 개인 GPG 생성

- 생성시 비번 설정 안하는게 편리
- 2년 마다 gpg key를 갱신할 수 있도록 expirese 설정 추천 (--generate-key 사용시 자동 설정)


```
gpg --generate-key
```

## 생성된 키 repository 에 등록

```
git secret tell <email>
```

## 확인

```
git secret whoknows

git secret hide

git secret reveal -f
```
