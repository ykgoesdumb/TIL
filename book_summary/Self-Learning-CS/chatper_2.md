# 2. 데이터
## 2-1 0과 1로 숫자를 표현하는 방법

### 정보 단위
- bit
- byte
- mega byte
- giga byte
- terra byte  .....


### word
- CPU 가 한번에 처리할 수 있는 데이터 크기
- CPU 가 한번에 16비트를 처리할 수 있다면 1 워드는 16비트가 됨
- half word, full word, double word\
- 현대 컴퓨터의 워드 크기는 대부분 32bit 아니면 64bit

### 이진수의 음수 표현

- 이진수의 양수 표현은 그냥 이진법
- 음수 표현은 2의 보수 
  - 어떤 수를 그것보다 큰 2^n 에서 뺀값
  - 양수의 0 과 1 을 다 뒤집고 1을 더한 값 이 양수 -> 음수 전환
  - 음수 -> 양수 로 전환할때도 동일하게 해준다

- 컴퓨터는 음수와 양수의 구분을 '플래그' 로 한다

- 이 방식에는 명확한 한계점도 있음 
  - n 비트로는 2^n 과 - 2^n 을 동시에 나타낼 수 없다


### 십육진수

- 0~9, A~F 로 정보를 표현
- 10이 넘어가는 단위는 숫자앞에 0x 를 붙여서 구분한다
  - 십육진수 15 표기 = 0x15
- 십육진수와 이진수가 상호 변환이 쉽다

- 십육진수의 한 글자를 4비트의 이진수로 간주
- 1A2B = 0001 1010 0010 1011
---
## 2-2 0과 1로 문자를 표현하는 방법

- 0 과 1 로 문자를 표현하는 핵심은 아래와 같다
  - 문자 집합
    - 컴퓨터가 인식하고 표현할 수 있는 문자의 모음
  - 인코딩
    - 문자를 0과 1로 변환하는 과정
  - 디코딩
    - 0과 1을 사람이 이해할 수 있는 문자로 변환하는 과정


## ASCII
- 초창기 문자 집합중 하나
- 영어 알파벳, 아라비아 숫자, 특수 문자 포함
- 하나의 아스키 문자를 나타내기 위해 8비트 사용
  - 이중 1비트는 오류 검출을 위해 사용되는 비트 (parity bit)
  - 실질적으로 사용되는건 7bit

- backspace, space, cancel, del, escape 같은 것도 포함되어있다


### ASCII 의 단점
- 한글 표현 못함
- 7 비트로 표현하기 때문에 128이상 늘릴 수 없음


## EUC - KR

한글을 인코딩하는 방식

- 완성형 인코딩
  - 완성된 하나의 글자에 고유한 코드를 부여
- 조합형 인코딩
  - 초성 중성 종성 코드를 합하여 하나의 글자코드를 만듬

- EUC - KR 은 '완성형 인코딩'

- 인코딩된 한글 한글자를 표현하려면 16 비트 필요
  - 16진수로 표현 가능

- 총 2350개 한글단어 표현 가능
  - 모든 한글 조합 표현 불가
  - 쀍 뾇 같은 단어 표현 안됨


## 유니코드 UTF-8
- 언어별로 인코딩을 나라마다 해야한다면 너무 번거로울 것
    - 모든 언어를 아우르는 문자 집합과 통일된 표준 인코딩 방식이 있다면? 

- 등장한 새로운 문자 집합 '유니코드'
    - 아스키나 EUC-KR 은 글자에 부여된 값을 그대로 인코딩 값으로 삼았음
    - 유니코드는 부여된 값 자체를 인코딩된 값으로 삼지 않고 다양한 방법으로 인코딩
      - UTF-8, UTF-16, UTF-32 (Unicode Transformation Format)






