-- SQL SafeDiv the first by the second number or returns 0 number is equal to 0.


CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    
    IF b = 0 THEN
        RETURN 0;
    END IF;
    
    SET result = a / b;
    RETURN result;
END; 
