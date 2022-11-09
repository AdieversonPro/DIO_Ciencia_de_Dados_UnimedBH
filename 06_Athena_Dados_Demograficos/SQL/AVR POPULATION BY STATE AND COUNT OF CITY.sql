SELECT STATE
	,count(DISTINCT city) AS qtd_municipios
	,sum(population) AS populacao
	,round(avg(population), 2) AS media_populacao
FROM "populationdb"."population"
GROUP BY 1
ORDER BY 2 DESC
	,3 DESC
	,4;