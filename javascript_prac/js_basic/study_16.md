## arguments

arguments 는 객체이다
- 사용방법이 배열과 비슷하다 (유사배열)


### 매개변수와 인자의 차이

- 예시로 알아보자

```js
function sum(args){     // args 가 '매개변수'
    return 1+1
}

sum(1);                // 1이 '인자'
```

다음의 예시는 정의한 함수에 매개변수가 존재하지 않고 호출할때 인자값은 존재하는 예시
- argument 의 성질을 이해하자
- js 는 관대한 언어이다 매개변수의 갯수와 인자의 갯수가 같지 않아도 에러를 내지 않음
- 그 쿨한 python 에서도 매개변수의 갯수는 지켜야 했다.
  

```js
function sum(){
    var i, _sum = 0;    
    for(i = 0; i < arguments.length; i++){
        document.write(i+' : '+arguments[i]+'<br />');
        _sum += arguments[i];
    }   
    return _sum;
}
document.write('result : ' + sum(1,2,3,4));
```
- arguments 안엔 사용자가 전달한 인자값을 가진 일종의 배열이다
  - 여기에선 (1,2,3,4)
  - arguments[i] 로 인자의 배열의 위치를 나타낼 수 있음
  - arguments[2] = 2

- arguments 는 유사배열이지 배열은 아니다 (객체의 인스턴스이다)

```
0 : 1
1 : 2
2 : 3
3 : 4
result : 10
```

## 매개변수의 수

```js
function zero(){
    console.log)
    'zero.length', zero.length,
    'arguments', arguments.length
    );
}

function one(arg1){
    console.log
        'zero.length', zero.length,
        'arugments', arguments.length
    );
}

function two(arg1, arg2){
    console.log(
        'two.length', two.length,
        'arguments', arguments.length
    );
}

zero();                 //zero.length 0 arguments 0        (매개변수 0 인자 0)
one('val1', 'val2');    //one.length 1 arguments 2
two('val1');            //two.length 2 arguments 1
```




