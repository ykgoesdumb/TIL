자바스크립트의 실행 환경은 웹 브라우저이다

- 브라우저 마다 개발자 도구라는 것이 있음
- 구글 크롬 개발자도구
- 파이어폭스 확장기능 firebug


HTML CSS 등을 동적으로 제어하기 위해서 만들어진 언어
- 오늘날 자바스트립트 매우 다양한 용도로 사용되고 있음
- 기본적으로 웹브라우저에서 동작하는 javascript 는 html 포맷 안에서 동작


밑에 script 부분이 자바스크립트 부분
```javascript
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"/>
    </head>
    <body>
        <script>
            alert('Hello world');
        </script>
    </body>
</html>
```


크롬을 사용하면 

- command +alt +j 누르면 개발자 도구 뜸 (mac)
- ctrl + shift + j (window)



DOM
- 브라우저에서 자바스크립트로 html 을 제어하는 api
- 자바스크립트 언어 자체는 아니다
- document oriented model
- dom tree 의 최상의 node 는 document 객체

DOM tree
- <html>
  - <head>  , <body>

- tree 형식으로 되어있는 구조 각각이 node

BOM
- browser object model
  

document.getRootNode()
- 최상위 객체

document.childNodes[1]~~~
- 차상위 객체

