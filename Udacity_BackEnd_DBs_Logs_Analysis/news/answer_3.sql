CREATE view Question_3 AS
SELECT to_char(A.time, 'FMMonth DD, YYYY') AS "DATE",
round((A.count/(CAST(A.count AS DECIMAL) + CAST(B.count AS DECIMAL))*100), 1) AS "Errors"
FROM
(SELECT A.time::DATE, count(*)
FROM log AS A
WHERE A.status != '200 OK' 
GROUP BY A.time::DATE
ORDER BY count(*) DESC) AS A
join
(SELECT B.time::DATE, count(*)
FROM log AS B
WHERE B.status = '200 OK' 
GROUP BY B.time::DATE
ORDER BY count(*) DESC) AS B
ON A.time = B.time
WHERE round((A.count/(CAST(A.count AS DECIMAL) + CAST(B.count AS DECIMAL))*100), 1) > 1
ORDER BY A.count DESC;