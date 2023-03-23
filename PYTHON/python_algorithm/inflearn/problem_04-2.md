## 대표값

```py
N명의 학생의 수학점수가 주어집니다. 
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.

▣ 입력예제 1
10 
45 73 66 87 92 67 75 79 75 80

▣ 출력예제 1 
74 7
```

---

## 나의 풀이

- 절댓값 함수를 어디서 적용할껀지에서 삽질을 많이함
- if 문을 중첩해서 사용하는 부분에서 시간 오래 소요

```py
n = int(input())
m = list(map(int, input().split(' ')))

total=0

for i in m:
    total+=i
mean=round(total/n)

deviation=[]

for j in m:
    deviation.append(abs(mean-j))

for k in range(len(deviation)):
    if deviation[k] == min(deviation):
        if m[k] > mean:
            print(mean, end=' ')
            print(k+1)
            break
```

## 해설

```py

n = int(input())
m = list(map(int, input().split(' ')))

# 그냥 sum 하면 되는데 for 문을 돌렸다 나는..
mean = round(sum(m)/n)
Min = 2147000000


for idx, x in enumerate(m):
    deviation=abs(x-mean)
    if deviation < Min:
        Min=deviation
        score=x
        res=idx+1
    elif deviation==Min:
        # deviation 값이 min이여도 기존 score 와 같기 때문에 출력되는 인덱스에 변화 없음
        if x>score:
            score=x
            res=idx+1
```

## 추가 사항

- python 의 round 함수는 'round_half_even' 방식을 사용하고있음
- 우리가 통상적으로 아는 반올림은 'round_half_up' 4이하 는 내림, 5이상은 올림 하는방식
- round half even 은 반올림 할 소수 첫번째 자리의 값이 5일때 '가장 가까운 짝수' 로 보낸다
  - 4.5 를 round half even 한다면
    - 4 이다
  - 5.5 round half even 한다면
    - 6 이다

- 그렇담 소수의 반올림도 동일하게 적용되는가?
  - nope
  - a = 0.45
  - round(a, 1)
  - 0.5