## 함수의 호출

```js
function sum(arg1, arg2){
    return arg1+arg2;
}

sum(1,2);

//apply 라고 하는 sum 함수에 담긴 method 에 접근하기
sum.apply(null, [1,2]);

// 결과는 같다
```


## apply 를 그럼 왜 사용할까?

```js
o1 = {val1:1, val2:2, val3:3}
o2 = {v1:10, v2:50, v3:100, v4:25}
function sum(){
    var _sum = 0;
    for(name in this){
        _sum += this[name];
    }
    return _sum;
}
alert(sum.apply(o1)) // 6
alert(sum.apply(o2)) // 185
```

this 는 호출할때 정해진다 sum() 을 정의하는 단계에서 정해지지 않음
- sum 이 합계를 내는 대상은 o1 이다
- sum.apply(o1)  -> o1.sum


```js
o1.sum = sum;
alert(o1.sum());
delete o1.sum();
```


- 일반적인 객체지향에서는 하나의 객체에 소속된 함수는  그 객체의 소유물이 됨
- js 에서는 함수는 독립적인 객체로서 존재하고 apply 나 메소드를 통해서 다른 객체의 소유물인 것처럼 실행할 수있다.

