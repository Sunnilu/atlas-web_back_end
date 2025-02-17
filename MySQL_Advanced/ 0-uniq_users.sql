---
title: "MySQL Table Creation"
---

# Create Table for Users

```sql
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- Auto-increment and primary key
    email VARCHAR(255) NOT NULL UNIQUE,      -- Email, not null, and unique
    name VARCHAR(255)                            -- Name
);
