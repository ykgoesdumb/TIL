## 소수(에라토스테네스 체)
```
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.

만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 제한시간은 1초입니다.

▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.

▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.

▣ 입력예제
20

▣ 출력예제
8
```


---

## 나의 풀이

- 소수가 약수가 2개인것을 구현하였음
- 중첩 for 문 구현
  - 나머지 0 일때 count 1 씩 증가
  - count 가 2일때 prime_count 1증가

```py
n = int(input())

prime_count=0

for i in range(2,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count == 2:
        prime_count+=1

print(prime_count)
```

---
## 해설

- [0] 을 n 개 이상의 숫자로 곱해서 (넉넉하게) 0 인 list ch 생성
- 중첩 for 문은 동일하나 step 을 사용하여 반복문의 배수 에 모두 1 을 더함
- i = 2 일땐 cnt 를 하나 올리고 (소수의 갯수) 2, 4, 6, 8 번에 해당하는 모든 숫자들 1 더함
  - 다음 반복문시 ch 1일때 자동으로 스킵 (2의 배수인 4 6 8번 index 는 이미 1 값을 가지고 있음)

![img src](https://user-images.githubusercontent.com/49462767/227769774-f6574f30-1d19-4536-b4c0-d3ebd0673d31.png)


```py
n = int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)
