-- Script shows the max temperature of each state (ordered by State name)
SELECT `state`, MAX(value) AS max_temp FROM tempratures
GROUP BY `state`
ORDER BY max_temp ASC;
