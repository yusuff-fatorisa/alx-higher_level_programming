-- This script contains some SQL commands that displays
-- the max temperature of each state, then ordered by
-- State name

SELECT state, MAX(value) AS max_temp FROM temperatures
GROUP BY state ORDER BY ASC
LIMIT 3
