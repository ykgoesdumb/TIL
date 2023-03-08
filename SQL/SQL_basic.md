# SQL BASIC

## 좋은 SQL 습관

- 예약어는 대문자로 (SELECT, WHERE, GROUP BY)
- 행갈이는 자주자주
- 주석 쓰기 ‘ — ’
- ALIAS 잘쓰기 (group -> g)


## SQL 순서

- SELECT   5.

- FROM    1. 

- WHERE   2.

- GROUP BY   3.

- HAVING   4.

- ORDER BY   6.

*** Mysql 에서는 HAVING (4) 절에서 SELECT (5) 절에서 정의한 ALIAS 를 예외적으로 쓸 수 있다***


## SQL FUNCTIONS
너무 기본적인 것은 skip하였음

### 짝수, 홀수 (MOD)

```SQL
--짝수
SELECT City 
FROM Station
WHERE MOD(ID,2) = 0

--홀수
SELECT City
FROM Station
WHERE MOD(ID,2) = 1

--중복없이 ID 가 짝수인것 뽑기

SELECT DISTINCT City 
FROM Station
WHERE MOD(ID,2) = 0

**mysql 에선
WHERE id%2=0 
```

### 가장 짧은 이름 과 가장 긴 이름 출력하기 (LENGTH)

```
예상 출력 값
Korea 5
America 7


가장 짧은 이름
SELECT city c,
			 length(city) l
FROM station
ORDER BY l ASC, c ASC
LIMIT 1;

가장 긴 이름
SELECT city c,
			 length(city) l
FROM station
ORDER BY l DESC, c ASC
LIMIT 1;
```

### REGEXP 로 복잡한 조건 

```SQL
문제: 모음 [a,e,i,o,u] 로 시작하는 City 이름 출력하기

like 로 일일히 선정하는 방법도 있으나
더 간편하게 만들어보자

SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[aeiou]'
```


### RIGHT,LEFT,MID

- MYSQL 에는 구현되어있으나 타 db 에서는 구현되어있지않음
  - LEFT : 문자에 왼쪽을 기준으로 일정 갯수를 가져오는 함수.
  - MID : 문자에 지정한 시작 위치를 기준으로 일정 갯수를 가져오는 함수.
  - RIGHT : 문자에 오른쪽을 기준으로 일정 갯수를 가져오는 함수.

- MID 는 SUBSTR, SUBSTRING 과 동일하게 동작함

```SQL
--LEFT

SELECT LEFT('abcdefg', 3);
--RESULT : abc

--MID
SELECT MID('abcdefg', 2, 4);
--RESULT : bcde
--SUBSTR('abcdefg', 2, 4) 와 동일

--RIGHT
SELECT RIGHT('abcdefg', 3);
efg
```


### REPLACE

```sql
문제: 월급 계산중 숫자 '0' 이 다 없어짐, 평균 월급 - 잘못계산한 평균월급 구하고, 올림 하기

올림은 CEIL
내림은 FLOOR

select CEIL(AVG(salary) - AVG(REPLACE(salary, '0', '')))
from employees
```


### CONCAT

```sql

문제: 월급 * 개월수 = total earning 이라고 할때
		최댓값 과 그 값과 동률인 사람의 수를 2 space-separated integer 로 나타내라.

select concat(max(salary * months),' ', count(salary * months)) from Employee
where (salary * months) = (select max(salary * months) from Employee)

Your Output
108064 7
```

### MEDIAN

- 오라클과 Mysql 과 방법이 다르다
- 오라클은 median functinon 이 있기 때문에 쉽다.

```sql

SELECT ROUND(MEDIAN(LAT_N,4)
FROM STATION;

MYSQL 은 median 이 없으므로

SELECT ROUND(LAT_N,4)
FROM (SELECT LAT_N, PERCENT_RANK() OVER (ORDER BY LAT_N) percent
     FROM STATION) abc
WHERE percent = 0.5;
```

### INNER JOIN 조건으로 범위(BETWEEN 사용)

```sql
SELECT 
    IF(g.grade >= 8, s.name, 'NULL'),
    g.grade,
    s.marks
FROM students s
INNER JOIN grades g
ON s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY g.grade DESC, s.name, s.marks
```

### GROUP BY 와 HAVING

