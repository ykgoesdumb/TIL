## 전역변수

예제를 통해 전역변수의 선언을 알아보자

- 먼저 상단에 변수를 설정한다
  - 함수 밖에서 변수를 선언하면 그 변수는 전역변수
- 함수안에서 변수를 재설정하고 함수를 호출해본다
- 결과 값은 '함수안 local' 과 '함수밖 global'

```js
var vscope = 'global'

function fscope(){
    var vscope = 'local';
    alert('함수안' + vscope);
}

fscope();
alert('함수밖' + vscope) 
```

하지만 아래의 코드는 결과 값이 다르다
- 함수를 호출하였음에도 불구하고 결과값이 
- 함수안 local' 과 '함수밖 local'
- var 를 이용하여 선언하지 않았기 때문

```js
var vscope = 'global'

function fscope(){
    vscope = 'local';
    alert('함수안' + vscope);
}

fscope();
alert('함수밖' + vscope)  
```

전역변수를 되도록이면 사용하지 않고 쓸때는 그것의 쓰임과 필요성을 명백히 알필요가 있음

## 지역변수
- 함수 안에 변수를 선언(지역변수)해보고 그 변수를 가지고 for 문을 돌려보자
  
```js
function a(){
    var i = 0
}


for(i = 0, i<5, i++){
    a();
    document.write(i)
}

//012345
```

- 정상적으로 for 문 출력된다


다음은 var 변수로 선언하지 않고 전역변수로 선언해보는 예

```js
function a(){
    i = 0
}


for(i = 0, i<5, i++){
    a();
    document.write(i)
}

// 무한루프이다
```

for 문을 돌려도 계속 i=0 으로 전역변수가 설정되었기 때문에 무한루프에 빠진다

## 불가피하게 전역변수를 써야되는 경우

- 전역변수를 그대로 선언하기보다 전역변수의 속성으로 관리한다
- MYAPP 의 속성 에 calculator라는 객체를 또 생성해 값을 선언해준다

```js
MYAPP = {}
MYAPP.calculator = {
    'left' : null,
    'right' : null
}
 
MYAPP.calculator.left = 10;
MYAPP.calculator.right = 20;
function sum(){
    return MYAPP.calculator.left + MYAPP.calculator.right;
}
document.write(sum());
```


## 익명함수
위의 예시를 전역변수를 선언하지 않고 목적을 달성하려면 이렇게 익명함수를 쓸 수 있다
- 자바스크립트를 모듈화하는 전형적인 방법이다

```js
(function(){
    var MYAPP = {}
    MYAPP.calculator = {
        'left' : null,
        'right' : null
    }
    MYAPP.coordinate = {
        'left' : null,
        'right' : null
    }
    MYAPP.calculator.left = 10;
    MYAPP.calculator.right = 20;
    function sum(){
        return MYAPP.calculator.left + MYAPP.calculator.right;
    }
    document.write(sum());
}())
```



## 자바스크립트의 유효범위의 대상

자바스크립트의 유효범위의 대상은 함수이다 (function)
- js에서 function 이 아닌 for 문 이나 조건문 안의 {} 에서 선언된 변수는 지역변수가 아닌 전역변수로 인식된다
- 타 언어들은(예를들어 java) {} 에대한 유효범위를 제공한다

먼저 자바스크립트 함수가 아닌 for 문안에 지역변수를 호출했다고 가정해보자

```js

for(var i = 0; i < 1; i++){
    var name = 'coding everybody';
}
alert(name);

```

그대로 name 이 출력된다
- 함수가 아닌 for 문에서 선언된 변수이기 때문에 전역변수로 인식되었기 때문이다


같은 logic 을 java 에서 돌려본다고 가정해보자

```java
for(int i = 0; i < 10; i++){
    String name = "egoing";
}
System.out.println(name);
```

위의 코드는 에러가 난다 java 에서는 for 문이던 함수던 중괄호{} 가 유효범위 이기 때문에 {} 밖에서 설정된 변수들은 인식하지 못함


## 정적 유효범위 (static scoping)

자바스크립트는 함수가 선언시점에서의 유효범위를 가진다

```js
var i = 5;
 
function a(){
    var i = 10;
    b();
}
 
function b(){
    document.write(i);
}
 
a();
```


