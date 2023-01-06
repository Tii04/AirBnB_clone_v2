<<<<<<< HEAD
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED WITH mysql_native_password BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'
=======
-- MySQL script to prepare the server for the Project
-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
-- If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
>>>>>>> c8bf2a5b0fee0dbf2daffa353e1eecb6ea021746
