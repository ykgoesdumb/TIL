## SQL 03

### HackerRank SQL - Medium (3/16)

[HackerRank - Binary Tree Nodes](hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true)


**CASE** 
``` 
SELECT N, 
    CASE 
        WHEN P IS NULL 
        THEN 'Root' 
        WHEN N NOT IN (SELECT P FROM BST WHERE P IS NOT NULL)
        THEN 'Leaf'
        ELSE 'Inner' 
    END
FROM BST
ORDER BY N;
```

- 집합에서 IN 으로 value 찾을 때는 다시 SELECT로 집합을 명시해 줄 것 

<br />


### HackerRank SQL - Medium (4/16)

[HackerRank - Occupations](https://www.hackerrank.com/challenges/occupations/problem)

**WINDOW FUNCTION, CTE, GROUP BY**

```
WITH temp AS (
SELECT *, ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS 'rn'
FROM OCCUPATIONS)

SELECT 
MAX(CASE WHEN Occupation = 'Doctor' THEN temp.Name END) AS 'Doctor',
MAX(CASE WHEN Occupation = 'Professor' THEN temp.Name END) AS 'Professor',
MAX(CASE WHEN Occupation = 'Singer' THEN temp.Name END) AS 'Singer',
MAX(CASE WHEN Occupation = 'Actor' THEN temp.Name END) AS 'Actor'

FROM temp

GROUP BY rn;
```

- Aggregate function을 활용해야 Group by 가 가능하다.
- Aggregate function을 활용해야 Value 가 없는 곳에 NULL로 채워 놓을 수 있다.

</Br>

## HackerRank SQL - Medium (5/16)
[HackerRank - New Companies](https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true)

**GROUP BY, COUNT DISTINCT**
```
SELECT Company_code, Founder, COUNT(DISTINCT lead_manager_code), COUNT(DISTINCT senior_manager_code), COUNT(DISTINCT manager_code), COUNT(DISTINCT employee_code)
FROM Employee
LEFT JOIN Company USING(company_code)
GROUP BY company_code, founder
ORDER BY Company_code;
```

- Group By 를 어떻게 해야 하나가 포인트
- 문제를 천천히 잘 읽고 Distinct를 잊지말자

</Br>

## HackerRank SQL - Medium (6/16)
[HackerRank - Weather Observation Station 18](https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true)

**ROUND, ABS**

```
SELECT  ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)),4)
FROM STATION;
```
- ROUND 함수와 ABS 함수를 사용해 본다
- 특별한 것 없는 문제

</Br>

## HackerRank SQL - Medium (7/16)

[HackerRank - Weather Observation Station 19](https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true)

**SQRT, POWER**

```
SELECT ROUND(
    SQRT(POWER((MAX(LAT_N) - MIN(LAT_N)),2) + POWER((MAX(LONG_W) - MIN(LONG_W)),2))
         ,4)
FROM STATION
```
- SQRT 함수와 POWER 함수를 사용해 본다
- 특별한 것 없는 문제

</Br>

## HackerRank SQL - Medium (8/16)
**WINDOW FUNCTION, OVER, Median**

[HackerRank - Weather Observation Station 20](https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true)

```
WITH t AS(SELECT *, ROW_NUMBER() OVER(ORDER BY LAT_N) AS rn, COUNT(LAT_N)over() AS rc
FROM STATION)

SELECT ROUND(t.LAT_N,4)
FROM t
WHERE rn IN (rc/2,(rc+1)/2)

```
- Mysql 에는 median funciton이 없으므로 count가 홀수 짝수 일 때를 고려하여 필터링 해주어야 한다.
- SELECT 문에서 aggregate function은 OVER 절을 활용 (Count는 단일함수지만 Window function과 함께 사용함으로 OVER 절을 활용)

</Br>