## Array
python 의 list 와 같다

python list 와 js array 를 비교한 글
- https://agvim.wordpress.com/2017/08/22/python-list-vs-javascript-array/

자바스크립트에서 []를 typeof 키워드로 확인하면 []가 객체 타입임을 알 수 있다. 배열인지 확인하려면 Array.isArray를 사용해야 한다. []는 Array이면서 객체이다.


```js
typeof([])
// object 라고 출력한다
Array.isArray([])
//true
```


```js
var member = ['kylekim', 'jwkim', 'jonnydepp']

alert(member[0]);
alert(member[1]);

// array 의 length 계산

var arr = [1,2,3,4,5];
alert(arr.length);
```

## 배열에 추가하기

```js
//배열의 끝에 원소 추가     복수의 원소 추가 가능
var li =[1,2,3,4,5]
li.push(6);
alert(li);

//복수의 원소 추가
li = li.concat([7,8])
alert(li)

//시작점에 추가
li = li.unshift(0)

// [1] 부터 시작해서 [2]개의 원소들을 제거하고 [3] 에 들어간 숫자를 [1] 뒤에 넣는다
// splice
var a = [1,2,3,4,5];
a.splice(2,3,3);
alert(a);


//결과는 2 [1] 뒤로 3개의 숫자 [2] (3,4,5)를 대체하고 그 자리에 3 [3]을 넣는다
//1,2,3

```

## 배열에서 제거하기
```js
// 첫번째 원소 제거하기

var li = [1,2,3,4,5];
li.shift();
alert(li);


// 마지막 원소 제거하기
li.pop();
alert(li);
```

## 정렬
```js
var li =['a','c','y','r']
li.sort();
alert(li);

//역순

li.reverse();
alert(li);
```

