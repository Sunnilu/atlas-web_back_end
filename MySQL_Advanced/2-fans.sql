-- Ranks country origns of bands --
-- Ordered by the number of (non-unique) fans --
-- Column names must be: origins and nb fan_fans --

SELECT origins, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;