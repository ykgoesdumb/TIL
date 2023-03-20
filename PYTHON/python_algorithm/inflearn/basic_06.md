## 함수 만들기

- 함수는 스크립트 상단에 정의

- print 와 return 의 차이

```py

# print 를 쓰면 함수 자체에서 값을 출력한다
def add(a,b):
    c=a+b
    print(c)


# return 을 쓰면 함수가 값을 가진 변수처럼 저장된다
def add(a,b):
    c=a+b
    return c

x=add(3,2)
print(x)
5

```

- 소수만 출력하는 함수
- 리스트가 주어졌을때 소수인값만 출력하라

```py

x=[12,13,7,9,19]

## 나의 판단오류 모든 결과물을 한번에 구현하는 함수를 만들려고 시도한것
def sosu(a):
    for i in a:
        answer=[]
        if i%2

## 정답은 함수인지 아닌지를 판별하는 함수를 먼저 만들고, 그뒤에 그 함수를 일괄 적용하는 두단계로 진행하면 되는 것
## 함수 정의

x=[12,13,7,9,19]

def sosu(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

answer=[]

for i in x:
    if sosu(i):
        answer.append(i)
print(answer)

[13, 7, 19]
```

## 람다 함수

- lamda 매개변수: 조건식
- 람다식은 변수에 할당을 해주어야 사용가능

```py
# 기존의 함수식

def plus_one(x):
    return x+1
print(plus_one(1))

# 변수를 함수명처럼 사용

plus_two = lambda x: x+2
print(plus_two(1))
```

- list map
- map(plus_one,a) 이렇게 함수와, 변수를 분리한것에 주목
- map class를 다시 list 라는 내장함수로 다시 list 화 (형변환)

```py
def plus_one(x):
    return x+1
a=[1,2,3]
print(list(map(plus_one, a)))

[2, 3, 4]

print(tuple(map(plus_one, a)))

(2, 3, 4)

# 이렇게 쓰지 않도록 주의한다
print(list(map(plus(a)))) 
```

- 위의 방식은 함수를 따로 정의해야함
- 함수를 정의하지않고 바로 적용시킬 수 있는 것이 lambda
- 익명의 함수 표현식
```py

a=[1,2,3]
print(list(map(lambda x: x+1, a)))

[2, 3, 4]