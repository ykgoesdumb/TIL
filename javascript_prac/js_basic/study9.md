## module

- 자바스크립트 구동되는 호스트 환경에 따라서 서로 다른 모듈화 방법이 제공되고 있다
### 호스트 환경
- 자바스크립트가 구동되는 환경
- 웹브라우저, node.js, google apps script 등등

## 모듈의 사용


- 어디까지가 javascript 이고 HTML 인지 잘 구분해주어야 한다
- script tag 가 이역할을 수행
  
```js
//greeting.js

function welcome(){
    return 'Hello World';
}

//main.html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8"/>
    <script src="greeting.js"></script>
</head>
<body>
    <script>
        alert(welcome());
    </script>
</body>
</html>

```


## node.js 에서의  모듈화

```js

//node.circle.js
var PI = Math.PI

exports.area = function (r) {
return PI * r * r;
};
  
exports.circumference = function (r) {
return 2 * PI * r;
};

//node.demo.js
var circle = require('./node.circle.js');
console.log('The area of a circle of radius 4 is ' + circle.area(4));

```

## 라이브러리 이용

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://code.jquery.com/jquery-1.11.0.min.js"></script>
</head>
<body>
    <ul id="list">
        <li>empty</li>
        <li>empty</li>
        <li>empty</li>
        <li>empty</li>
    </ul>
    <input id="execute_btn" type="button" value="execute" />
    <script type="text/javascript">
     $('#execute_btn').click(function(){
        $('#list li').text('coding everybody');
     })
    </script>
</body>
</html>
```
