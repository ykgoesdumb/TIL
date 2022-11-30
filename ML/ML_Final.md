# Week 02 Probability Basic & Information Theroy 

## From Probability to Information Theory

- Attribute 간의 관계를 정의하기 위해선 하나의 attribute 가 얼마나의 정보를 가지고 있는지 파악하는 것이 중요하다.
- 정보란 충격 (surprise)와 같다. Expectation - realization = 정보 (충격쓰!)



## Information Theory
How do we measure those information?
- Measure the uncertainty: How it is difficult to make prediction without the attribute & with the attribute
- The level of difficulty, uncertainty making the prediction is what we call **Entrophy**
- The difference in uncertainty is what we call **Information Gain**

Entrophy 를 계산 할 때 밑이 2인 로그를 활용
- Entropy of X (Level of disorder) 

    $\displaystyle H(x)= H(p_1,p_2,p_3..) = -{\mathrm {} }\sum _{i}p_{i}\log _2 p_{i}$
- 왜 앞에 minus (-)가 있을까? 
```
    P 가 숫자 0 - 1 사이의 소수이니 로그를 계산하면 음수가 된다. 그러므로 앞에 (-) 를 붙여준다. 
```

- 앤트로피가 높으면 좋은걸까 나쁜걸까? 

    앤트로피가 높으면 High uncertainty, so it is not good.

- 그렇다면 두가지 확률이 주어질 때 가장 Entrophy 가 높을 때는 두 확률이 50:50 일 때이다. (무엇을 골라야 할 지 모르기 때문)

```
Information Gain is mutual: 
I(X;Y) = Y의 정보가 주어질 때 X 정보의 변화
I(X;Y) = H(X) - H(X|Y)
I(X;Y) = H(Y) - H(Y|X) = I(Y;X)

만약 X 와 Y가 독립적 (상관관계가 전혀 없을 때) 이라면
H(Y|X) = H(Y)
I(X;Y) = 0

H(X|Y) 에서 Information Gain = 1 - H(X|Y)
```

Gain Ratio 
- Measures the information gain relative to the entropy of the attribute
- G(X;Y) = I(X;Y)/H(Y)
- G(X;Y) != G(Y;X)

## Preparing Data



