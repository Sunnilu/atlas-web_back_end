-- Ranks country origns of bands --
-- Ordered by the number of (non-unique) fans --
-- Column names must be: origins and nb fan_fans --

-- Create index for partition optimization

CREATE PROCEDURE RankCountriesByFans()
BEGIN
    SELECT 
        origin,
        nb_fans,
        DENSE_RANK() OVER (ORDER BY nb_fans DESC) as rank
    FROM metal_bands
    ORDER BY nb_fans DESC;
END //

;