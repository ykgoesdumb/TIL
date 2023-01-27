## Reverse String


- list 에있는 순서를 거꾸로 뒤집은 list 출력

```python

# my initial answer

class Solution:
    def reverse_string(self, s: List[str]) -> None:
        reverse_list=[]
        s[::-1] = reverse_list.append()
        return reverse_list

solution = Solution()
test_list = ['a','b','c']
result = solution.reverse_string(test_list)
print(result)
```
- 오답 밑에 풀이방식 참조

---


## two pointer way
- pointer 두개를 이용하여 범위를 조정
  
```python
def reverse_string(self, s: List[str]) -> None:
    left, right = 0, len(s) -1
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
```


## pythonic way

```python
def reverse_string(self, s: List[str]) -> None:
    s.reverse()
```
- reverse 는 list 에만 제공
- 문자열일 경우 
  - s = s[::-1]
  - s[:] = s[::-1]
