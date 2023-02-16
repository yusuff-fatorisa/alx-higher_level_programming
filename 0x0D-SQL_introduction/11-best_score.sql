-- This script contains some SQL commands that lists all records
-- with a score >= 10 in the table 'second_table' of the hbtn_0c_0
-- database of your MySQL server.

SELECT score, name FROM seconds_table
WHERE score >= 10
ORDER BY score DESC;
