## SQL 04

### HackerRank SQL - Medium (9/16)

[HackerRank - Top Competitors](https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true)


**JOIN** 
``` 
SELECT h.hacker_id, h.name
FROM Submissions s
INNER JOIN Challenges c ON c.challenge_id = s.challenge_id
INNER JOIN Difficulty AS d ON c.difficulty_level = d.difficulty_level
INNER JOIN Hackers AS h ON h.hacker_id = s.hacker_id
WHERE s.score = d.score AND c.difficulty_level = d.difficulty_level
GROUP BY h.hacker_id, h.name
HAVING COUNT(h.hacker_id) > 1
ORDER BY COUNT(h.hacker_id) DESC, h.hacker_id ASC;

```

- JOIN 을 먼저 한 칼럼을 활용해서 바로 아래 추가로 조인이 가능하다
- Group by 는 SELECT문에 사용한 칼럼을 모두 포함하고 있어야 한다

<br />

### HackerRank SQL - Medium (10/16)

[HackerRank - The Report](https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true)


**JOIN** 
``` 
SELECT CASE 
WHEN g.grade >=8 THEN s.Name
ELSE NULL END, 
g.grade,
s.Marks
FROM Students s
INNER JOIN Grades g ON (s.Marks >= g.Min_Mark AND s.Marks <= g.Max_Mark)
ORDER BY g.Grade DESC, s.Name, s.Marks

```

- JOIN ON 을 활용해서 범위에 해당하는 값을 할당

<br />


### Leetcode SQL (7/50)
[595. Big Countries](https://leetcode.com/problems/big-countries/)

**WHERE**

``` 
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;

``` 
- Nothing Special

</Br>

### Leetcode SQL (8/50)
[176. Second Highest Salary](https://leetcode.com/problems/second-highest-salary/)

****

``` 
WITH t AS (SELECT *, DENSE_RANK() OVER(ORDER BY salary desc) as 'r'
FROM Employee)

SELECT CASE WHEN r = 2 THEN salary ELSE NULL END AS 'SecondHighestSalary'
FROM t
ORDER BY SecondHighestSalary DESC
LIMIT 1
;

``` 
- Alias 는 sql 명령어가 아닌 것들로 지정해주어야 한다
- Order by 에서 DESC 해주어야 한다

</Br>

