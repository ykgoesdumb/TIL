# 문자열 조작


## Valid Palindrome

- palindrome 이란 '회문' 거꾸로해도 똑같은 문장
  - "여보 안경 안 보여"
  - , " 등 특수문자, 공백 제외

```python

    # step 1. convert every word to lowercase and exclude non-alphabet words
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for word in s:
            if word.isalnum():
                strs.append(word.lower())
    # step 2. validate if string is palindrome or not
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

solution = Solution()
test_case: str = 'YaY'
result: bool = solution.isPalindrome(test_case)
print(result)

```

- 자료형을 deque 로 선언하면 더 좋은 성능을 낼 수 있음
  
```python
import collections

    def ifPalindrome(self, s:str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())
    # deque 의 popleft 를 사용하면 더 빠른처리 가능하다
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True
```

- 슬라이싱 사용
- 정규표현식으로 deque 보다 좋은성능 낼 수 있음

```python
import re

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규 표현식
        ## ^ 패턴 사용으로 [] 안에 들어간 패턴 이외의 것을 선택하여 ('' 로) 삭제한다 
        s = re.sub('[^a-z0-9]', '',s)
        return s == s[::-1]

```

- 한문장으로 반복문과 조건문을 같이 쓸 수 있음

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        strs = [char.lower() for char in s if char.isalnum()] 
        return strs == strs[::-1] 

solution = Solution()
test_case: str = "A man, a plan, a canal: Panama"
result: bool = solution.isPalindrome(test_case)
print(result) # 결과 : True
```



- 슬라이싱은 내부적으로 C로 구성되어있어서 좋은 기능을 제공한다.

- s[::1] 는 동일함
- s[::-1]는 뒤집음
- s[::2]는 2칸씩 앞으로 이동



