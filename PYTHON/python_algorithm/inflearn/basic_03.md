## 조건문 if (분기, 중첩)

```py

# == 는 관계연산자 라고함

x=7
if x == 7:
    print('lucky')

lucky

if x != 7:
    print('lucky')

```


```py
## 나머지가 1 홀수 라는 뜻

x = 12
if x>=10:
    if x%2==1
        print('10 이상의 홀수')
```


```py
# C 혹은 C++ 에서는 허용안하지만 python 에서는 and 연산없이 아래와 같이 표현 가능
x = 7
if 0<x<10:
    print("10보다 작은 자연수")
```


```py
# 아무일도 일어나지 않음
for i in range (10,0):
    print(i)

# 1씩 작아진다면?

for i in range (10,0,-1):
    print(i)

```

## while

```py
while i <=10:
    print(i)
    i=i+1


# 무한루프 깨는 break

i=1
while True:
    print(i)
    if i==10
        break
    i+=1

# 밑의 logic 을 건너뛰는 continue

for i in range(1,10):
    if i%2==0:
        continue
    print(i)


# for 문이 정상적으로 종료가 되었다면 그 뒤에 else도 출력함
# if else 만 있는것이 아닌 for else 도 있음


for i in range(1,11):
    print(i)
else:
    print(11)
```


---

- 1 부터 n 까지 홀수 출력

```py
n = input()
for i in range(n+1):
    if i%2==1:
        print(i)
```


- 1 부터 n 까지의 합 구하기

```py
n = int(input())
answer = 0

for i in range(n+1):
    answer = answer + i

print(answer)
```

- n의 약수 출력하기

```py
n = int(input())

for i in range(1,n+1):
    if n%i==0:
        print(i, end=' ')
```