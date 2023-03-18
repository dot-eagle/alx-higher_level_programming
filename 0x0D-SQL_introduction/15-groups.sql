-- Displays the number of records with the same score in the table second_table
SELECT `score` UNIQUE COUNT AS `number`
ORDER BY `score` DESC
GROUP BY `score`;

