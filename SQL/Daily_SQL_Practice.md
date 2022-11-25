
## Daily SQL Practice 

### 196. Delete Duplicate Emails

2022-11-20:
``` 
Input: 
Person table:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Output: 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Explanation: john@example.com is repeated two times. We keep the row with the smallest Id = 1.
``` 

**Utilizing self-join** 
``` 
DELETE p1
FROM Person p1, Perosn p2
WHERE p1.email = p2.email AND p1.id > p2.id;

```



## 1484. Group Sold Products By The Date

2022-11-21:
``` 
Input: 
Activities table:
+------------+------------+
| sell_date  | product     |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Basketball |
| 2020-06-01 | Bible      |
| 2020-06-02 | Mask       |
| 2020-05-30 | T-Shirt    |
+------------+------------+
Output: 
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
Explanation: 
For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
For 2020-06-02, the Sold item is (Mask), we just return it.
``` 

** GROUP CONCAT?!**
```
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product ORDER BY product ASC separator ',') AS products
FROM ACTIVITIES
GROUP BY sell_date
ORDER BY sell_date;
```

Remember GROUP_CONCAT needs a separator 'xxx'
Read about alias


### 1965. Employees With Missing Information

2022-11-22:
``` 
Input: 
Employees table:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Crew     |
| 4           | Haven    |
| 5           | Kristian |
+-------------+----------+
Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 5           | 76071  |
| 1           | 22517  |
| 4           | 63539  |
+-------------+--------+
Output: 
+-------------+
| employee_id |
+-------------+
| 1           |
| 2           |
+-------------+
Explanation: 
Employees 1, 2, 4, and 5 are working at this company.
The name of employee 1 is missing.
The salary of employee 2 is missing.
``` 

**FULL JOIN in MySQL**

``` 
SELECT employee_id
FROM(

SELECT e.employee_id, e.name, s.salary
FROM Employees e
LEFT JOIN Salaries s ON e.employee_id = s.employee_id

UNION

SELECT s.employee_id, e.name, s.salary
FROM Employees e
RIGHT JOIN Salaries s ON e.employee_id = s.employee_id
) AS t
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id
;


``` 
Mysql does not have FULL JOIN function so we need to perform FULL JOIN by repeating LEFT & RIGHT JOIN
with UNION function. Remember to put alias when making a joint table for FROM.


### 1965. Employees With Missing Information

2022-11-23:
1795. Rearrange Products Table

``` 
Input: 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output: 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
Explanation: 
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.
``` 
** Rearranging the table**
``` 
SELECT product_id, 'store1' AS store, store1 AS price
FROM products 
WHERE store1 IS NOT NULL

UNION

SELECT product_id, 'store2' AS store, store2 AS price
FROM products 
WHERE store2 IS NOT NULL

UNION

SELECT product_id, 'store3' AS store, store3 AS price
FROM products 
WHERE store3 IS NOT NULL;
``` 
SQL TIP
SELECT 'XXX' AS Column_name will put 'XXX' under Column_name

### 1965. Employees With Missing Information

2022-11-24:
608. Tree Node
``` 
SELECT id,
CASE WHEN P_id IS NULL THEN 'Root'  
    WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'  
    ELSE 'Leaf'
END AS type
FROM Tree
ORDER BY id;
``` 
Must carefully write sub query without syntax error.



