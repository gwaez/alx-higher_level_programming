-- This script lists all records of the table second_table, excluding rows without a name value, and listing the score and name (in this order), sorted by descending score.

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

