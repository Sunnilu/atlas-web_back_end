-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

SELECT 
    band_name,
    CASE
        WHEN split is NULL THEN YEAR(CURDATE()) - first_album_year
        ELSE split - first_album_year
    END as lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;