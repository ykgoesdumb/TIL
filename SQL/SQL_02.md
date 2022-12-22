## SQL 02

### HackerRank SQL - Medium (1/16)

[HackerRank - The PADS](https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true)


**CONCAT, GROUP BY, ORDER BY, LEFT** 
``` 
SELECT CONCAT(name, '(', LEFT(occupation,1), ')')
FROM OCCUPATIONS
ORDER BY name;

SELECT CONCAT('There are a total of ',COUNT(occupation),' ',LOWER(occupation),'s.')
FROM OCCUPATIONS
GROUP BY occupation
ORDER BY COUNT(occupation), occupation;

```

- CONCAT 을 사용 할 때는 항상 띄어쓰기를 주의
- 특별한 것 없는 문제

<br />


### HackerRank SQL - Medium (2/16)
[HackerRank - Placements](https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true)

**CTE, Multiple Joins**
```
WITH Friend_Salary AS (SELECT f.ID, f.Friend_ID, p.Salary 
FROM Friends f
JOIN Packages p ON f.Friend_ID = p.ID
ORDER BY f.ID)

SELECT s.Name
FROM Students s
LEFT JOIN Friends f ON s.ID = f.ID
LEFT JOIN Packages p ON s.ID = p.ID
LEFT JOIN Friend_Salary fs ON s.ID = fs.ID
WHERE p.Salary < fs.Salary
ORDER BY fs.Salary;
```

- CTE 를 활용해서 Friend_ID 와 ID를 맞추는 것이 포인트
- 연속해서 Join을 활용 할 수 있다


### Leetcode - (6/50)
[180. Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/)

**SELF JOIN**

```
SELECT DISTINCT a.num
FROM Logs a
JOIN Logs b ON a.id = b.id + 1 AND a.num = b.num
JOIN Logs c ON a.id = c.id + 2 AND a.num = c.num
;


```
- 같은 컬럼, 특히 가까운 칼럼끼리의 값 비교는 SELF JOIN으로 많이 풀어낸다.
- 한 칸씩 더한 값을 비교해주기

### Leetcode - (7/50)
[184. Department Highest Salary](https://leetcode.com/problems/department-highest-salary/)

**Rank, IN, Alias**

```
# 풀이 1
SELECT d.name AS Department, e.name AS Employee, e.salary as Salary
FROM Employee e
INNER JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId,e.salary) IN (SELECT departmentId, MAX(salary)
FROM Employee
GROUP BY departmentID);
```
- Filtering 할 때 서브쿼리가 2개 이상일 경우 WHERE, IN clause 에 두개의 attribute를 포함 시켜야 함

```
# 풀이 2
SELECT t.Department, t.Employee, t.Salary
FROM
(SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary, rank() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS 'Rank'
FROM Employee e
INNER JOIN Department d ON e.departmentId = d.id) AS t
WHERE t.Rank = 1;
```
- Alias 사용법 확실히 알아두기
- Alias 사용 할 때 따옴표