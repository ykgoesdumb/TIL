## 클로저


클로저란 : 내부함수가 외부함수의 context 에 접근할 수 있는 것을 가르킨다.


내부함수

```js
function outter(){
    function inner(){
        var title = 'hello world';
        alert(title);
    }
    inner();
}
outter();
```


내부함수는 외부함수의 지역변수를 사용할 수 있다.
- 아래의 코드는 'hihi'를 출력한다

```js
function outter{
    var a = 'hihi';
    function inner{
        alert(a);
    }
    inner();
}
outter();
```

외부함수는 외부함수의 지역변수를 사용하는 내부함수가 소멸될 때까지 소멸되지 않는 특성이 있다.

```js
function outter(){
    var title = 'coding everybody';  
    return function(){        
        alert(title);
    }
}
inner = outter();
inner();
```

- outter 함수의 실행은 inner=outter(); 에서 끝났지만
- 지역변수를 사용하는 함수 inner가 소멸되지 않았기 때문에 outter 함수는 소멸되지 않음
- 결과는 동일하게 coding everybody 이다


<br></br>
동일한 외부함수에서 만들어진 내부한수나 메소드는 외부함수의 지역변수를 공유한다

- 함수의 리턴값으로 객체를 반환하는 함수
- 그 객체안에 메서드가 두개 있다고 가정해보자

```js
function factory_movie(title){
    return {
        get_title : function (){
            return title;
        },
        set_title : function(_title){
            title = _title
        }
    }
}

ghost = factory_movie('Ghost in the shell');
matrix = factory_movie('Matrix');
 
alert(ghost.get_title());
alert(matrix.get_title());
 
ghost.set_title('공각기동대');
 
alert(ghost.get_title());
alert(matrix.get_title());

```

- ghost.set_title 로 ghost 에다가만 이름을 변경하였다
- ghost.get_title() 하면  '공각기동대'로 변경되었다
- 그래도 같은 외부함수에서 만들어진 matrix 도 그럼 title 이 '공각기동대'로 바뀌었을까??
- 결과는 아니다.


### 외부함수가 실행될 때마다 새로운 지역변수를 포함하는 클로저가 생성된다


<br></br>

### 클로저 성질의 예시


보통 이해하는 for 문의 logic 이겠지만 원하는 결과값을 주지 못한다

```js
var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(){
        return i;
    }
}
for(var index in arr) {
    console.log(arr[index]());
}
```
결과는 이러하다

```
5
5
5
5
5
```

- 함수는 함수내부에 지역변수가있으면 그걸 사용하고 없다면 외부에서 가장 최근 값을 사용한다
- 위의 함수에서 arr[i] 와 function() { return i;} 의 값이 다른곳을 가르키고 있음
- 다시말해 for 문 i 와 function i 가 다름
- 뒤에 호출한 for 문은 i 의 최신값인 5를 다섯번 호출하는 것
- 위의 두개의 for 문에 i = 10; 을 선언해보자

```js
var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(){
        return i;
    }
}
i = 10;
for(var index in arr) {
    console.log(arr[index]());
}

// 결과

10
10
10
10
10
```
for 문 뒤에 i 를 10 으로 선언하였고 그 뒤에 나오는 for 문이 i

최신상태인 10 을 5번 출력한 것



### 제대로 출력한 예시
```js
var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(id){  
        return function(){
            return id;
        }
    }(i);   

```
1. (i) 맨 마지막 줄에 i값을 인자로 넣어주고
2. function(id) id 에 인자값 i 가 들어온다
3. return id 에서 들어온 인자값을 함수내의 지역변수처럼 사용할 수 있게 내부함수를 만들어 들어온 인자값을 가르킴


