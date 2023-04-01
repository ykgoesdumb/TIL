## K번째 큰 수

```
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 
같은 숫자의 카드가 여러장 있을 수 있습니다. 
현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려 고 합니다. 
3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.


▣ 입력설명

첫 줄에 자연수 N(3<=N<=100)과 K(1<=K<=50) 입력되고, 그 다음 줄에 N개의 카드값이 입력 된다.

▣ 출력설명

첫 줄에 K번째 수를 출력합니다. K번째 수는 반드시 존재합니다.

▣ 입력예제 1

10 3
13 15 34 23 45 65 33 11 26 42

▣ 출력예제 1 

143

```

---
## 나의 풀이

```py
N, K=map(int, input().split())
a=list(map(int, input().split()))
answer=[]

for i in a[0:-2]:
    for j in a[1:-1]:
        for k in a[2:]:
            answer.append(i+j+k)
else:
    answer.sort(reverse=True)

for l in range(len(answer)):
    if K>1:
        if answer[l+1] == answer[l]:
            continue
        else:
            K -=1
    else:
        print(answer[l])
        break

## 내가 받은 값

172

## answer 의 list

[195, 175, 175, 175, 172, 164, 164, 164, 163, 163, 163, 156, 156, 155, 155, 155, 153, 153, 153, 152 ....]

## 여기서 K 번 째 큰수를 출력한 172 값이 나왔다 로직은 맞게 나온 것 같은데.. 뭔가 list 꼬였다.
```

## 해설
- set 의 자료함수를 사용함
  - set 은 중복된 숫자를 집어 넣지 않음
  - set 는 append 가 아닌 add 를 사용해주어야함
  - set 는 sort기능이 없으므로 list로 재 변환 해주어야함

- set 자료형을 사용하여 중복을 없애는 조건 추가하지 않고 사전에 없애버림
- 

```py
n, k=map(int, input().split())
a=list(map(int, input().split()))
res=set()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

res=list(res)
res.sort(reverse=True)
print(res[k-1])
