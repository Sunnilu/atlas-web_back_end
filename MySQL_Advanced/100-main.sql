-- show the compute average weighted score
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

CALL compute_average_weighted_score();

SELECT "----";
SELECT * FROM users;