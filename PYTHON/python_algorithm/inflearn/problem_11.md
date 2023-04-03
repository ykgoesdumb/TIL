## 회문 문자열 검사

```
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

▣ 입력설명

첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다. 각 단어의 길이는 100을 넘지 않는다.

▣ 출력설명

각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

▣ 입력예제 
5
level
moon
abcba
soon
gooG

▣ 출력예제
#1 YES
#2 NO
#3 YES
#4 NO 
#5 YES
```

---
## 나의 풀이

- str.lower
- 슬라이싱 사용 [::-1]
- f string 사용

```py
n = int(input())

for i in range(1,n+1):
    word=list((str.lower(input())))
    word_reversed=word[::-1]
    if word == word_reversed:
        print(f'#{i} YES')
    else:
        print(f'#{i} NO')
```

---
## 해설

- 가운데 중간의 유무와 상관없이 맨 앞 맨 뒤, 맨앞 +1, 맨뒤 -1 .... 짝을 이루는 인덱스의 숫자만 같으면 회문 문자열임
- size//2 로 최대 단어가 몇 쌍이 파악
- 두개의 for 문으로 구현
- 2번째 풀이방법은 나의 답과 일치

```py
n = int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
        else:
            print("#%d YES" %(i+1))
