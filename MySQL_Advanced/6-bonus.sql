-- SQL script that creates a stored procedure
-- AddBonus that add a new correction
-- for a student.

DELIMITER //

CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score INT
)
BEGIN
    DECLARE v_project_id INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error adding bonus correction';
    END;
    
    START TRANSACTION;
    
    -- Check if project exists, or create it if it doesn't
    SELECT id INTO v_project_id 
    FROM projects 
    WHERE name = p_project_name;
    
    IF v_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (p_project_name);
        SET v_project_id = LAST_INSERT_ID();
    END IF;
    
    -- Add the correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (p_user_id, v_project_id, p_score);
    
    COMMIT;
END //

DELIMITER ;