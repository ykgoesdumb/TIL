### Leetcode SQL (13/50)
[175. Combine Two Tables](https://leetcode.com/problems/combine-two-tables/)

**JOIN**

``` 
SELECT p.firstName, p.lastName, city, state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;

;

``` 
- NOTHING SPECIAL

</Br>

### Leetcode SQL (14/50)
[181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

**SELFJOIN**

``` 
SELECT e1.name AS Employee
FROM Employee e1
INNER JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary
;

``` 
- e1.salary 와 e2.salary가 따로 나오려면 INNER JOIN을 해야한다

</Br>

### Leetcode SQL (15/50)
[181. Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/)

**SELFJOIN**

``` 
SELECT e1.name AS Employee
FROM Employee e1
INNER JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary
;

``` 
- e1.salary 와 e2.salary가 따로 나오려면 INNER JOIN을 해야한다

</Br>