## base 64 는 64진법이다


<br></br>
![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FDhKIc%2FbtqC6P1AjX8%2FHXZAO93bdtqma76OiKJH00%2Fimg.png)



변환하는 순서는 이러하다

>원본 문자열 -> ASCII binary -> 6bit 로 cut -> base64 encoding

> Man -> 77 97 110 -> 01001101 01100001 01101110 -> TWFu




## 왜 base 64 를 사용하는가?


Base64 로 인코딩하면 6bit 당 2 bit 의 overhead 가 발생한다? -> (33% 증가)

그럼에도 불구하고 왜 쓸까?

- 통신과정에서 binary 데이터 손실을 막기위해
- 이미지, video 를  ASCII로 encoding 하여 전송하게 되면 여러가지 문제 발생 가능성 있음
- Binary Data가 시스템 독립적으로 동일하게 전송 또는 저장되는 걸 보장하기 위해 사용
