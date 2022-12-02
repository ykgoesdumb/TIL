## var let const

var는 변수 선언 방식에 있어서 단점이 있음
  
동일한 변수를 선언했음에도 불구하고 다른값이 출력
```js
var name = 'bathingape'
    console.log(name) // bathingape

var name = 'javascript'
    console.log(name) // javascript
```

## let
  - let 과 const 의 가장 큰 차이점은 immutable 이다
  - let은 아래와같이 재할당이 가능하다

```js
    let name = 'bathingape'
    console.log(name) // bathingape

    let name = 'javascript'
    console.log(name) 
    // Uncaught SyntaxError: Identifier 'name' has already been declared

    name = 'react'
    console.log(name) //react
```
## const
- 변수 재선언, 변수 재할당 모두 불가능 하다

```js
    const name = 'bathingape'
    console.log(name) // bathingape

    const name = 'javascript'
    console.log(name) 
    // Uncaught SyntaxError: Identifier 'name' has already been declared

    name = 'react'
    console.log(name) 
    //Uncaught TypeError: Assignment to constant variable.
```


## 변수 생성 logic

선언 >> 초기화 >> 할당

- var 는 선언단계와 초기화 단계 한번에 이루어짐
- let 은 분리해서 이루어짐

```js
// 스코프의 선두에서 선언 단계와 초기화 단계가 실행된다.
// 따라서 변수 선언문 이전에 변수를 참조할 수 있다.

console.log(foo); // undefined
var foo;
console.log(foo); // undefined

foo = 1; // 할당문에서 할당 단계가 실행된다.
console.log(foo); // 1
```

```js
// 스코프의 선두에서 선언 단계가 실행된다.
// 아직 변수가 초기화(메모리 공간 확보와 undefined로 초기화)되지 않았다.
// 따라서 변수 선언문 이전에 변수를 참조할 수 없다.

console.log(foo); // ReferenceError: foo is not defined

let foo; // 변수 선언문에서 초기화 단계가 실행된다.
console.log(foo); // undefined

foo = 1; // 할당문에서 할당 단계가 실행된다.
console.log(foo); // 1
```

## solution

- 변수 선언엔 기본적으로 const
- 재할당 필요한 경우 let