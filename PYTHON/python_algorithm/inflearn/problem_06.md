## 자릿수의 합


```
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 
각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자 를 출력합니다.

▣ 입력예제 1 
3
125 15232 97

▣ 출력예제 1 
97
```


---

## 나의 풀이

- 숫자를 -> str 으로 치환 -> 한글자 한글자를 str에서 int 로 치환하여 덧셈하는 로직
- 최대값 구하는 logic

```py
n = int(input())
m = list(map(int, input().split(' ')))

sum_list = []
Max=0
for i in m:
    to_string = str(i)
    sum_int=0
    for j in to_string:
        sum_int+=int(j)
    sum_list.append(sum_int)

for i in range(len(sum_list)):
    if sum_list[i] > Max:
        Max = sum_list[i]

for i in range(len(sum_list)):
    if sum_list[i] == Max:
        print(m[i])
```
---
## 해설
### 총 두가지 풀이법을 제시하였음


1. 몫 과 나머지

- 각자리의 자연수를 더하는 함수를 먼저 구축하였다.
- x 가 0보다 작아질 때 까지 10으로 나눈 나머지를 더함
- x 의 몫을 다시 x 로 치환

2. str -> int 

- 내가 풀엇던 방식

```py
n = int(input())
m = list(map(int, input().split(' ')))

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

Max= -2147000000

for x in m:
    tot=digit_sum(x)
    if tot>Max:
        Max = tot
        res = x
print(res)

```

