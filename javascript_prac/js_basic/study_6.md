## function

python 의 def 와 동일하다

```js
function 함수명( [인자...[,인자]] ){
   코드
   return 반환값
}

```

```js
function numbering(){
    i = 0;
    while(i<10){
        document.write(i);
        i += 1;
    }
}
```
## return

function 에서 returen 은 return 뒤에 따라오는 값을 함수의 결과로 반환
<b>*동시에 함수를 종료시킨다*</b>

```js
function get_member(){
    return 'kylekim';
    return 'chriskim';
    return 'paulkim';
}
alert(get_member());
```
위의 코드는 kylekim 만 반환한다 (최초의 return이 함수를 종료시키기 때문)

## argument

인자

```js
function get_arguments(arg1, arg2){
    return arg1 + arg2
}
 
alert(get_arguments(10, 20));
alert(get_arguments(20, 30));
```


자바스크립트는 함수를 var 를 이용하여 정의할 수 도 있다.
```js
var numbering = function (){
    i = 0;
    while(i < 10){
        document.write(i);
        i += 1;
    }   
}
numbering();
```

