{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;\f2\fnil\fcharset129 AppleSDGothicNeo-Regular;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red114\green186\blue255;
\red203\green203\blue202;\red194\green125\blue100;\red141\green213\blue254;\red71\green138\blue206;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c99985\c0;\cssrgb\c51431\c78175\c100000;
\cssrgb\c83320\c83320\c83112;\cssrgb\c80772\c56796\c46790;\cssrgb\c61545\c86704\c99884;\cssrgb\c34146\c61677\c84338;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 ## SQL 02\cb3 \strokec5 \
\
\cb3 \strokec4 ### HackerRank SQL - Medium (1/16)\cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cb3 \strokec5 HackerRank - The PADS\cb3 \strokec6 ](https://www.hackerrank.com/challenges/the-pads/problem?isFullScreen=true)\cb3 \strokec5 \
\
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **CONCAT, GROUP BY, ORDER BY, LEFT**
\f0\b0 \cb3 \strokec5  \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ``` \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 SELECT CONCAT(name, '(', LEFT(occupation,1), ')')\cb3 \strokec5 \
\cb3 \strokec7 FROM OCCUPATIONS\cb3 \strokec5 \
\cb3 \strokec7 ORDER BY name;\cb3 \strokec5 \
\
\cb3 \strokec7 SELECT CONCAT('There are a total of ',COUNT(occupation),' ',LOWER(occupation),'s.')\cb3 \strokec5 \
\cb3 \strokec7 FROM OCCUPATIONS\cb3 \strokec5 \
\cb3 \strokec7 GROUP BY occupation\cb3 \strokec5 \
\cb3 \strokec7 ORDER BY COUNT(occupation), occupation;\cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cb3 \strokec5 CONCAT 
\f2 \cb3 \strokec5 \'c0\'bb
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'bb\'e7\'bf\'eb
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c7\'d2
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b6\'a7\'b4\'c2
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c7\'d7\'bb\'f3
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b6\'e7\'be\'ee\'be\'b2\'b1\'e2\'b8\'a6
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c1\'d6\'c0\'c7
\f0 \cb3 \strokec5 \
\cb3 \strokec4 - 
\f2 \cb3 \strokec5 \'c6\'af\'ba\'b0\'c7\'d1
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b0\'cd
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'be\'f8\'b4\'c2
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b9\'ae\'c1\'a6
\f0 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec8 <br\cb3 \strokec5  \cb3 \strokec8 />\cb3 \strokec5 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 ### HackerRank SQL - Medium (2/16)\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cb3 \strokec5 HackerRank - Placements\cb3 \strokec6 ](https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true)\cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **CTE, Multiple Joins**
\f0\b0 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 WITH Friend_Salary AS (SELECT f.ID, f.Friend_ID, p.Salary \cb3 \strokec5 \
\cb3 \strokec7 FROM Friends f\cb3 \strokec5 \
\cb3 \strokec7 JOIN Packages p ON f.Friend_ID = p.ID\cb3 \strokec5 \
\cb3 \strokec7 ORDER BY f.ID)\cb3 \strokec5 \
\
\cb3 \strokec7 SELECT s.Name\cb3 \strokec5 \
\cb3 \strokec7 FROM Students s\cb3 \strokec5 \
\cb3 \strokec7 LEFT JOIN Friends f ON s.ID = f.ID\cb3 \strokec5 \
\cb3 \strokec7 LEFT JOIN Packages p ON s.ID = p.ID\cb3 \strokec5 \
\cb3 \strokec7 LEFT JOIN Friend_Salary fs ON s.ID = fs.ID\cb3 \strokec5 \
\cb3 \strokec7 WHERE p.Salary < fs.Salary\cb3 \strokec5 \
\cb3 \strokec7 ORDER BY fs.Salary;\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cb3 \strokec5 CTE 
\f2 \cb3 \strokec5 \'b8\'a6
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c8\'b0\'bf\'eb\'c7\'d8\'bc\'ad
\f0 \cb3 \strokec5  Friend_ID 
\f2 \cb3 \strokec5 \'bf\'cd
\f0 \cb3 \strokec5  ID
\f2 \cb3 \strokec5 \'b8\'a6
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b8\'c2\'c3\'df\'b4\'c2
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b0\'cd\'c0\'cc
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c6\'f7\'c0\'ce\'c6\'ae
\f0 \cb3 \strokec5 \
\cb3 \strokec4 - 
\f2 \cb3 \strokec5 \'bf\'ac\'bc\'d3\'c7\'d8\'bc\'ad
\f0 \cb3 \strokec5  Join
\f2 \cb3 \strokec5 \'c0\'bb
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c8\'b0\'bf\'eb
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c7\'d2
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'bc\'f6
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c0\'d6\'b4\'d9
\f0 \cb3 \strokec5 \
\
\
\cb3 \strokec4 ### Leetcode - (6/50)\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cb3 \strokec5 180. Consecutive Numbers\cb3 \strokec6 ](https://leetcode.com/problems/consecutive-numbers/)\cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **SELF JOIN**
\f0\b0 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 SELECT DISTINCT a.num\cb3 \strokec5 \
\cb3 \strokec7 FROM Logs a\cb3 \strokec5 \
\cb3 \strokec7 JOIN Logs b ON a.id = b.id + 1 AND a.num = b.num\cb3 \strokec5 \
\cb3 \strokec7 JOIN Logs c ON a.id = c.id + 2 AND a.num = c.num\cb3 \strokec5 \
\cb3 \strokec7 ;\cb3 \strokec5 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - 
\f2 \cb3 \strokec5 \'b0\'b0\'c0\'ba
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c4\'c3\'b7\'b3
\f0 \cb3 \strokec5 , 
\f2 \cb3 \strokec5 \'c6\'af\'c8\'f7
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b0\'a1\'b1\'ee\'bf\'ee
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c4\'ae\'b7\'b3\'b3\'a2\'b8\'ae\'c0\'c7
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b0\'aa
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'ba\'f1\'b1\'b3\'b4\'c2
\f0 \cb3 \strokec5  SELF JOIN
\f2 \cb3 \strokec5 \'c0\'b8\'b7\'ce
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b8\'b9\'c0\'cc
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c7\'ae\'be\'ee\'b3\'bd\'b4\'d9
\f0 \cb3 \strokec5 .\
\cb3 \strokec4 - 
\f2 \cb3 \strokec5 \'c7\'d1
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c4\'ad\'be\'bf
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b4\'f5\'c7\'d1
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b0\'aa\'c0\'bb
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'ba\'f1\'b1\'b3\'c7\'d8\'c1\'d6\'b1\'e2
\f0 \cb3 \strokec5 \
\
\cb3 \strokec4 ### Leetcode - (7/50)\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cb3 \strokec5 184. Department Highest Salary\cb3 \strokec6 ](https://leetcode.com/problems/department-highest-salary/)\cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **Rank, IN, Alias**
\f0\b0 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 # 
\f2 \cb3 \strokec7 \'c7\'ae\'c0\'cc
\f0 \cb3 \strokec7  1\cb3 \strokec5 \
\cb3 \strokec7 SELECT d.name AS Department, e.name AS Employee, e.salary as Salary\cb3 \strokec5 \
\cb3 \strokec7 FROM Employee e\cb3 \strokec5 \
\cb3 \strokec7 INNER JOIN Department d ON e.departmentId = d.id\cb3 \strokec5 \
\cb3 \strokec7 WHERE (e.departmentId,e.salary) IN (SELECT departmentId, MAX(salary)\cb3 \strokec5 \
\cb3 \strokec7 FROM Employee\cb3 \strokec5 \
\cb3 \strokec7 GROUP BY departmentID);\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cb3 \strokec5 Filtering 
\f2 \cb3 \strokec5 \'c7\'d2
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b6\'a7
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'bc\'ad\'ba\'ea\'c4\'f5\'b8\'ae\'b0\'a1
\f0 \cb3 \strokec5  2
\f2 \cb3 \strokec5 \'b0\'b3
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c0\'cc\'bb\'f3\'c0\'cf
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b0\'e6\'bf\'ec
\f0 \cb3 \strokec5  WHERE, IN clause 
\f2 \cb3 \strokec5 \'bf\'a1
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b5\'ce\'b0\'b3\'c0\'c7
\f0 \cb3 \strokec5  attribute
\f2 \cb3 \strokec5 \'b8\'a6
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c6\'f7\'c7\'d4
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'bd\'c3\'c4\'d1\'be\'df
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c7\'d4
\f0 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 # 
\f2 \cb3 \strokec7 \'c7\'ae\'c0\'cc
\f0 \cb3 \strokec7  2\cb3 \strokec5 \
\cb3 \strokec7 SELECT t.Department, t.Employee, t.Salary\cb3 \strokec5 \
\cb3 \strokec7 FROM\cb3 \strokec5 \
\cb3 \strokec7 (SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary, rank() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS 'Rank'\cb3 \strokec5 \
\cb3 \strokec7 FROM Employee e\cb3 \strokec5 \
\cb3 \strokec7 INNER JOIN Department d ON e.departmentId = d.id) AS t\cb3 \strokec5 \
\cb3 \strokec7 WHERE t.Rank = 1;\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cb3 \strokec5 Alias 
\f2 \cb3 \strokec5 \'bb\'e7\'bf\'eb\'b9\'fd
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c8\'ae\'bd\'c7\'c8\'f7
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'be\'cb\'be\'c6\'b5\'ce\'b1\'e2
\f0 \cb3 \strokec5 \
\cb3 \strokec4 - \cb3 \strokec5 Alias 
\f2 \cb3 \strokec5 \'bb\'e7\'bf\'eb
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'c7\'d2
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b6\'a7
\f0 \cb3 \strokec5  
\f2 \cb3 \strokec5 \'b5\'fb\'bf\'c8\'c7\'a5
\f0 \cb3 \strokec5 \
}