## 조건문
js 에서의 조건문 문법은

if로 시작하고 if뒤의 괄호에 조건이 오고, 조건이 될 수 있는 값은 Boolean 이다. 

```js
//그대로 출력
if(true){
    alert('result : true')
}

//출력하지 않음
if(false){
    alert('result : true');
}

//괄호안의 값이 false니 2를 출력한다

if(false){
    alert(1);
} else {
    alert(2);
}

//else if
//다음 값은 2를 출력한다

if(false){
    alert(1);
} else if(true){
    alert(2);
} else if(true){
    alert(3);
} else {
    alert(4);
}

//다음 값은 4를 출력한다


if(false){
    alert(1);
} else if(false){
    alert(2);
} else if(false){
    alert(3);
} else {
    alert(4);
}

//else if는 순서대로 검증되고  모든 else if 조건들이 거짓일떼 else 값을 반환한다
```

## 논리 연산자

- &&   (and 연산자)
- ||   (or 연산자)
- 두개를 복합적을 사용 가능하다



아래의 경우는 밑의 세가지 아이디중 하나를 사용하고 패스워드가 111111 일때만 참을 반환한다
```js
id = prompt('아이디를 입력해주세요.');
password = prompt('비밀번호를 입력해주세요.');
if((id==='kylekim' || id==='leohs' || id==='soraaoi') && password==='111111'){
    alert('인증 했습니다.');
} else {
    alert('인증에 실패 했습니다.');
}
```

### not 연산자

- ! 는 부정을 나타낸다
- 조건문에서 ! 와 && 이 합쳐진 경우를 살펴보자
- 양측이 참이될때만 반환한다 (!false && !false 이거나 true && true 이여야한다)

```js
//아래의 값은 4 를 반환한다

if(!true && !true){
    alert(1);
}
if(!false && !true){
    alert(2);
}
if(!true && !false){
    alert(3);
}
if(!false && !false){
    alert(4);
}
```

## boolean 의 대체재

- 01
- 0 은 false 1 은 true 로 간주한다

```js
// 2를 출력
if(0){
    alert(1)
}
if(1){
    alert(2)
}
```

- ' '
- ' ' 는 false 로 간주된다

```js
// you 를 출력

if(''){
    alert('hey')
}else{
    alert('you')}
```

- 값이 할당되지 않은 변수
- var a;

```js
var a;
if(!a){
    alert('값이 할당되지 않은 변수'); 
}
```

- null
- NaN
- undefined

```js
if(!undefined){
    alert('undefined');
}

if(!null){
    alert('null');
}
if(!NaN){
    alert('NaN');
}
```


