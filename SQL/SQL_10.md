### Leetcode SQL (40/50)
[1934. Confirmation Rate](https://leetcode.com/problems/confirmation-rate/description/)

**CTE, Window Function**

``` 
WITH CTE AS(
SELECT user_id, SUM(IF(action = 'confirmed', 1 ,0)) OVER (PARTITION BY user_id) AS ccount, COUNT(*) OVER(PARTITION BY user_id) AS uccount
FROM Signups
LEFT JOIN Confirmations USING(user_id)
)

SELECT user_id, ROUND(ccount/uccount,2) as confirmation_rate
FROM CTE
GROUP BY user_id
``` 

```
SELECT user_id, CASE WHEN action IS NULL THEN 0.00 ELSE SUM(action = 'confirmed')/COUNT(*) END AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations USING(user_id)
GROUP BY user_id
```
- CTE is easy but try to solve without partition by when possible.
- 2nd solution is 10 time faster than the first one due to CTE and window fucntions

### Leetcode SQL (41/50)
[###.problem title](URL)

**CTE&Window Function**

``` 
WITH CTE AS (SELECT *, AVG(quantity) average, MAX(quantity) AS max
FROM OrdersDetails
GROUP BY order_id)

SELECT distinct(order_id)
FROM CTE
WHERE max > (SELECT MAX(average) FROM CTE)
``` 

```
WITH CTE AS (SELECT *, MAX(AVG(quantity)) OVER() average, MAX(quantity) AS maxq
FROM OrdersDetails
GROUP BY order_id)

SELECT DISTINCT order_id
FROM CTE
WHERE maxq > average
```
- Logically did not make sense to find max average... that's why it's not a popular problem I guess
- Use as less partition by as possible if can be solved with group by

### Leetcode SQL (42/50)
[1077. Project Employees III](https://leetcode.com/problems/project-employees-iii/description/)

**CTE, WINDOW FUNCTION**

``` 
WITH CTE AS(SELECT *, MAX(experience_years) OVER(PARTITION BY project_id) AS maxexp
FROM Project
JOIN Employee USING(employee_id))

SELECT project_id, employee_id
FROM CTE
WHERE experience_years = maxexp
``` 
- Am now used to CTE and Window Funciton :) Very fast!

### Leetcode SQL (43/50)
[2238. Number of Times a Driver Was a Passenger](https://leetcode.com/problems/number-of-times-a-driver-was-a-passenger/description/)

**Join**

``` 
WITH CTE AS(SELECT *, COUNT(*)OVER(PARTITION BY passenger_id) AS pcount
FROM Rides)

SELECT r.driver_id, IF(c.pcount IS NULL, 0, c.pcount) AS cnt
FROM Rides r
LEFT JOIN CTE c ON r.driver_id = c.passenger_id 
GROUP BY r.driver_id
``` 
- Filtering using join is an essential skill

### Leetcode SQL (44/50)
[1355. Activity Participants](https://leetcode.com/problems/activity-participants/description/)

**GROUP BY**

``` 
WITH CTE AS (SELECT *, COUNT(activity) as cnt
FROM Friends
GROUP BY activity)

SELECT activity
FROM CTE
WHERE cnt NOT IN (SELECT MAX(cnt) FROM CTE) AND cnt NOT IN (SELECT MIN(cnt) FROM CTE)


``` 
- Need to clearly understand what group by limits and why group function is not working when using between

### Leetcode SQL (45/50)
[1709. Biggest Window Between Visits](https://leetcode.com/problems/biggest-window-between-visits/description/)

**Learning Point**

``` 
WITH CTE AS(SELECT *, LEAD(visit_date) OVER(PARTITION BY user_id ORDER BY visit_date) AS last_date
FROM UserVisits)

, CTE2 AS(SELECT *, CASE WHEN last_date IS NULL THEN DATEDIFF(DATE('2021-01-01'),visit_date) ELSE DATEDIFF(last_date,visit_date) END AS windows
FROM CTE)

SELECT user_id, MAX(windows) AS biggest_window
FROM CTE2
GROUP BY user_id
;

``` 
- Note

### Leetcode SQL (46/50)
[###.problem title](URL)

**ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW**

``` 
WITH CTE AS (SELECT *, SUM(weight) OVER(ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total
FROM Queue)


SELECT person_name
FROM CTE
WHERE total <= 1000
ORDER BY total DESC
LIMIT 1;
``` 
- Note

### Leetcode SQL (47/50)
[1112. Highest Grade For Each Student](https://leetcode.com/problems/highest-grade-for-each-student/description/)

**ORDER BY**

``` 
WITH CTE AS(SELECT * , RANK()OVER(PARTITION BY student_id ORDER BY grade DESC, course_id ASC) as cr
FROM Enrollments)

SELECT student_id, course_id, grade
FROM CTE
GROUP BY student_id
``` 
- ORDER BY can be priortized by its order

```
WITH CTE AS( SELECT *, MAX(grade)OVER(PARTITION BY student_id) as highest
FROM Enrollments)

SELECT student_id, MIN(course_id) AS course_id, grade
FROM CTE
WHERE grade = highest
GROUP BY student_id
ORDER BY student_id
```

- Much faster approach, bring all options and match with max score and bring smallest course_id

### Leetcode SQL (48/50)
[608. Tree Node](https://leetcode.com/problems/tree-node/description/)

**CASE**

``` 
SELECT id, CASE WHEN p_id IS NULL THEN 'Root' WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner' ELSE 'Leaf' END type 
FROM Tree
``` 
- CASE clause considers its order IS NULL comes before IN therefore even 1 is IN the group, still NULL comes first so it is assigned as 'Root' rather than 'Inner'

### Leetcode SQL (49/50)
[###.problem title](URL)

**Learning Point**

``` 
WITH CTE1 AS (SELECT visited_on, SUM(amount) AS amount
FROM Customer
GROUP BY visited_on)

,CTE2 AS(SELECT *, SUM(amount) OVER(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma, COUNT(*) OVER(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS cnt
FROM CTE1)

SELECT visited_on, ma AS amount, ROUND(ma/cnt,2) AS average_amount
FROM CTE2
WHERE cnt = 7
``` 
- Taking Step by step is the key
- Be familiar with ROWS BETWEEN n(OR UNBOUNDED) PRECEDING AND CURRENT ROW for aggregation among window function/ range window