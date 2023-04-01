## K 번째 약수

```
어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다. 6을 예로 들면
6÷1=6...0 6÷2=3...0 6÷3=2...0 6÷4=1...2 6÷5=1...1 6÷6=1...0
그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
```

- 내 풀이
  - 정답이다
  - 리스트 사용

```py
N, K=map(int, input().split())
params=[]
for i in range(1,N+1):
    if N%i==0:
        params.append(i)
if len(params)>=K:
    print(params[K-1])
else:
    print(-1)
```

- 정답
  - for else 구문
  - if 절 조건 두개 break 사용
  - count 사용
```py
N, K=map(int, input().split())
count=0
for i in range(1,N+1):
    if N%i==0:
        count+=1
    if count==K:
        print(i)
        break
else:
    print(-1)
```
