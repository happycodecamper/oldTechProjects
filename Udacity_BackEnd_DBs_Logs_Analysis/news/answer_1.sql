CREATE view Question_1 AS
SELECT articles.title AS "Most Popular Articles", count(*) AS "Views"
FROM log JOIN articles
ON '/article/' || articles.slug = log.path
GROUP BY articles.title
ORDER BY count(*) DESC LIMIT 3;