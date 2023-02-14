## 매개변수 확장
스크립트를 짜다보면 변수와 텍스트가 구분안갈때 많음

- ${변수}


### 변수 초기화 하기위한 확장 변경자
- var 는 변수 text 는 문자열

|확장자|설명|
|--|--|
| ${var-text}| var 가 설정되지 않은경우 text로 var 를 치환|
${var:-text}| var 가 설정되지 않았거나 Null 값인 경우 text 로 var 치환|
${var=text}| var 가 설정되지 않을 때 text를 var 에 '저장'하고 var 치환 |
${var:=text}| var 가 설정되지 않았거나 Null로 설정된 경우 text를 var 에 저장하고 var 치환
${var+text}| var 가 설정된 경우 text로 치환
${var:+text}| var 가 설정되고 Null 이외의 값으로 설정된 경우 문자열로 변수 치환
${var?error_message}| var 가 설정되었을때 var의 값을 사용하며, 설정되지 않은 경우 표준 오류 출력으로 에러 메시지를 출력
${var:?error_message}| var Null 이외의 값으로 설정된 경우 var 의 값을 사용, 설정 되지 않았거나 Null 인경우 에러메시지 출력후 셀 종료
${var:starting_point}| var 값이 문자열일 경우 starting_point 부터 문자열 끝까지 출력
${var:starting_point:length}| var 값이 문자열일 경우 starting_point 부터 length 까지 출력



### 예시 1

- "" 값도 Null 값으로 인식한다
- 아래 예제는 null 값이므로 :- 의 치환조건을 만족한다

```sh
os_type =""
echo $(os_type:-ubuntu)
```

### 예시 2

- :- 옵션은 값을 저장하지 않는다



```sh
os_type=""
echo $(os_type:-redhat)

> redhat

echo $os_type

>
```
- := 옵션은 값을 저장한다

```sh
os_type=""
echo $(os_type:=redhat)

> redhat

echo $os_type

> redhat
```


### 예시 3
- + 는 변수에 어떠한게 이미 선언이 되어있다면 text 로 초기화 한다 (null 포함)
- :+ 는 변수에 null 의외의 값이 선언되어야만 text 로 초기화 한다 

### 예시 4
- ?error_message 일경우 변수값이 null일 경우 error 로 인식하지 않는다
- ?:error_message 일경우 변수값이 null인 경우 error 로 인식하고 셀을 종료함
- 두 옵션다 변수값이 선언이 안된경우 에러메세지를 띄우고 종료함 


### 예시 5
```sh

os_type="ubuntu debian redhat fedora"
echo $(os_type:14)

> redhat fedora

echo $(os_type:14:6)

> redhat

echo $(os_type:(-6))

> debian

echo $(os_type:(-6):2)

> de

echo $(os_type:(-6):-2)

> debi
