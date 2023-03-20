## 변수 입력과 연산자

- input
```py
a = input("숫자를 입력하세요 : ")
print(a)
```
- 다중 input 

```py
a, b = input("숫자를 입력하세요 : ").split()
print(a+b)

# 2 와 3을 input 으로 줄때 결과는 str 으로 인식하여

23

# 조금 귀찮긴 하지만 이렇게 일일히 int 로 설정하는방법도 있다
a, b = input("숫자를 입력하세요 : ").split()
a=int(a)
b=int(b)
print(a+b)


# 처음부터 int 로 넣는 map 함수를 이용한다
a, b = map(int, input("숫자를 입력하세요 : ").split())

# int 와 map 둘다 내장 함수
```


