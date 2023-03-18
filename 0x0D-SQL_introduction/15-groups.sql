-- Displays the number of records with the same score in the table second_table
SELECT `score` COUNT( * ) AS `number`
ORDER BY `number` DESC
GROUP BY `score`;

