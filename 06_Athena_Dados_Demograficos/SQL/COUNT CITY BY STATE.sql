SELECT STATE
	,count(city)
FROM "populationdb"."population"
GROUP BY 1
ORDER BY 2 DESC;