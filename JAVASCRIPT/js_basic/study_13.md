## 값으로서의 함수와 콜백
js 에서는 함수도 객체이다.


```js
function a(){}
```

위의 함수 a는 변수 a 에 담겨진 값이다
<br></br>

또한 함수는 객체의 값으로 포함될 수 있다
- 이것을 method 라고 한다
```js
a ={
    b:function(){
    }
};
```

함수 자체가 또다른 함수의 인자로 전달될 수 있다
- increase 와 decrease 가 cal 함수의 인자값으로 전달된다
```js
function cal(func, num){
    return func(num)
}

function increase(num){
    return num+1
}

function decrease(num){
    return num-1
}

alert(cal(increase,1))
alert(cal(decrease,2))

```


함수가 함수의 리턴값으로 사용되는경우
- 이렇게 dictionary로 선언된 변수의 value 값으로 반환하는 것도 가능
- 호출할땐 먼저 cal(mode) -> function(left,right) 순이므로 
- cal(mode)(left,right) 이러한 방식으로 호출해아한다
- dictionary 뿐만 아니라 array 로도 쓸 수 있다

```js

function cal(mode){
    var func ={
        'plus' : function(left,right){return left+right},
        'minus' : function(left,right(return left-right))
    }
    return funcs[mode];
}

alert(cal(plus)(2,1))
alert(cal(minus)(2,1))
```

array 로 각자 원소들을 function 으로 채웠다
- 첫번째 부터 세번째 식을 거쳐 60.5 가 산출됨
```js
var process = [
    function(input){ return input + 10;},
    function(input){ return input * input;},
    function(input){ return input / 2;}
];

var input = 1;
for(var i = 0; i < process.length; i++){
    input = process[i](input);
}
alert(input);
```

## 콜백 함수

내장 함수 


**array.sort(sortfunc)
sortfunc 안에는 function 이 들어감
- sort() 는 default 로 정순으로 정렬
- () 안에 function 형태로 들어갈 수 있음 **optional
- () 안의 값에 들어갈 함수를 인자로써 전달하여  내장함수의 동작을 다르게 변경할 수 있다.
- sort(b-a)를 전달함으로써 '역순으로 정렬하기'라는 기능을 수행함
- 여기서 sortNumber 는 콜백 함수 이다

```js
function sortNumber(a,b){
    return b-a
}

var numbers = [1,2,3,4,5,8,9,10]
alert(numbers.sort(sortNumber))
```


## 비동기 처리

동기 처리란
a b c 라는 태스크가 있다고 가정하자

a 가 끝나야 b, b가 끝나야 c 로가는 dependency 가 걸려있는 작업의 형태

비동기 처리는
- 실행결과를 기다리지 않아도 되는 처리 방식
- 자바스크립트에서 ajax
  - Asynchronous Javascript and XML
    - XML 은 더이상 유효하지 않음

페이스북에서 팔로워 목록을 눌렀을 때 팔로워 리스트탭이 조그맣게 현재 페이지 위에서 뜬다 (약간의 로딩이 있다)
이 과정에서 페이스북을 새로고침 하지 않았는데 그 정보를 띄운것은 AJAX 의 한 예이다.


이것이 비동기 처리의 한 예


### 비동기 처리에 있어서 콜백함수가 중요하다
시간이 오래걸리는 작업이 있을 때 이 작업이 완료된 후에 처리해야 할일을 콜백으로 지정하여 해당 작업이 끝났을 때 미리 등록한 작업을 실행하도록 할 수 있음.

- jquery 에서 비동기 처리의 한 예이다

```js
//demo.html
<!DOCTYPE html>
<html>
<head>
<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
</head>
<body>
<script type="text/javascript">
    $.get('./datasource.json.js', function(result){
        console.log(result);
    }, 'json');
</script>
</body>
```
