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