```sql
Hacker 들 중 2개 이상 challenge 에서 만점을 받은 hacker 들의 ID, 와 이름 을 출력하고
만점을 받은 총 challenge 갯수 내림차순으로 정렬하고 동률이 나올 시, hacker ID 오름 차순으로 정렬
 

SELECT h.hacker_id
    ,  h.name
FROM submissions s
INNER JOIN hackers h ON s.hacker_id = h.hacker_id
INNER JOIN challenges c ON s.challenge_id = c.challenge_id
INNER JOIN difficulty d ON c.difficulty_level = d.difficulty_level
WHERE s.score = d.score AND
      c.difficulty_level = d.difficulty_level
GROUP BY h.hacker_id, h.name
HAVING COUNT(h.hacker_id) > 1
ORDER BY COUNT(h.hacker_id) DESC, h.hacker_id
```

### SELFJOIN INNERJOIN

```sql
SELECT w.id
    , p.age
    , w.coins_needed
    , w.power
FROM wands_property p
INNER JOIN wands w ON p.code = w.code
WHERE p.is_evil = 0 
AND w.coins_needed = (SELECT MIN(w1.coins_needed)
                      FROM wands w1
                      INNER JOIN wands_property p1 ON w1.code = p1.code
                      WHERE p1.is_evil = 0
                      AND w1.power = w.power
                      AND p1.age = p.age)
ORDER BY w.power DESC, p.age DESC;
```

### SELFJOIN (중복 제거)

```sql
//GROUP BY 를 통해 중복을 제거하였다

SELECT a.company, a.num
FROM route a
JOIN route b 
  ON a.num = b.num
WHERE a.stop = '230' AND 
      b.stop = '53' 
GROUP BY a.company,a.num
```

### SUBQUERY

```sql
SELECT h.hacker_id
    , h.name
    , COUNT(c.challenge_id) chal_count
FROM hackers h
INNER JOIN challenges c 
        ON h.hacker_id = c.hacker_id
GROUP BY c.hacker_id, h.name
HAVING chal_count = (SELECT MAX(tmp1.cnt)
                     FROM (SELECT COUNT(challenge_id) cnt
                           FROM challenges
                           GROUP BY hacker_id) tmp1)
    OR chal_count NOT IN 
                    (SELECT MAX(tmp2.cnt)
                     FROM (SELECT COUNT(challenge_id) cnt
                           FROM challenges
                           GROUP BY hacker_id) tmp2
                     GROUP BY tmp2.cnt
                     HAVING COUNT(tmp2.cnt) >= 2)
                     
ORDER BY chal_count DESC, h.hacker_id
```

### JOINNING  2  SELF-JOINED SUBQUERIES

```sql

버스 노선 데이터가 쭉 나와있다 (출발지, 도착지 정보만) 
'Craiglockhart' 에서 'Lochend' 까지 직행은 없고 최소 2번 갈아타야한다고 가정했을때
가는 모든 방법을 구하고 첫번째 차량번호, 차량 회사, 환승역 이름, 두번째 차량번호, 회사 를 출력 

SELECT t1.num, t1.company, t1.name2, t2.num, t2.company

FROM
    (SELECT DISTINCT a.num, 
            a.company, 
            stopa.id id1, 
            stopa.name name1,
            stopb.id id2, 
            stopb.name name2
        FROM route a
        JOIN route b 
          ON a.num = b.num AND
             a.company = b.company
        JOIN stops stopa ON a.stop = stopa.id  
        JOIN stops stopb ON b.stop = stopb.id
        WHERE stopa.name = 'Craiglockhart') t1
INNER JOIN 
    (SELECT DISTINCT a.num, 
            a.company, 
            stopa.id id1, 
            stopa.name name1, 
            stopb.id id2, 
            stopb.name name2 
        FROM route a
        JOIN route b 
          ON a.num = b.num AND
             a.company = b.company
        JOIN stops stopa ON a.stop = stopa.id  
        JOIN stops stopb ON b.stop = stopb.id
        WHERE stopb.name = 'Lochend') t2
    ON t1.id2 = t2.id1
```

### CASE

```sql
SELECT CASE
    WHEN a = b AND b = c THEN 'Equilateral'
    WHEN a>=b+c OR b>=a+c OR c>=a+b THEN 'Not A Triangle'
    WHEN a = b OR b = c OR a = c THEN 'Isosceles'
    ELSE 'Scalene' END AS tri_form
FROM triangles
```

