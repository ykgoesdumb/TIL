## 최솟값 구하기



```py
#min 쓰지 않고 배열에서 최솟값 구하기

arr=[5,3,7,9,2,5,2,6]

##일단 처음의 값을 무한대 (가장 큰 값)으로 설정
Min=float('inf')


for i in range(arr):
    if arr[i] < Min:
        Min = arr[i]

##무한대가 아니더라도 이렇게 설정해도 결과는 동일하다

Min=arr[0]

for i in arr:
    if i < Min:
        Min = i
```

