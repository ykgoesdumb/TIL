## 숫자와 문자
---

자바스크립트 에서 ' 나 " 붙지 않는 숫자는 숫자로 인식

```javascript
alert(1+1);
alert(1.2 + 1.3);
alert(2 * 5);
alert(6/2);
```


### 복잡한 연산

```javascript
Math.pow(3,2);
Math.round(10.6);
Math.ceil(10.2);
Math.floor(10.6);
Math.sqrt(9);
Math.random();    //0~ 1.0까지의 랜덤한 숫자
```

## 문자
```javascript
alert("hello world");

alert(typeof true); typeof 는 자료형을 출력해준다 //python 의 type(true)

alert('kyle's world');      //에러를 반환한다
alert('kyle\'s world');     //백슬래쉬를 사용한다

//문자의 덧셈 길이
alert("coding" + "everybody")
alert("coding everybody".length) //숫자를 반환한다
