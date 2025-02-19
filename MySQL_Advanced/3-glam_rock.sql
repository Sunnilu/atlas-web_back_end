-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT 
    band_name,
    CASE
        WHEN split is NULL THEN 2025 - formed
        ELSE split - formed
    END 
    as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;