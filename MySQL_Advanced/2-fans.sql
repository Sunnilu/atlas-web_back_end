-- Ranks country origns of bands --
-- Ordered by the number of (non-unique) fans --
-- Column names must be: origins and nb fan_fans --

-- Create index for partition optimization
CREATE INDEX idx_origin ON bands(origin);

WITH country_fans AS (
    SELECT 
        origin,
        COUNT(*) as nb_fans
    FROM bands
    GROUP BY origin
),
ranked_countries AS (
    SELECT 
        origin,
        nb_fans,
        DENSE_RANK() OVER (ORDER BY nb_fans DESC) as rank
    FROM country_fans
)
SELECT 
    rank,
    origin,
    nb_fans
FROM ranked_countries
ORDER BY nb_fans DESC;