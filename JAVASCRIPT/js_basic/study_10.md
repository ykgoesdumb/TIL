## RegExp (regular expression)

컴파일은 검출하고자 하는 패턴을 만드는 일

- 정규표현식 객체를 만드는 방법은 두가지다

```js
var a = "a";

// 첫번째 방법 (리터럴)
var pattern = /a/;

// 두번째 방법 (정규표현식 객체 생성자)

var pattern = new RegExp('a');

```

## 정규표현식 실행하기

```js

//exec method

console.log(pattern.exec('abcdef')); //['a', index: 0, input: 'abcdef', groups: undefined]

console.log(patern.exec('bcdef')); //null

//test method

console.log(pattern.test('abcdef')); // true
console.log(pattern.test('bcdefg')); // false


//string.match()

console.log('abcdef'.match(pattern)); // ["a"]
console.log('bcdefg'.match(pattern)); // null

//string.replace)()
console.log('abcde'.replace(pattern, 'A')); //Abcede

```


## 정규표현식 패턴

- 정규표현식은 / 과 / 사이에 표현을 한다
- / / 뒤에 붙는 옵션이 있음

i 를 붙이면 대소문자 구분을 하지 않는다
```js
const pattern1 = /a/;
const pattern2 = /a/i;

console.log(pattern1.test('Abcde'));  // false
console.log(pattern2.test('Abcde'));  // true
```

g를 붙이면 검색된 모든 결과를 반환한다
- g 가 없을땐 최초로 조건에 맞는 검색결과만 반환하고 종료된다


```js
var xg = /a/;
console.log("abcdea".match(xg));
var og = /a/g;
console.log("abcdea".match(og));
```

정규표현식 안에서 ( ) 는 그룹을 의미한다
- /(\w)\s(\w)/
- 그룹이 두개가 있는 것
- \w 는 단어를 뜻한다 (A~Z, a~z, 0~0)
- \s 는 공백을 뜻함
- $1 첫번째 그룹을 의미, $(숫자) 의 형태로 사용

```js
var pattern = /(\w+)\s(\w+)/;
var str = "bye everybody";
var result = str.replace(pattern, "$2, $1");
console.log(result);  //everybody, bye
```


## 치환

- 아래의 코드는 패턴을 찾을때마다 function 을 실행한다

```js
var urlPattern = /\b(?:https?):\/\/[a-z0-9-+&@#\/%?=~_|!:,.;]*/gim;

var content = '구글 : http;//google.com 입니다. 네이버 : http://naver.com 입니다. ';
var result = content.replace(urlPattern, function(url){
    return '<a href="'+url+'">'+url+'</a>';