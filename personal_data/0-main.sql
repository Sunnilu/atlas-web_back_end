-- setup mysql server
-- configure permissions
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'my_db')
BEGIN
    CREATE DATABASE my_db;
END;
IF NOT EXISTS (SELECT 1 FROM mysql.user WHERE User = 'root' AND Host = 'localhost') THEN
    CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
END IF;
GRANT ALL PRIVILEGES ON my_db.* TO 'root'@'localhost';

USE my_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    email VARCHAR(256)
);

INSERT INTO users(email) VALUES ("bob@dylan.com");
INSERT INTO users(email) VALUES ("bib@dylan.com");