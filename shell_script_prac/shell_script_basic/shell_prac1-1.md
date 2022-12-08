## 쉘 스크립트 만들기


- #!/bin/bash
- 로 시작한다

### 실행 방법
- myshell.sh 를 생성했다고 가정해보자

```sh
#!/bin/bash

# 파일명 : myshell.sh

echo "hello world"
```


- 방법1
```sh
sh myshell.sh
```

- 방법2
- 실행 권한을 주고 직접 셸 스크립트를 실행하는 방식
```sh
chmod +x myshell.sh
./myshell.sh
```

- 방법3
- 파일 실행 없이 프롬프트에서 바로 실행하기
```
echo "hello world"
```
---

## 변수 선언

```sh

#!/bin/bash

language="Korean"
echo " I can speak $language"

```

### 변수로 디렉토리 생성

```sh
#!/bin/bash

language="Korean English Japan"
mkdir $language
```
- 결과로 korean english japan 디렉토리가 개별적으로 생성됨

---

## 함수

```sh
#!/bin/bash

function print() {

    echo $1
}

print "I can speak Korean"
```

- 함수를 호출할때 print 명령문 형식으로 호출한다
- 소괄호 없음

### 전역변수

```sh
#!/bin/bash

language='Korean'

function print(){
    echo 'I can speack $language'
}

print
```


### 지역변수

```sh
#!/bin/bash

language="Korean"

funciton learn(){

    local learn_language="English"
    echo "I am learning $learn_language"
}

function print() {
    echo "I can speak $language"
}

learn
print $language
print $learn_language
```
결과
```
I am learning English
I can speak Korean
I can speak
```

## 위치 매개변수

- 스크립트 수행시 함께 넘어오는 parameter

|매개변수|설명|
|--|--|
|$0|실행된 스크립트 이름|
|$1| $1 $2 $3... ${10} 파라미터 순서대로 부여 10  부터 {} 로 감싸줘야함|
|$*| 전체 인자값|
|$@| 전체 인자 값($*는 동일하지만 쌍따옴표로 변수를 감싸면 다른 결과|
|$#| 매개변수의 총 개수|


### $ * 와  "$*" 의 차이점
```sh

#!/bin/bash
### 파일명 mylanguage.sh

for language in $*
do
    echo "I can speak language"
done
```
위와 같은 스크립트를 인자값과 함께 실행을 시켜보자
- 복합적으로 " " 를 붙인 인자도 전달해 보았다

```sh
sh mylanguage.sh Korean English "Japanese Chinese"

I can speak Korean
I can speak English
I can speak Japanese
I can speak Chinese
```
각각 개별로 인식한다 


그렇다면 "$*" 는?
```sh
#!/bin/bash
### 파일명 mylanguage2.sh

for language in "$*"
do
    echo "I can speak language"
done

---
sh mylanguage2.sh Korean English "Japanese Chinese"

I can speak Korean English "Japanese Chinese"
```
히나의 문자열로 인식한다


그렇다면 "$@" 은?

```sh
#!/bin/bash
### 파일명 mylanguage3.sh

for language in "$@"
do
    echo "I can speak language"
done

---

sh mylanguage3.sh Korean English "Japanese Chinese"

I can speak Korean
I can speak English
I can speak "Japanese Chinese"
```
큰 따옴표 사이의 문자열을 하나의 매개변수로 인식