### SET 과 CASE 그리고 SUBQUERY

해설: [https://techblog-history-younghunjo1.tistory.com/159](https://techblog-history-younghunjo1.tistory.com/159)

```sql
SET @D=0, @P=0, @S=0, @A=0;

-- 문자열의 알파벳순서에서 최솟값(MIN)은 A(a)로 시작하는 것을 추출해줌!
SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM (SELECT CASE WHEN Occupation = 'Doctor' THEN Name END AS Doctor,
             CASE WHEN Occupation = 'Professor' THEN Name END AS Professor,
             CASE WHEN Occupation = 'Singer' THEN Name END AS Singer,
             CASE WHEN Occupation = 'Actor' THEN Name END AS Actor,
             CASE
             WHEN Occupation = 'Doctor' THEN (@D:=@D+1)
             WHEN Occupation = 'Professor' THEN (@P:=@P+1)
             WHEN Occupation = 'Singer' THEN (@S:=@S+1)
             WHEN Occupation = 'Actor' THEN (@A:=@A+1)
             END AS RowNumber
       FROM Occupations
       ORDER BY Name) sub
GROUP BY RowNumber
```

### COALESCE

```sql
배타적 OR 관계 열에서 활용도가 높다
지정한 표현식들 중에 NULL이 아닌 첫 번째 값을 반환한다.

// NULL 처리 상황
SELECT COALESCE(Column명1, Column명1이 NULL인 경우 대체할 값)
FROM 테이블명

// 배타적 OR 관계 열
// Column1 ~ 4 중 NULL이 아닌 첫 번째 Column을 출력
SELECT COALESCE(Column명1, Column명2, Column명3, Column명4)
FROM 테이블명

// NAME Column의 값이 NULL인 경우 다음 표현식으로 넘어간다.
// 다음 표현식인 "No name"이 Null이 아니므로 "No name"을 출력.
SELECT COALESCE(NAME, "No name")
FROM ANIMAL_INS
```

## CAST, CONVERT

- 형 변환 함수

<aside>
💡 **지정할 수 있는 데이터 타입**

BINARY[(N)]

CHAR[(N)] [charset_info]

DATE

DATETIME

DECIMAL[(M[,D])]

JSON

NCHAR[(N)]

SIGNED [INTEGER]

TIME

UNSIGNED [INTEGER]

</aside>

```sql
--CAST 로 현재 시간을 SIGNED type 으로 변환
SELECT CAST(NOW() AS SINGED);

--CONVERT
SELECT CONVERT(NOW(), SINGED);

--숫자를 날짜 타입으로 변환
SELECT CAST(20220502 AS DATE);
> 2022-05-02
SELECT CONVERT(20220502, DATE);
> 2022-05-02

```

## WINDOW 함수

---

### PARTITION BY

```sql
기본형태
함수(함수_적용_열) OVER (PARTITION BY 그룹열 ORDER BY 순서열)

SELECT empno
		,  ename
		,  job
		,  SUM(sal) OVER(PARTITTION BY job)
	FROM emp
WHERE job IN ('MANAER', 'SALESMAN')
ORDER BY job
```

### 순위

- ROW_NUMBER() = 중복 없는 순위, 행 번호
- RANK() = 중복 가능, 공동순위만큼 건너뜀
- DENSE_RANK()
    - 중복가능
    - 공동순위 있더라도 1, 2, 3 순차적으로 순위 결정
    - 동일한 순위는 하나의 순위로 취급
    

```sql
SELECT
		, ROW_NUMBER() OVER (ORDER BY val) AS 'row_num'
		, RANK() OVER (ORDER BY val) AS 'rank'
		, DENSE_RANK OVER (ORDER BY val) AS 'dense_rank'
FROM table
```



### LAG, LEAD (데이터 위치 n 칸 밀고 당기기)

- LAG(컬럼, n, 결측값 채울값) OVER(PARTITION BY 그룹열 ORDER BY 순서열)
- LEAD(컬럼, n, 결측값 채울값) OVER(PARTITION BY 그룹열 ORDER BY 순서열)

```sql
SELECT ID
		,  RecordDate  --order 의 기준 열
		,  Temperature -- 밀고 당길 대상 열
    ,  LAG(Temperature) OVER (ORDER BY RecordDate) AS 'lag'
		,  LEAD(Temperature) OVER (ORDER BY RecordDate As 'lead'
FROM table
```

