### Leetcode SQL (20/50)
[1398. Customers Who Bought Products A and B but Not C](https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/)

**WHERE**

``` 
#1st solution:

SELECT customer_id, customer_name
FROM Customers
WHERE customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'A')
AND customer_id IN (SELECT customer_id FROM Orders WHERE product_name = 'B')
AND customer_id NOT IN (SELECT customer_id FROM Orders WHERE product_name = 'C')
;


``` 
- Most easy solution but not efficient

**JOIN**
```
#2nd solution:
SELECT DISTINCT c.customer_id, c.customer_name
FROM Customers c
INNER JOIN Orders a ON a.customer_id = c.customer_id AND a.product_name = 'A'
INNER JOIN Orders b ON b.customer_id = c.customer_id AND b.product_name = 'B'
LEFT JOIN Orders o ON o.customer_id = c.customer_id AND o.product_name = 'C'
WHERE o.product_name IS NULL
;
```
- A little faster. Fun approach using join

### Leetcode SQL (21/50)
[602. Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/)

**UNION ALL**

``` 
SELECT DISTINCT friend AS id, COUNT(friend) OVER (PARTITION BY friend) AS num
FROM 
(SELECT requester_id as friend
FROM RequestAccepted

UNION ALL

SELECT accepter_id as friend
FROM RequestAccepted) AS f
ORDER BY num DESC
LIMIT 1;
``` 
- FASTER THAN 90% 

### Leetcode SQL (22/50)
[1285. Find the Start and End Number of Continuous Ranges](https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/description/)

**CTE & ROW NUM**

``` 
WITH CTE AS(
SELECT log_id, ROW_NUMBER() OVER() AS rn, log_id - ROW_NUMBER()OVER() AS part
FROM LOgs)

SELECT MIN(log_id) as start_id, MAX(log_id) AS end_id
FROM CTE
GROUP BY part
ORDER BY start_id
;
``` 
- Smart solution but slow. Try to find better solution if possible
- **Solve it once again **

### Leetcode SQL (23/50)
[1747. Leetflex Banned Accounts](https://leetcode.com/problems/leetflex-banned-accounts/)

**JOIN AND BETWEEN**

``` 
SELECT DISTINCT b.account_id
FROM LogInfo a
JOIN LogInfo b ON a.account_id = b.account_id AND a.ip_address != b.ip_address
WHERE b.login BETWEEN a.login AND a.logout
``` 
- SELF JOIN & Between
- Nothing special

### Leetcode SQL (24/50)
[550. Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv/)

**SUBQUERY**

``` 
    SELECT ROUND(COUNT(DISTINCT PLAYER_ID) / 
        (SELECT COUNT(DISTINCT PLAYER_ID) FROM ACTIVITY) 
    , 2) AS a
    FROM ACTIVITY 
    GROUP BY PLAYER_ID
    HAVING ABS(MIN(EVENT_DATE) - MAX(EVENT_DATE)) = 1
``` 
- ABS to solve all cases**

### Leetcode SQL (25/50)
[2159. Order Two Columns Independently](https://leetcode.com/problems/order-two-columns-independently/))

**ROW_NUMBER + joine**

``` 
SELECT first_col, second_col
FROM (
    SELECT first_col, ROW_NUMBER() OVER(ORDER BY first_col ASC) AS fr
    FROM Data
) a
JOIN (
    SELECT second_col, ROW_NUMBER() OVER(ORDER BY second_col DESC) AS sr
    FROM Data
) b
ON a.fr = b.sr
``` 
- row_num to play with

### Leetcode SQL (26/50)
[1445. 1445. Apples & Oranges](https://leetcode.com/problems/apples-oranges/description/)

**CTE**

``` 
WITH CTE
AS(SELECT sale_date, CASE WHEN fruit = 'apples' THEN sold_num ELSE -1 * sold_num END as ele
FROM Sales)

SELECT sale_date, SUM(ele) AS diff FROM CTE
GROUP BY sale_date 
```

**CASE**
``` 
SELECT sale_date, SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE -1 * sold_num END)
AS Diff
FROM Sales
GROUP BY sale_date
ORDER BY sale_date;
```

**IF**
SELECT
    sale_date, 
    SUM(
        IF(fruit = 'apples', sold_num, -sold_num)
        ) as diff
FROM Sales
GROUP BY sale_date
ORDER BY sale_date

- Tried to solve this with Join, How is the join clause operate?
- GROUP BY only spits out the first row

### Leetcode SQL (27/50)
[2084. Drop Type 1 Orders for Customers With Type 0 Orders](https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/description/)

**WHERE**
``` 
SELECT *
FROM Orders
WHERE order_type = 0 OR customer_id NOT IN (SELECT customer_id FROM Orders WHERE order_type = 0);
``` 
**CTE**
```
WITH cte AS(SELECT *, MIN(order_type) OVER(PARTITION BY customer_id) AS min
FROM Orders)

SELECT order_id, customer_id, order_type
FROM cte
WHERE min = order_type
ORDER BY order_type DESC
```
- NOT IN filters all the id which included some type 0
- MIN() OVER(PARTITION BY) will identify if partition has the lowest value which is 0



### Leetcode SQL (28/50)
[1393. Capital Gain/Loss](https://leetcode.com/problems/capital-gainloss/)

**CTE, IF**

``` 
WITH CTE as(
SELECT *, IF(operation = 'Buy', -price, price) AS cal
FROM Stocks)

SELECT stock_name, sum(cal) AS capital_gain_loss
FROM CTE
GROUP BY stock_name
```

**IF**
```
SELECT stock_name, sum(IF(operation='Sell', price,-price)) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name
```
- Using CTE was faster solution

### Leetcode SQL (29/50)
[1783. Grand Slam Titles](https://leetcode.com/problems/grand-slam-titles/description/)

**INNER JOIN OR**

``` 
SELECT p.player_id, p.player_name, SUM(p.player_id = c.Wimbledon) + SUM(p.player_id = c.Fr_open) + SUM(p.player_id = c.US_open) + SUM(p.player_id = c.Au_open) AS grand_slams_count
FROM Players p
INNER JOIN Championships c ON p.player_id = Wimbledon or p.player_id = Fr_open or p.player_id = US_open or p.player_id = Au_open
GROUP BY p.player_id
``` 
- IF using 'OR' clause when INNER JOIN, INNER JOIN builds up for all elements are satisfied
- WITHOUT GROUP BY, SUM will SUM ALL values in the column
