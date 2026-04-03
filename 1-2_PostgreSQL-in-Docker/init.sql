-- Create a sample table named 'users' with relevant fields
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,           -- SERIAL auto-incrementing ID
    name VARCHAR(100) NOT NULL,      -- Name 100 characters max
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email address not null
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of creation
);

-- Insert sample data
INSERT INTO users (name, email) VALUES
    ('Benjamin Dubois', 'benjamin@example.com'),
    ('Marie Martin', 'marie.martin@example.com'),
    ('Jean Dupont', 'jean.dupont@example.com'),
    ('Sophie Laurent', 'sophie.laurent@example.com'),
    ('Lucas Bernard', 'lucas.bernard@example.com');

-- Query to verify data insertion
SELECT * FROM users;