-- Script shows the max temperature of each state (ordered by State name)
SELECT `state`, MAX(value) AS max_temp FROM tempratures
ORDER BY `state` ASC;
