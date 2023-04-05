## 숫자만 추출

```
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다. 
만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 됩니다.
즉 첫 자리 0은 자연수화 할 때 무시합니다. 출력은 120 를출력하고,다음 줄에120 의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.

▣ 입력설명

첫 줄에 숫자가 썩인 문자열이 주어집니다. 문자열의 길이는 50을 넘지 않습니다.

▣ 출력설명

첫 줄에 자연수를 출력하고, 두 번째 줄에 약수의 개수를 출력합니다.

▣ 입력예제

g0en2Ts8eSoft

▣ 출력예제

28
6
```
---
## 나의 풀이

- string 화 한 숫자 0~9 를 list 로 생성하였음
- *10+int(i)
- 약수가 들어갈 list 생성 후 append 하고 len 출력
```py
n=list(str(input()))
b=['0','1','2','3','4','5','6','7','8','9']
res=0
divisor=[]

for i in n:
    if i in b:
        res=res*10+int(i)
print(res)

for j in range(1,res+1):
    if res%j==0:
        divisor.append(j)
print(len(divisor))
```

---
## 해설
- isdigit = 모든 숫자형 2^31 이 들어와도 true 로 인식
- isdecimal = 0~9 까지의 숫자인지 true or false
  - string 이여도 하나하나 숫자인지 아닌지 확인함

```py
s=input()
res=0
for x in s:
    if x.isdecimal():
        res=res*10+int(x)
print(res)

cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)
```
