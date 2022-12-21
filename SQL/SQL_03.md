{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fmodern\fcharset0 Courier-Bold;\f2\fnil\fcharset129 AppleSDGothicNeo-Regular;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red114\green186\blue255;
\red203\green203\blue202;\red194\green125\blue100;\red141\green213\blue254;\red71\green138\blue206;}
{\*\expandedcolortbl;;\cssrgb\c0\c1\c1;\cssrgb\c100000\c100000\c99985\c0;\cssrgb\c51431\c78175\c100000;
\cssrgb\c83320\c83320\c83112;\cssrgb\c80772\c56796\c46790;\cssrgb\c61545\c86704\c99884;\cssrgb\c34146\c61677\c84338;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 ## SQL 03\cf2 \cb3 \strokec5 \
\
\cf2 \cb3 \strokec4 ### HackerRank SQL - Medium (3/16)\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cf2 \cb3 \strokec5 HackerRank - Binary Tree Nodes\cf2 \cb3 \strokec6 ](hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true)\cf2 \cb3 \strokec5 \
\
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **CASE**
\f0\b0 \cf2 \cb3 \strokec5  \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ``` \cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 SELECT N, \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7     CASE \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7         WHEN P IS NULL \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7         THEN 'Root' \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7         WHEN N NOT IN (SELECT P FROM BST WHERE P IS NOT NULL)\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7         THEN 'Leaf'\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7         ELSE 'Inner' \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7     END\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 FROM BST\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 ORDER BY N;\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - 
\f2 \cf2 \cb3 \strokec5 \'c1\'fd\'c7\'d5\'bf\'a1\'bc\'ad
\f0 \cf2 \cb3 \strokec5  IN 
\f2 \cf2 \cb3 \strokec5 \'c0\'b8\'b7\'ce
\f0 \cf2 \cb3 \strokec5  value 
\f2 \cf2 \cb3 \strokec5 \'c3\'a3\'c0\'bb
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b6\'a7\'b4\'c2
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b4\'d9\'bd\'c3
\f0 \cf2 \cb3 \strokec5  SELECT
\f2 \cf2 \cb3 \strokec5 \'b7\'ce
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c1\'fd\'c7\'d5\'c0\'bb
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b8\'ed\'bd\'c3\'c7\'d8
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c1\'d9
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b0\'cd
\f0 \cf2 \cb3 \strokec5  \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec8 <br\cf2 \cb3 \strokec5  \cf2 \cb3 \strokec8 />\cf2 \cb3 \strokec5 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 ### HackerRank SQL - Medium (4/16)\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cf2 \cb3 \strokec5 HackerRank - Occupations\cf2 \cb3 \strokec6 ](https://www.hackerrank.com/challenges/occupations/problem)\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **WINDOW FUNCTION, CTE, GROUP BY**
\f0\b0 \cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 WITH temp AS (\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 SELECT *, ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS 'rn'\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 FROM OCCUPATIONS)\cf2 \cb3 \strokec5 \
\
\cf2 \cb3 \strokec7 SELECT \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 MAX(CASE WHEN Occupation = 'Doctor' THEN temp.Name END) AS 'Doctor',\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 MAX(CASE WHEN Occupation = 'Professor' THEN temp.Name END) AS 'Professor',\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 MAX(CASE WHEN Occupation = 'Singer' THEN temp.Name END) AS 'Singer',\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 MAX(CASE WHEN Occupation = 'Actor' THEN temp.Name END) AS 'Actor'\cf2 \cb3 \strokec5 \
\
\cf2 \cb3 \strokec7 FROM temp\cf2 \cb3 \strokec5 \
\
\cf2 \cb3 \strokec7 GROUP BY rn;\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cf2 \cb3 \strokec5 Aggregate function
\f2 \cf2 \cb3 \strokec5 \'c0\'bb
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c8\'b0\'bf\'eb\'c7\'d8\'be\'df
\f0 \cf2 \cb3 \strokec5  Group by 
\f2 \cf2 \cb3 \strokec5 \'b0\'a1
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b0\'a1\'b4\'c9\'c7\'cf\'b4\'d9
\f0 \cf2 \cb3 \strokec5 .\
\cf2 \cb3 \strokec4 - \cf2 \cb3 \strokec5 Aggregate function
\f2 \cf2 \cb3 \strokec5 \'c0\'bb
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c8\'b0\'bf\'eb\'c7\'d8\'be\'df
\f0 \cf2 \cb3 \strokec5  Value 
\f2 \cf2 \cb3 \strokec5 \'b0\'a1
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'be\'f8\'b4\'c2
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b0\'f7\'bf\'a1
\f0 \cf2 \cb3 \strokec5  NULL
\f2 \cf2 \cb3 \strokec5 \'b7\'ce
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c3\'a4\'bf\'f6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b3\'f5\'c0\'bb
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'bc\'f6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c0\'d6\'b4\'d9
\f0 \cf2 \cb3 \strokec5 .\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec8 </Br>\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 ## HackerRank SQL - Medium (5/16)\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cf2 \cb3 \strokec5 HackerRank - New Companies\cf2 \cb3 \strokec6 ](https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true)\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **GROUP BY, COUNT DISTINCT**
\f0\b0 \cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 SELECT Company_code, Founder, COUNT(DISTINCT lead_manager_code), COUNT(DISTINCT senior_manager_code), COUNT(DISTINCT manager_code), COUNT(DISTINCT employee_code)\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 FROM Employee\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 LEFT JOIN Company USING(company_code)\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 GROUP BY company_code, founder\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 ORDER BY Company_code;\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cf2 \cb3 \strokec5 Group By 
\f2 \cf2 \cb3 \strokec5 \'b8\'a6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'be\'ee\'b6\'bb\'b0\'d4
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c7\'d8\'be\'df
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c7\'cf\'b3\'aa\'b0\'a1
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c6\'f7\'c0\'ce\'c6\'ae
\f0 \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec4 - 
\f2 \cf2 \cb3 \strokec5 \'b9\'ae\'c1\'a6\'b8\'a6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c3\'b5\'c3\'b5\'c8\'f7
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c0\'df
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c0\'d0\'b0\'ed
\f0 \cf2 \cb3 \strokec5  Distinct
\f2 \cf2 \cb3 \strokec5 \'b8\'a6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c0\'d8\'c1\'f6\'b8\'bb\'c0\'da
\f0 \cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec8 </Br>\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 ## HackerRank SQL - Medium (6/16)\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cf2 \cb3 \strokec5 HackerRank - Weather Observation Station 18\cf2 \cb3 \strokec6 ](https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true)\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **ROUND, ABS**
\f0\b0 \cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 SELECT  ROUND(ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)),4)\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 FROM STATION;\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cf2 \cb3 \strokec5 ROUND 
\f2 \cf2 \cb3 \strokec5 \'c7\'d4\'bc\'f6\'bf\'cd
\f0 \cf2 \cb3 \strokec5  ABS 
\f2 \cf2 \cb3 \strokec5 \'c7\'d4\'bc\'f6\'b8\'a6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'bb\'e7\'bf\'eb\'c7\'d8
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'ba\'bb\'b4\'d9
\f0 \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec4 - 
\f2 \cf2 \cb3 \strokec5 \'c6\'af\'ba\'b0\'c7\'d1
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b0\'cd
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'be\'f8\'b4\'c2
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b9\'ae\'c1\'a6
\f0 \cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec8 </Br>\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 ## HackerRank SQL - Medium (7/16)\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cf2 \cb3 \strokec5 HackerRank - Weather Observation Station 19\cf2 \cb3 \strokec6 ](https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true)\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **SQRT, POWER**
\f0\b0 \cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 SELECT ROUND(\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7     SQRT(POWER((MAX(LAT_N) - MIN(LAT_N)),2) + POWER((MAX(LONG_W) - MIN(LONG_W)),2))\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7          ,4)\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 FROM STATION\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cf2 \cb3 \strokec5 SQRT 
\f2 \cf2 \cb3 \strokec5 \'c7\'d4\'bc\'f6\'bf\'cd
\f0 \cf2 \cb3 \strokec5  POWER 
\f2 \cf2 \cb3 \strokec5 \'c7\'d4\'bc\'f6\'b8\'a6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'bb\'e7\'bf\'eb\'c7\'d8
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'ba\'bb\'b4\'d9
\f0 \cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec4 - 
\f2 \cf2 \cb3 \strokec5 \'c6\'af\'ba\'b0\'c7\'d1
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b0\'cd
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'be\'f8\'b4\'c2
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b9\'ae\'c1\'a6
\f0 \cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec8 </Br>\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 ## HackerRank SQL - Medium (8/16)\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0

\f1\b \cf2 \cb3 \strokec5 **WINDOW FUNCTION, OVER, Median**
\f0\b0 \cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 [\cf2 \cb3 \strokec5 HackerRank - Weather Observation Station 20\cf2 \cb3 \strokec6 ](https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true)\cf2 \cb3 \strokec5 \
\
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec7 WITH t AS(SELECT *, ROW_NUMBER() OVER(ORDER BY LAT_N) AS rn, COUNT(LAT_N)over() AS rc\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 FROM STATION)\cf2 \cb3 \strokec5 \
\
\cf2 \cb3 \strokec7 SELECT ROUND(t.LAT_N,4)\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 FROM t\cf2 \cb3 \strokec5 \
\cf2 \cb3 \strokec7 WHERE rn IN (rc/2,(rc+1)/2)\cf2 \cb3 \strokec5 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec6 ```\cf2 \cb3 \strokec5 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec4 - \cf2 \cb3 \strokec5 Mysql 
\f2 \cf2 \cb3 \strokec5 \'bf\'a1\'b4\'c2
\f0 \cf2 \cb3 \strokec5  median funciton
\f2 \cf2 \cb3 \strokec5 \'c0\'cc
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'be\'f8\'c0\'b8\'b9\'c7\'b7\'ce
\f0 \cf2 \cb3 \strokec5  count
\f2 \cf2 \cb3 \strokec5 \'b0\'a1
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c8\'a6\'bc\'f6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c2\'a6\'bc\'f6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c0\'cf
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b6\'a7\'b8\'a6
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b0\'ed\'b7\'c1\'c7\'cf\'bf\'a9
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c7\'ca\'c5\'cd\'b8\'b5
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c7\'d8\'c1\'d6\'be\'ee\'be\'df
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c7\'d1\'b4\'d9
\f0 \cf2 \cb3 \strokec5 .\
\cf2 \cb3 \strokec4 - \cf2 \cb3 \strokec5 SELECT 
\f2 \cf2 \cb3 \strokec5 \'b9\'ae\'bf\'a1\'bc\'ad
\f0 \cf2 \cb3 \strokec5  aggregate function
\f2 \cf2 \cb3 \strokec5 \'c0\'ba
\f0 \cf2 \cb3 \strokec5  OVER 
\f2 \cf2 \cb3 \strokec5 \'c0\'fd\'c0\'bb
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c8\'b0\'bf\'eb
\f0 \cf2 \cb3 \strokec5  (Count
\f2 \cf2 \cb3 \strokec5 \'b4\'c2
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'b4\'dc\'c0\'cf\'c7\'d4\'bc\'f6\'c1\'f6\'b8\'b8
\f0 \cf2 \cb3 \strokec5  Window function
\f2 \cf2 \cb3 \strokec5 \'b0\'fa
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c7\'d4\'b2\'b2
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'bb\'e7\'bf\'eb\'c7\'d4\'c0\'b8\'b7\'ce
\f0 \cf2 \cb3 \strokec5  OVER 
\f2 \cf2 \cb3 \strokec5 \'c0\'fd\'c0\'bb
\f0 \cf2 \cb3 \strokec5  
\f2 \cf2 \cb3 \strokec5 \'c8\'b0\'bf\'eb
\f0 \cf2 \cb3 \strokec5 )\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec8 </Br>\cf2 \cb3 \strokec5 \
\
}