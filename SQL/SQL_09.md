### Leetcode SQL (30/50)
[1308. Running Total for Different Genders](https://leetcode.com/problems/running-total-for-different-genders/description/)
**PARTITION BY WITH ORDER BY **

``` 
SELECT gender, day, 
       SUM(score_points) OVER(PARTITION BY gender ORDER BY day) AS total
FROM Scores;
``` 
- Partition by sets the window by group (partition) and order by followed orders the partition in certain rules
- ORDER BY day is followed by the PARTITION BY gender, gender aggregation splits into days due to former reason

### Leetcode SQL (31/50)
[1285. Find the Start and End Number of Continuous Ranges](https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/description/)
**Continuous Value & ROW_NUMBER**

``` 
WITH CTE AS(SELECT log_id, ROW_NUMBER()OVER() AS rn
FROM Logs)

SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM CTE
GROUP BY (log_id - rn)
;
``` 
- Continuous value can be calculated by substracting a row_number columns and group by the result

### Leetcode SQL (32/50)
[1270. All People Report to the Given Manager](https://leetcode.com/problems/all-people-report-to-the-given-manager/description/)
**JOIN FOR RELATIONSHIPS**

``` 
WITH CTE AS(
SELECT e1.employee_id AS e1emp, e1.manager_id AS e1mng, e2.manager_id AS 21mng, e3.manager_id AS e3mng
FROM Employees e1
LEFT JOIN Employees e2 ON e1.manager_id = e2.employee_id
LEFT JOIN EMployees e3 ON e2.manager_id = e3.employee_id)

SELECT e1emp AS employee_id
FROM CTE
WHERE e3mng = 1 AND e1emp != 1;
``` 
- In order to know the relationship between managers and employees, we need keep left join to see who reports to whom

### Leetcode SQL (33/50)
[1699. Number of Calls Between Two Persons](https://leetcode.com/problems/number-of-calls-between-two-persons/description/)
**GROUP BY**

``` 
SELECT IF((from_id - to_id) <0, from_id, to_id) AS person1, IF((from_id - to_id) >0, from_id, to_id) AS person2, COUNT(*) AS call_count, SUM(duration) as total_duration
FROM Calls
GROUP BY person1, person2;
``` 
- Sort the columns into two sides and group them with COMMA
- Don't forget to sum the duration since GROUP BY do not sum it automatically

### Leetcode SQL (34/50)
[1596. The Most Frequently Ordered Products for Each Customer](https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer/description/)
**Learning Point**

``` 
# Write your MySQL query statement below
WITH CTE AS (SELECT customer_id, product_id, COUNT(*) as cnt
FROM Orders
GROUP BY customer_id, product_id
ORDER BY customer_id), 

  CTE2 AS (SELECT *, MAX(cnt) OVER(PARTITION BY customer_id) as most_frequent
FROM CTE)

SELECT c2.customer_id, c2.product_id, p.product_name
FROM CTE2 c2
INNER JOIN Products p ON c2.product_id = p.product_id
WHERE cnt = most_frequent
;
``` 
- When solving the problem step by step would help
- Don't hesitate to split CTE when select can't be solved by 1 quary

### Leetcode SQL (35/50)
[1831. Maximum Transaction Each Day](https://leetcode.com/problems/maximum-transaction-each-day/description/)
**CTE, DATE**

``` 
WITH CTE AS (SELECT transaction_id, DATE(day) as date, amount, MAX(amount) OVER(PARTITION BY DATE(day)) as maxa
FROM Transactions
ORDER BY date)

SELECT  transaction_id
FROM CTE
WHERE amount = maxa
ORDER BY transaction_id;
``` 
- Being familiar with DATE function is important
- CTE is awesome

### Leetcode SQL (36/50)
[1468. Calculate Salaries](https://leetcode.com/problems/calculate-salaries/description/)
**ROUND, CASE, WINDOW**

``` 
WITH CTE AS (SELECT *, MAX(salary) OVER(PARTITION BY company_id) AS max
FROM Salaries)

SELECT company_id, employee_id, employee_name, CASE WHEN max < 1000 THEN ROUND(salary,0) WHEN max BETWEEN 1000 AND 10000 THEN round(salary*0.76,0) ELSE round(salary * 0.51,0) END AS salary
FROM CTE
``` 
- Calculating salary after tax can be simply calculated by salary * (1-tax rate)

### Leetcode SQL (37/50)
[1398. Customers Who Bought Products A and B but Not C](https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/)
**SUB QUERY**

``` 
SELECT customer_id,customer_name
FROM Orders o
JOIN Customers c USING (customer_id)
WHERE customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'A')
AND customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'B')
AND customer_id NOT IN (SELECT customer_id FROM Orders WHERE product_name = 'C')
GROUP BY customer_id
``` 
- Filtering using IN/NOT IN, We need to specifically list with Sub queries

### Leetcode SQL (38/50)
[1715. Count Apples and Oranges](https://leetcode.com/problems/count-apples-and-oranges/)
**SUM**

``` 
SELECT SUM(CASE WHEN b.chest_id IS NULL THEN b.apple_count ELSE b.apple_count + c.apple_count END) AS apple_count, SUM(CASE WHEN b.chest_id IS NULL THEN b.orange_count ELSE b.orange_count + c.orange_count END) AS orange_count
FROM Boxes b
LEFT JOIN Chests c USING(chest_id) 

``` 
- When using SUM, try to sum it once not at all due to NULL values

### Leetcode SQL (39/50)
[2041. Accepted Candidates From the Interviews](https://leetcode.com/problems/accepted-candidates-from-the-interviews/)
**CTE**

``` 
WITH CTE AS(SELECT *, SUM(score) OVER(PARTITION BY interview_id) AS total
FROM Rounds
JOIN Candidates USING(interview_id)
)
x
SELECT DISTINCT candidate_id
FROM CTE
WHERE years_of_exp >= 2 AND total > 15
``` 
- CTE is faster than you expect (Maybe faster than sub-queries) but found out that it's exactly the same logically