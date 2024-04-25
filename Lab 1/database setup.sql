DROP DATABASE IF EXISTS database1;

CREATE DATABASE database1;

USE database1;

CREATE TABLE `Medical records` (
    Profession VARCHAR(255) NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Age INT NOT NULL,
    Disease VARCHAR(20)
);

CREATE TABLE `Sports Survey` (
    `Name` VARCHAR(30) NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Profession VARCHAR(50) NOT NULL,
    `Favorite Sport` VARCHAR(30) NOT NULL,
    Age INT NOT NULL
);

SHOW VARIABLES LIKE "secure_file_priv";

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Medical records.csv' 
INTO TABLE `Medical records`
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Sports Survey.csv' 
INTO TABLE `Sports Survey`
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;