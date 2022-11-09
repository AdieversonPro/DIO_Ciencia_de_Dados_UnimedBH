SELECT p.STATE
	,sum(p.population) AS populacao
	,CAST(sum(p.population) * 100 AS DECIMAL) / CAST(s.pp AS DECIMAL) AS result
FROM "populationdb"."population" AS p
	,(
		SELECT sum(population) AS pp
		FROM "populationdb"."population"
		) AS s
GROUP BY 1
	,s.pp;