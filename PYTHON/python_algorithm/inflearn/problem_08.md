## 뒤집은 소수

```
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 
예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력 한다. 
단 910를 뒤집으면 19로 숫자화 해야 한다. 첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하 여 프로그래밍 한다.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다. 각 자연수의 크기는 100,000를 넘지 않는다.

▣ 출력설명
첫 줄에 뒤집은 소수를 출력합니다. 출력순서는 입력된 순서대로 출력합니다.

▣ 입력예제 
5
32 55 62 3700 250

▣ 출력예제 
23 73
```
---

## 나의 풀이

- reverse 함수를 str 변환후 index 에 음수값을 주어 역순으로 for문을 돌렸다 
  - 그런뒤 int 로 재전환

- 23 None None 73 None 
  - 이런식으로 None 값이 출력되어 None 을 제거하는 로직을 추가하였다
  - 정확히 왜 None 값이 출력되는지 이해하지 못함
 
```py

n=int(input())
m=list(map(int, input().split(' ')))

def reverse(x):
    x=str(x)
    reversed=''
    for i in range(len(x)):
        reversed+=x[-i-1]
    answer=int(reversed)
    return answer

def isPrime(x):
    cnt=0
    for i in range(2,x+1):
        if x%i==0:
            cnt+=1
    if cnt==1:
        return(x)

for i in m:
    answer = isPrime(reverse(i))
    if answer != None:
        print(answer, end=' ')
```


---
## 해설

- x = 10으로나눈 몫 을 갱신하는 logic 7번문제에도 동일하게 적용된 로직이다
- 역순패턴으로 숫자를 채워나가는 방식
  - answer= 0 으로 최초 세팅
  - answer = answer*10 + 나머지
  - 987 을 10 으로 나눈 나머지는 7
  - answer = 0 * 10 + 7   = 7
    - 이렇게 7 -> 78 -> 789 가 됨


- isPrime 구현도 내가 한 방식보다 효율적으로 접근함
  - True False 로 return,
  - 나는 약수가 1개일때 return 하는 logic 이였지만 해설은 약수가 존재하면 false 로 loop 을 끝내버렸음
    - overhead 더 적은 방식
- for else 구문을 사용하였다
  - 정상적으로 for 문을 마쳤는데 return 한 값이 없을 경우 True return

```py
n=int(input())
m=list(map(int, input().split(' ')))

def reverse(x):
    res=0
    while x>0:
        t=x%10
        x=x//10
        res=res*10+t
    return(res)

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True

for x in m:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
```     