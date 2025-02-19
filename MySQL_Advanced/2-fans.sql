-- Ranks country origns of bands --
-- Ordered by the number of (non-unique) fans --
-- Column names must be: origins and nb fan_fans --

-- Create index for partition optimization

SELECT 
        origin,
        SUM(fans) as nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;