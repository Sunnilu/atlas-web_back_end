-- Create a table users with country enum --

CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    -- country VARCHAR(2) NOT NULL DEFAULT 'US'
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);

-- ALTER TABLE users ADD CONSTRAINT chk_country CHECK (country IN ('US', 'CO', 'TN'));