## if 문

shell script 의 if 문은 아래의 형식을 따른다

```sh
if [ 첫번째 조건]
then 
    수행문

elif [두번째 조건]

then
    수행문
else
    수행문
fi
```


### if[연산자 $변수]

-z 는 변수의 저장된 값의 길이가 0인지를 비교하여 0이면 true

```sh

#!/bin/bash

value=""

if [-z $value]
then
    echo True
else
    echo False
fi
```


### if[조건식]연산자[조건식]; then

- -gt 는 greater than
- -lt 는 less than
- &&는 and 연산

```sh
#!/bin/bash

value = 5

