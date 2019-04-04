CREATE view Question_2 AS
SELECT  authors.name AS "Articles Authors Name", count(*) AS "Views"
FROM log JOIN articles
ON '/article/' || articles.slug = log.path
JOIN authors
ON authors.id = articles.author
GROUP BY authors.name
ORDER BY count(*) DESC;