## 중첩 반복문

``` py
## print() 는 줄바꿈 j loop 이 한번 다 완리할경우 줄 바꿈

for i in range(5):
    print('i:', i, sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()

i:0 j:0 j:1 j:2 j:3 j:4 
i:1 j:0 j:1 j:2 j:3 j:4 
i:2 j:0 j:1 j:2 j:3 j:4 
i:3 j:0 j:1 j:2 j:3 j:4 
i:4 j:0 j:1 j:2 j:3 j:4 
```

- 계단식 출력

```py
for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

* 
* * 
* * * 
* * * * 
* * * * * 

## 역순

for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()

* * * * * 
* * * * 
* * * 
* * 
* 
```

## 문자열과 내장함수

```py

## find 는 제일 처음 결과 인덱스만 반환
msg = "It is Time"
tmp = msg.upper()
print(tmp.find('T'))

## count 는 전부 다셈
print(tmp.count('T'))

## string 변수의 모든 string 값들을 다 출력

for i in range(len(msg)):
    print(msg[i], end = ' ')

I t   i s   T i m e 

## 위와 동일하다
for j in msg:
    print(j , end=' ')


## 대문자만 출력 isupper 는 대문자 인지 아닌지 boolean
for k in msg:
    if k.isupper():
        print(k, end= ' ')

## is lower 소문자일때만
## is alpha 알파벳일때만

## ASCII number 출력
print(ord(x))

## ASCII number -> 문자로
print(chr(x))

```