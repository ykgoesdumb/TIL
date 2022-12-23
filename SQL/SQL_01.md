
## SQL 01 

### Leetcode SQL (1/50)
[196. Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/)

**SELF JOIN, DELETE**

``` 
DELETE p1
FROM Person p1, Perosn p2
WHERE p1.email = p2.email AND p1.id > p2.id;

```
- Delete 함수 활용법 Check
- Self-Join filtering

</Br>

### Leetcode SQL (2/50)
[1484. Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/)

**GROUP CONCAT**

```
SELECT sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product ORDER BY product ASC separator ',') AS products
FROM ACTIVITIES
GROUP BY sell_date
ORDER BY sell_date;
```

- GROUP_CONCAT 은 separator 'xxx' 가 필요하다
- Alias 사용법 (따옴표 등) 확인하기

</Br>

### Leetcode SQL (3/50)
[1965. Employees With Missing Information](https://leetcode.com/problems/employees-with-missing-information/)

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
- Mysql 에서는 FULL JOIN 기능을 제공하지 않기 때문에 LEFT & RIGHT JOIN을 UNION 함수로 묶어준다.
- 항상 Alias에 유의

</Br>

### Leetcode SQL (4/50)
[1795. Rearrange Products Table](https://leetcode.com/problems/rearrange-products-table/) 


**Rearranging the table**
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
- SELECT 'XXX' AS Column_name 을 활용하여 칼럼 아래 'XXX' value 를 추가

</Br>

### Leetcode SQL (5/50)
[608. Tree Node](https://leetcode.com/problems/tree-node/) 

``` 
SELECT id,
CASE WHEN P_id IS NULL THEN 'Root'  
    WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'  
    ELSE 'Leaf'
END AS type
FROM Tree
ORDER BY id;
``` 