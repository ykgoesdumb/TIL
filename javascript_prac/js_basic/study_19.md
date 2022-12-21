## 전역 객체

```js
function func(){
    alert('Hello?');    
}
func();
window.func();
```
- func() 와 window.func() 둘다 실행된다


모든 전역변수는 window 객체의 property 이다 
- 객체를 명시하지 않으면 암시적으로 window 의 property 로 간주
  
```js

var o = {'func':function(){
    alert('Hello?');
}}
o.func();
window.o.func();
```

- 역시 둘다 실행된다

o.func() 가 실행되는걸로보아
- 자바스크립트에서 모든 객체는 전역객체의 프로퍼티임을 알 수 있다
---
- 웹 브라우저에서 전역객체는 window 
- node.js 에서는 alert
---

## this 
- 함수 내에서 함수 호출 맥락을 의미함
- 함수를 어떻게 호출하느냐에 따라 this가 가리키는 대상이 달라짐
- 함수와 객체를 실질적으로 연결시켜주는  연결점 역할


함수를 변수 없이 호출하면 window 의 method 이다.

<br>

- 여기에서 this 는 전역객체인 window와 같다

```js
function func(){
    if(window === this){
        document.write("window === this")
    }
}
func();

// 결과
window === this
```


- 객체의 소속인 method의 this 는 그 객체를 가르킨다.


```js
var = o {
    func : function(){
        if(o === this){
            document.write("o === this");
        }
    }
}
o.func();

//결과

o === this
```

- 함수로 호출했을때와 생성자를 호출했을 때의 차이

```js
var funcThis = null; 
 
function Func(){
    funcThis = this;
}
var o1 = Func();
if(funcThis === window){
    document.write('window <br />');
}
 
var o2 = new Func();
if(funcThis === o2){
    document.write('o2 <br />');
}
```
- new 를 이용하여 만들면 새로운 객체를 만들고 this 는 그 객체를 가르킨다

<br>
<br>

생성자의 호출이 모두 끝난 시점부터 변수 를 참조할 수 있다 그전에 먼저 참조할 수 없다

```js
function Func(){
    document.write(o);
}
var o = new Func();

//result

undefined
```
- 이처럼 생성자의 호출이 완료되지 않은 시점에서 o 를 참조 하였기 때문에 undefined 가 나온다



## 리터럴

- 좀더 간편한 형식으로 객체 함수 배열 등을 생성하는 방식
- 간결성과 편리성
- 객체 방식으로 동일하게 구현이 가능하다
- 리터럴 방식은 자바스크립트 엔진에 의해서 객체방식으로 자동변환되어 실행됨


```js
//함수 리터럴
function sum(x,y){return x+y;}
sum(1,2)
// result
3

//객체 방식으로 동일한 구현
var sum2 = new Func('x','y', 'return x+y;');
sum2(1,2)
//result
3


//객체 리터럴
var o = '~~~'
//객체 방식으로 동일 구현
var o = new String(~~~)

//배열 리터럴
var a = [1,2,3]
//객체 방식 동일 구현

var a = new Array(1,2,3)
