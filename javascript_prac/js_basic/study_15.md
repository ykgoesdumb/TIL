## value  & reference

자바스크립트는 포인터의 개념이 없다

포인터란?
- 다른변수, 혹은 다른 변수의 메모리 공간 주소를 가리키는 변수 
- 포인터가 가르키는 값을 가져오는 것을 '역참조'라 함
- http://www.tcpschool.com/c/c_pointer_intro




아래는 C 언어에서  변수의 선언과 포인터의 선언이다
```C
int n = 100;   // 변수의 선언

int *ptr = &n; // 포인터의 선언
```

js 타언어와 달리 참조하는 방법도 다르다
- js 에서 레퍼런스는 공유된 값을 가리킨다
- 10개의 레퍼런스가 있다면 이들은 공유된 단일 값을 개별적으로 참조함


즉, 값 또는 레퍼런스의 할당 및 전달을 제어하는 구문 암시가 전혀 없다.


###  원시타입
어떠한 원시타입이 변수에 할당된다면, 변수를 원시타입을 가진 변수로 인식

```js
var x = 10;
var y = 'abc';
var z = null;
```

변수들을 다른 변수에 =이라는 키워드를 이용하여 할당할 때, 새로운 변수에 값을 복사(Copy) 하게 된다. 이 변수들은 값에 의해 복사.


단순값
- null, undefined, string, number, boolean, symbol
- 값 - 복사 방식으로 할당/전달됨

```js
var a = 2;
var b = a;
b++;

a; // 2
b; // 3
```

합성값
- 객체, 함수, 배열
- 레퍼런스 사본을 생성하고 할당/전달 된다


원시타입이 아닌 값(합성값)이 할당된 변수들 그 값으로 향하는 reference 를 갖게 됨
- 이는 메모리에서 객체의 위치를 가리키고 있음
- 변수는 실제로 값을 가지고 있지 않음
- 예를들어 arr = [] 를 작성할 경우 메모리 내부에 배열을 만든것이고 , 변수 arr 이 갖는 것은 그 배열이 위치한 주소

```js
//1
var arr = [];

//2
arr.push(1);
```
위의 명령어를 메모리가 저장하는 방식은 아래와 같은 표로 나타낼 수 있다.

1.
|Variables|Values|Addresses|Objects|
|--|--|--|--|
|arr|<#001>|#001|[]|

2.
|Variables|Values|Addresses|Objects|
|--|--|--|--|
|arr|<#001>|#001|[1]|

- arr 이 가진 주소는 정적이다
- 변수의 값이 바뀌는 것이 아닌 메모리속의 배열값만 바뀌는 것
- push 를 실항할때 메모리속의 arr 위치로 가고 거기에 저장된 정보를 이용하여 작업을 수행하는 것


### 참조로 할당하기

합성값이 다른 변수로 복사될 때, 그 값의 주소는 실제로 복사된다

```js
var reference = [1];
var refCopy = reference;
```
|Variables|Values|Addresses|Objects|
|--|--|--|--|
|reference|<#001>|#001|[1]|
|refcopy|<#001>|||

각각의 변수 reference, refcopy 는 같은 배열로 향하는 레퍼런스를 갖는다

```js
reference.push(2);
console.log(reference, refCopy); // -> [1, 2], [1, 2]
```
- 같은 레퍼런스 이므로 reference 를 변경하여도 refCopy 도 변경된걸 알 수 있다


### 참조 재할당하기

참조 값을 재할당 하는 것은 오래된 참조를 대체함

```js
var obj = { first: 'reference' };
```
|Variables|Values|Addresses|Objects|
|--|--|--|--|
|obj|<#234>|#234|{ first: 'reference' }|

이렇게 입력된것을 재할당 하면 메모리는 어떻게 동작할까?
```js
var obj = { first: 'reference' };
obj = { second: 'ref2' }
```

|Variables|Values|Addresses|Objects|
|--|--|--|--|
|obj|<#678>|#234|{ first: 'reference' }|
|||#678| { second: 'ref2' }|

이렇게 메모리가 동작한다 

첫번째 등록한 객체는 { first: 'reference' } 메모리상에 표기는 된다 남아있는 객체를 가리키는 참조가 남아있지 않다면 Garbage Collection 의 대상이 된다.


<br></br>


## 예시

```js
var c = [1, 2, 3];
var d = c;
d.push(4); // 실제 공유한 배열 값이 바뀌어 공유하던 c, d의 값이 바뀜

c; // [1, 2, 3, 4]
d; // [1, 2, 3, 4]

var e = [1, 2, 3];
var f = e;

e; // [1, 2, 3]
f; // [1, 2, 3]

f = [4, 5, 6];

e; // [1, 2, 3]
f; // [4, 5, 6]
```
- 합성값으로 c [1,2,3]에서 push로 공유된 [1,2,3]이 바뀌어서 c,d 바뀜
- f,e 는 후에 새로운 레퍼런스를 할당했기때문에 참조값다름


밑의 a 의 결과 값을 보자
```js
function test(x) {
    x.push(4);
    x; 

    x = [4, 5, 6];
    x.push(7);
    x;
}

var a = [1, 2, 3];

test(a);

a; // [1, 2, 3, 4]
```

```js
function test(x) {
    x.push(4);
    x;

    x.length = 0; // 기존 배열을 즉시 비움
    x.push(4, 5, 6, 7);
    x;
}

var a = [1, 2, 3];

test(a);

a; // [4, 5, 6, 7]
```

