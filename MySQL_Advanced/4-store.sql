-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

DELIMITER //

CREATE TRIGGER decrease_item_quantity
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE existing_quantity INT;
    
    -- Get current quantity
    SELECT quantity INTO existing_quantity 
    FROM items WHERE name = NEW.item_name;
    
    -- Update quantity
    UPDATE items 
    SET quantity = existing_quantity - NEW.number
    WHERE name = NEW.item_name;
    
    -- Log the change
    INSERT INTO inventory_changes (
        item_name,
        old_quantity,
        new_quantity,
        change_type,
        changed_at
    ) VALUES (
        NEW.item_name,
        existing_quantity,
        existing_quantity - NEW.number,
        'ORDER_DEDUCTION',
        NOW()
    );
END//

DELIMITER ;