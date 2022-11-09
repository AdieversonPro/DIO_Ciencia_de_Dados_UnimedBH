SELECT region
	,sum(population)
FROM "populationdb"."population"
GROUP BY region;