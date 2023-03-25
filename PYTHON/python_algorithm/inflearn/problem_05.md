## 정다면체

```
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.


▣ 입력설명
첫 번째 줄에는 자연수 N과 M이 주어집니다. N과 M은 4, 6, 8, 12, 20 중의 하나입니다.
▣ 출력설명
첫 번째 줄에 답을 출력합니다.


▣ 입력예제 
4 6

▣ 출력예제 
5 6 7

```

---
## 나의 풀이 

- 일단 풀다가 포기하였음
- cnt 의 접근은 옳은 접근이였음
- set(nrpt non-repeat) 자료형과 list(rpt repeat) 자료형, 그리고 count 를 세는 0의 리스트를 따로따로 만드는 오류를 범했다 
- 복잡성이 늘어나 감당이안되었음


```py
n, m= map(int, input().split(' '))
nrpt = set()
rpt = []

for i in range(1,n+1):
    for j in range(1,m+1):
        nrpt.add(i+j)
        rpt.append(i+j)

nrpt=list(nrpt)
nrpt.sort()
rpt.sort()

cnt={}

for key, count in range(len(nrpt)):
    cnt.append(0)

for g in range(len(rpt)):
    if rpt[g] in nrpt:

print(nrpt)
print(rpt)
```


## 해설

- 문제를 잘 이해하면 n면체 와 m면체의 값의 최대는 n+m 일 것
- 2~n+m 까지 가 경우의수일것 -> set 을 만들 필요 없었으며 cnt 의 index 번호 = 경우의 수로 출력된 숫자값
  - cnt = [0]*(n+m+1)         cnt[i+j]+=1
- cnt 인덱스 번호에 +=1 씩 더함으로써 경우의 숫자 카운팅을 계산
- Max 값을 0 으로 설정한뒤 최빈값을 갱신함
- Max 값과 일치한 cnt의[index] 값 출력 

```py
n, m= map(int, input().split(' '))
cnt = [0]*(n+m+1)
Max = 0

for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1

for i in range(len(cnt)):
    if cnt[i] > Max:
        Max=cnt[i]

for i in range(len(cnt)):
    if cnt[i]==Max:
        print(i, end=' ')
```
