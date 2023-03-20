## 리스트와 내장함수

```py

a=[]
b=list(range(1,11))

print(a)
print(b)
```

```py
## append

a.append(6)
print(a)

[6]


## insert(인덱스번호, 넣을 값) list 에서 인덱스 번호에 넣을값을 추가한다
c=list(range(1,7))
c.insert(3,7)
print(c)

[1, 2, 3, 7, 4, 5, 6]


## pop 제일 마지막 index 를 빼낸다
a.pop()
print(a)

## remove() 해당값 삭제 (가장 먼저 match 된 값만 삭제한다)

d=[1,1,2,3,4,5,6]
d.remove(1)
print(d)

[1, 2, 3, 4, 5, 6]


## 검색한 값의 인덱스 번호를 출력

print(d.index(5))

4

```

- random

```py
import random as r

## shuffle 로 섞음

a=list(range(1,11))
r.shuffle(a)
print(a)

## 정렬
a.sort()

## 역순
a.sort(reverse=True)

## 클리어
a.clear()
```


- 리스트 for loop

```py
## 리스트도 똑같이 출력

a=[23, 12 ,394, 324, 21]

for i in range(len(a)):
    print(a[i], end=' ')

for j in a:
    print(j, end=' ')


```
- enumerate


```py


## enumerate 로 list 를 tuple 값으로 출력

for k in enumerate(a):
    print(k, end=' ')


(0, 23) (1, 12) (2, 394) (3, 324) (4, 21) 


## 조금더 편하게 enumerate 접근

for index, value enumerate(a):
    print(index, value)


```



- if all 

```py
## if all(조건 for loop)  loop 중 모든 변수가 '조건'을 만족했을 때  참

if all(60>x for x in a):
    print("YES")
else:
    print("NO")
```

- if any
    - 하나라도 조건을 만족한다면 참
    - 모두가 거짓일 때 거짓

```py
if any(60>x for x in a):
    print("YES")
else:
    print("NO")
```



## 2차원 리스트 생성과 접근
- 2차원 리스트는 표의 개념으로 접근하는게 좋음

```py
a=[[0]*3 for i in range(3)]
print(a)

[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a[1][1]=2
print(a)

[[0, 0, 0], [0, 2, 0], [0, 0, 0]]

## 바둑판 처럼 출력
for x in a:
    print(x)

[0, 0, 0]
[0, 2, 0]
[0, 0, 0]

## list 형식이 아닌 숫자로만 보고싶다면?
## print() 는 줄바꿈을 내포함을 기억하자

for x in a:
    for y in x:
        print(y, end=' ')
    print()

0 0 0 
0 2 0 
0 0 0 
```

