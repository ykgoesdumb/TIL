## typescript 는 정적 언어이다

- 기존의 javascript 는 실행을 해야 runtime 에러를 확인 할 수있는 동적 언어
- typescript 는 컴파일 단계에서 에러를 알 수 있는 정적언어임



```javascript
function add(num1, num2) {
    console.log(num1+num2);
}


add();
add(1);
add(1,2);
add(3,4,5);
add('hello', 'world');

```

사실상 설계 용도에 적합한것은  3번 뿐이나 1,2,4,5 번 다 에러를 발생하지 않고 값을 출력함

1,2 번은 인자값이 조건과 맞지 않아 NaN 을 반환
4 는 2개의 params 까지 인식하고 3번째 parameter 인 5를 계산하지 않음


---

### 되도록이면 any type 을 쓰지 않는것을 원칙으로 한다

```typescript
function add(num1:number, num2:number){
    console.log(num1+num2);
}

add();
add(1);
add(1,2);
add(3,4,5);
add('hello', 'world');
```

type script 로 작성하였을때는 run 시키기 전에 에러가 뜸

---

## type 추론
```javascript
let age:number = 30;
let isAdult:boolena = true;


//same function
let a:number[] = [1,2,3];
let a2:Array<number> = [1,2,3];

let week1:string[] = ['mon','tue']
let week2:Array<string> = ['mon','tue']

//tuple
let b:[string, number];
b = ['z',1];   //this works
b = [1,'z'];   //error on compile stage

b[0].toLowerCase();     //this works
b[1].tolowerCase();     //error on compile stage

```

void 는 함수에서 아무것도 반환하지 않을 때 사용한다



