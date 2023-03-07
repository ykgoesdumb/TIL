### Leetcode SQL (16/50)
[626. Exchange Seats](https://leetcode.com/problems/exchange-seats/)

**MOD**

``` 
SELECT CASE WHEN id%2 = 1 AND id NOT IN (SELECT MAX(id) FROM Seat) 
            THEN id+1
            WHEN id%2 = 1 AND id IN (SELECT MAX(id) FROM Seat) 
            THEN id
            ELSE id - 1 END as id, student
FROM Seat
ORDER BY id;

``` 
- 

</Br>

### Leetcode SQL (17/50)
[619. Biggest Single Number](https://leetcode.com/problems/biggest-single-number/?envType=study-plan&id=sql-ii)

**CASE WHEN**

``` 
SELECT CASE WHEN COUNT(*) = 1 THEN num ELSE null END AS num
FROM MyNumbers
GROUP BY num
ORDER BY num DESC
LIMIT 1;
``` 
- SQL Basic Syntax FROM > JOIN > ON > WHERE > GROUP BY > HAVING > ORDER BY > LIMIT

</Br>


### Leetcode SQL (18/50)
[1112. Highest Grade For Each Student](https://leetcode.com/problems/highest-grade-for-each-student/description/?envType=study-plan&id=sql-ii)

**DENSE RANK()**

``` 
SELECT e1.student_id, e1.course_id, e1.grade
FROM(
SELECT student_id, course_id, grade, DENSE_RANK() OVER (partition by student_id order by grade DESC, course_id ASC) AS top
FROM Enrollments
) AS e1
WHERE e1.top = 1
GROUP BY e1.student_id;
``` 
- Window function 활용법을 다시 한 번 숙지

</Br>

### Leetcode SQL (19/50)
[1398. Customers Who Bought Products A and B but Not C](https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/?envType=study-plan&id=sql-ii)

**DENSE RANK()**

``` 
SELECT e1.student_id, e1.course_id, e1.grade
FROM(
SELECT student_id, course_id, grade, DENSE_RANK() OVER (partition by student_id order by grade DESC, course_id ASC) AS top
FROM Enrollments
) AS e1
WHERE e1.top = 1
GROUP BY e1.student_id


``` 
- Window function 활용법을 다시 한 번 숙지

</Br>