-- SQL SafeDiv the first by the second number or returns 0 number is equal to 0.
DELIMITER //

CREATE FUNCTION SafeDivi(a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE result FLOAT;
    
    IF b = 0 THEN
        RETURN 0;
    END IF;
    
    SET result = a / b;
    RETURN result;
END //

DELIMITER ;