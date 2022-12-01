## 반복문
js 의 반복문 문법은 이러하다
```js
while (조건){
    반복 실행할 코드
}
```

document.write 는 웹브라우저에서만 동작
  
node.js 콘솔과 같은 환경에서 실습한다면 console.log와 같은 메소드를 대신 사용
- 개발자 도구에서는 console.log 를 사용한다

```js
while(true){
    document.write('coding everybody <br />')
}
```

괄호 안의 조건이 참(true)이면 중괄호 안의 코드를 반복적으로 실행한다

```js
var i = 0;
// 종료조건으로 i의 값이 10보다 작다면 true, 같거나 크다면 false가 된다.
while(i < 10){
    // 반복이 실행될 때마다 coding everybody <br />이 출력된다. <br /> 줄바꿈을 의미하는 HTML 태그
    document.write('coding everybody <br />');
    // i의 값이 1씩 증가한다.
    i++
}

```

## for 문

for 문의 형식은 아래와 같다

```
for(초기화; 반복조건; 반복이 될 때마다 실행되는 코드){
    반복해서 실행될 코드
}
```

```js
for(var i = 0; i<10; i++){
    document.write('this is version' + i +'</br>');
}

```


### break

base 로직은 비슷하다
- break 는 조건이 충족시 반복문을 중단
- continues 는 조건 충족시 반복해서 실행할 코드를 건너뛴다

```js
for(var i = 0; i < 10; i++){
    if(i === 5) {
        break;
    }
    document.write('coding everybody'+i+'<br />');
}
```

### continue

```js
for(var i= 0; i < 10, i++ ){
    if(i===5){
        continue;
    }
    document.write('coding is fun');
}
```
