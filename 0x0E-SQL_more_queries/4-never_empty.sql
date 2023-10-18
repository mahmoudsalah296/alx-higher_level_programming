-- a script that creates the table id_not_null
-- id INT with the default value 1
-- name VARCHAR(256)
-- If the table id_not_null already exists, your script should not fail
-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
