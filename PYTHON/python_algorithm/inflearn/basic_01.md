## 변수와 출력함수

- 변수명 정하기
  - 영문과 숫자 _ 로 이루어짐
  - 대소문자를 구분
  - 문자나, _ 로 시작한다
  - 특수문자를 사용하면 안된다
  - 키워드 사용하면 안된다 (if for)

```bash
같다의 개념이 아닌 대입 연산자이다
a 를 1에 대입한다
a=1
A=2

여러개의 변수를 동시에 선언하고 값을 넣을 수 있다
a,b,c =3,2,1

```


### 값 교환

```
a,b = 10, 20
a,b = b,a
print (a,b)

a = 20 , b = 10
```

### 변수 타입
- 8 byte 가 넘어가면 실수형은 손실됨  (float)


### 출력 타입

```
## 복수의 변수 print 할때 자동으로 띄어쓰기
a,b,c = 1,2,3
print(a,b,c)

1 2 3

## separator

print(a,b,c, sep ='')

123

print(a,b,c, sep ='\n')

1
2
3
```

### 줄바꿈
- print 를 할경우 자동으로 줄바꿈을 수행
- 줄바꿈을 없애고 싶을때

```
print(a, end=' ')
print(b, end=' ')
print(c)

1 2 3
```


