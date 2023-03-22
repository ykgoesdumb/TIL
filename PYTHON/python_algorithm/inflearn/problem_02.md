## K 번째 수 

```
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
```
---
## 나의 정답
  - f string 사용하였다
  - 정답


```py
T = int(input())

for i in range(1,T+1):
    N, s, e, k = map(int,input().split())
    N_var = map(int,input().split())
    list_created = []
    for j in N_var:
        list_created.append(j)
    answer_list = list_created[s-1:e]
    answer_list.sort()
    print(f'#{i} {answer_list[k-1]}')
```


## 해설
  - 조금 올드한 프린트 방식이지만 결과적으로 동일하다

```py
T = int(input())

for i in range(1,T+1):
    N, s, e, k = map(int,input().split())
    a=list(map(int, input().split()))
    a=[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))
```
