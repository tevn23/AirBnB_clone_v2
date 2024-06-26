-- Prepares a MySQL server for the project development
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'HBNB_test_pwd_98';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
