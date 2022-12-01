## 변수

자바스크립트에서는 변수는 var 로 시작한다

```javascript
var a = 1;
alert(a+1);  //2
```

## 줄바꿈과 여백
 
 세미콜론은 하나의 명령의 단위를 나타냄
```js
var a = 1 alert(a);  //이런식으로 하게 된다면 명령의 단위를 컴퓨터가 파악 하기 힘듬
var a = 1; alert(a); //이런식으로 해줘야함
```

## 연산자

기초적인 개념은 python 과 비슷하다
```js
alert(1==1) //true
alert(1!=1) //false
```
하지만 같은 문자지만 datatype 이 달라도 참을 반환한다
```js
alert(1 =='1')  //true
```

datatype 까지 정확하게 일치하는 연산자는 === 를 써주어야한다
js 에서는 ===를 쓰는것을 권장한다고 한다

```js
alert(1 =='1')  //true
alert(1 === '1')  //false
```

### null, undefined, NaN
- null 과 undefined 는 값이 없다는 의미의 데이터형이다
- NaN 은 0/0 과 같은 연산의 결과로 만들어지는 특수한 데이터 형인데 숫자가 아니라는 뜻

```js
alert(null == undefined);       //true
alert(null === undefined);      //false
alert(true == 1);               //true
alert(true === 1);              //false
alert(true == '1');             //true
alert(true === '1');            //false
 
alert(0 === -0);                //true
alert(NaN === NaN);             //false
```

== 와  === 처럼 != 와 !== 은 같은 관계이다
- !== 는 정확히 datatype 까지 다른지를 검증한다

