## HTML 에 JS  load

inline
- 태그에 직접 기술
- 정보와 제어가 섞여서 가치가 크지 않다

```html

<!DOCTYPE html>
<html>
<body>
    <input type="button" onclick="alert('Hello world')" value="Hello world" />
</body>
</html>
```

script
- <script></script>
- html 과 js 분리 가능

```HTML
<!DOCTYPE html>
<html>
<body>
    <input type="button" id="hw" value="Hello world" />
    <script type="text/javascript">
        var hw = document.getElementById('hw');
        hw.addEventListener('click', function(){
            alert('Hello world');
        })
    </script>
</body>
</html>
```

js 별도의 파일로 분리
- js 의 재활용성 높일 수 있음
- 캐쉬를 통해 속도의 향상, 전송량 경량화 가능

```js

//main.html
<!DOCTYPE html>
<html>
<body>
    <input type="button" id="hw" value="Hello world" />
    <script type="text/javascript" src="script.js"></script>
</body>
</html>

//script.js
var hw = document.getElementById('hw');
hw.addEventListener('click', function(){
    alert('Hello world');
})
```


### js script 파일의 위치

script 를 head tag 에 넣을수도 있으나

js 스크립트에서 약간의 추가가 필요하다
- window.onload = function(){    }
- 이것은 웹브라우저의 모든 구성요소에 대한 load 가 끝났을때 브라우저에 의해서 호출되는 함수 = 이벤트
- 보통은 하단에 스크립트를 위치하는것이 더 좋은 방법

```js
//main.html

<!DOCTYPE html>
<html>
<head>
    <script src="script.js"></script>
</head>
<body>
    <input type="button" id="hw" value="Hello world" />
</body>
</html>

//script.js
window.onload = function(){
    var hw = document.getElementById('hw');
    hw.addEventListener('click', function(){
        alert('Hello world');
    })
}
```