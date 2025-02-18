-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT 
    band_name,
    CASE 
        WHEN split IS NULL THEN TIMESTAMPDIFF(YEAR, formed, CURRENT_DATE)
        ELSE TIMESTAMPDIFF(YEAR, formed, split)
    END as longevity_years
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY longevity_years DESC;