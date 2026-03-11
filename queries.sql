--Most valuable unread comics, only showing ones worth more than $20
SELECT title, issue_number, estimated_value_usd AS value, condition
FROM comics
WHERE read_status = 'Unread'
AND estimated_value_usd > 20
ORDER BY estimated_value_usd DESC;

--Publishers founded before 1988 and the sum of those comics in the collection
SELECT publishers.name AS publisher, publishers.founded_year, 
       COUNT(comics.comic_id) AS total_issues,
       SUM(comics.estimated_value_usd) AS total_value
FROM publishers
JOIN comics ON publishers.publisher_id = comics.publisher_id
WHERE publishers.founded_year < 1988
GROUP BY publishers.name, publishers.founded_year
ORDER BY total_value DESC;

--Comics with mid-range value and not in poor condition
SELECT DISTINCT title, issue_number, condition, estimated_value_usd AS value
FROM comics
WHERE estimated_value_usd BETWEEN 20 AND 100
AND condition != 'Poor'
ORDER BY value DESC;