python 3.7 이후 부터는
해시 테이블을 이용한 자료형특성상 입력순서 유지되지 않았던게 개선됨


```python
a = dict()

# or

a = {}

# 예외 처리


try:
    print(a['key4'])
except: KeyError:
    print('존재하지 않는 키')
```

```python
# 반복문 dictionary 의 items() 메소드

for k,v in a.items():
    print(k,v)

```

# collections


## defaultdict
### set default 보다 collections 모듈에서 defaultdict 사용 많이함

```python
import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
a
# >> defaultdict(<class 'int'>, {'A': 5, 'B': 4})


# 존재하지 않는 키에서 더하기
a['C'] += 3

## >> defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 3})
## keyError 발생하지 않는다
```


## Counter


 - counter 는 item 의 대한 개수를 계산해 딕셔너리로 리턴

```python

>>> b = [1,2,2,3,3,3,3,4,4,4,5,6,7,7,7,6,5,6,4,4,4,4,5,5,6,8]
>>> c = collections.Counter(b)
>>> c
Counter({4: 7, 3: 4, 5: 4, 6: 4, 7: 3, 2: 2, 1: 1, 8: 1})


>>> type(c)
<class 'collections.Counter'>
```

- 최빈값 뽑기

```python
>>> c.most_common(3)
[(4, 7), (3, 4), (5, 4)]
```

## OrderedDict
- 3.6 이전의 dictionary type 은 순서가 유지되지 않아서 ordereddict 라는 별도의 객체를 제공했엇음



---
# type 선언

- 이름대신 기호로 선언
  
```python
>>> type([])
<class 'list'>
>>> type(())
<class 'tuple'>
>>> type({})
<class 'dict'>
>>> type({1})
<class 'set'>
```

