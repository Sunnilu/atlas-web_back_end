-- SQL SafeDiv the first by the second number or returns 0 number is equal to 0.

DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10,4)
DETERMINISTIC
BEGIN
    DECLARE result DECIMAL(10,4);
    
    IF b = 0 THEN
        RETURN 0;
    END IF;
    
    SET result = a / b;
    RETURN result;
END //

DELIMITER ;