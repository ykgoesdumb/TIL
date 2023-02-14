
## 객체지향

- 객체지향에 대해서 공부할 때 철학적으로 파고들지 말 것
- 프로그램을 상태와 행위로 이루어진 '객체'로 만드는 것
- 레고 블럭처럼 조립해서 하나의 프로그램을 만드는 것


### 객체

- 변수와 메소드를 그룹핑한 것

### 문법과 설계

- 문법  
  - 객체를 만드는 법에 대한 학습
- 설계
  - 좋은 객체를 만드는 법

- 객체지향이 추구하는 지향점이 몇가지 있음


### 부품화

- 모니터와 컴퓨터를 분리했다 (부품화)
- 그렇담 그 부품을 분리하는 기준은 무엇인가? 그 기준을 세우는 것이 '추상화'
- 정해진 답은 없다 기능이 분리되어있는 컴퓨터가 있는반면에 일체형 컴퓨터도 있음 -> 설계의 차이

메소드 또한 부품화의 예이다
- 로직들을 결합하여 메소드를 만들고 메소드를 하나의 부품으로 사용하여 독립되 프로그램을 만드는 것


### 은닉화, 캡슐화
- 부품화라는 것이 단순히 동일한 기능을 하는 메소드와 변수를 그룹핑한다고 달성되는 것은 아님
- 어떻게 만들어졌는지 모르는사람도 사용하는 방법만 알면 쓸 수 있어야함
- 컴퓨터 어떻게 설계되었는지 몰라도 전원버튼을 눌러 킬 수 있는것처럼

- 내부의 동작을 단단한 케이스에 숨기고 사용자에게는 그 부품의 사용방법만을 노출하는 것 (은닉화, 캡슐화)

### 인터페이스
- 인터페이스는 부품들 간의 약속이다
- HDMI 케이블이 규격을 따르고 있는것처럼
- 이러한 약속을 프로그래밍적으로 구현한 것


---
### 객체 예시
- 객체 내의 변수를 property, 함수를 method 라고 한다
- 객체를 생성하고 그 안에 property와 method를 넣어보자

```js
var person = {}
person.name = 'kylekim'
person.introduce = function(){
    return 'My name is '+this.name;
}

document.write(person.introduce());
```

객체를 정의할때 넣어준다면

```js
var person = {
    'name' : 'kylekim',
    'introduce' : function(){
        return 'My name is '+this.name;
    }
}
document.write(person.introduce());
```
- 딱히 개선되진 않았다
- 객체를 만드는 함수인 생성자를 사용해보자

### 생성자

- js 에서 함수란 재사용 가능한 logic 이라기보다 객체를 만드는 창조자 라고 할 수 있음
- 함수를 호출할때 new를 붙이면 새로운 객체를 만든 후에 이를 리턴한다

```js
function Person(){}
var p1 = new Person();
p1.name = 'kylekim';
p1.introduce = function(){
    return 'My name is '+this.name;
}


var p2 = new Person();
p2.name = 'leolee';
p2.introduce = function(){
    return 'My name is '+this.name;
}
```
- 새로운 객체를 생성하긴 하지만 효율적이지 않다
- 생성자 내에서 property 를 정의하는 방식은?


```js
function Person(name){
    this.name = name;
    this.introduce = function(){
        return 'My name is '+this.name;
    }
}

var p1 = new Person('kylekim')
var p2 = new Person('leolee')
```
- 드디어 생성자를 사용하여 재사용이 용이한 코드가 탄생하였다



### 생성자의 특징
- 일반적으로 생성자는 class 의 소속이다
  - python 의 class self.~~ 가 그 예이다
- 하지만 js에서는 생성자의 주체는 함수이다
  - 함수에 new를 붙이는 것을 통해서 객체를 만들 수 있음


