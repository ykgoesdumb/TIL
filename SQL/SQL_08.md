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
[xxx. Question name](URL)

**Key Learnings Here**

``` 
# Your code 
``` 
- Notes

### Leetcode SQL (24/50)
[xxx. Question name](URL)

**Key Learnings Here**

``` 
# Your code 
``` 
- Notes

### Leetcode SQL (25/50)
[xxx. Question name](URL)

**Key Learnings Here**

``` 
# Your code 
``` 
- Notes

### Leetcode SQL (26/50)
[xxx. Question name](URL)

**Key Learnings Here**

``` 
# Your code 
``` 
- Notes

### Leetcode SQL (27/50)
[xxx. Question name](URL)

**Key Learnings Here**

``` 
# Your code 
``` 
- Notes

### Leetcode SQL (28/50)
[xxx. Question name](URL)

**Key Learnings Here**

``` 
# Your code 
``` 
- Notes

### Leetcode SQL (29/50)
[xxx. Question name](URL)

**Key Learnings Here**

``` 
# Your code 
``` 
- Notes
