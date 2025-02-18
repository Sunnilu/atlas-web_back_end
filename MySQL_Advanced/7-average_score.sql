-- SQL script that creates a stored procedure ComputeAverageScoreForUser that updates the average score of a user.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE v_average_score FLOAT;
    
    -- Calculate average score for the user
    SELECT AVG(score) INTO v_average_score
    FROM corrections
    WHERE user_id = p_user_id;
    
    -- Update the user's average score
    UPDATE users
    SET average_score = COALESCE(v_average_score, 0)
    WHERE id = p_user_id;
END //

DELIMITER ;