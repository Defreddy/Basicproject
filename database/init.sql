-- Verwijderen tabellen

DROP TABLE if exists  cve.cveDetails;
DROP SCHEMA if exists cve;

--  DB CVE FREDERIK CRAUWELS  

CREATE SCHEMA cve;
USE cve;

-- Table cveDetails

  CREATE TABLE cveDetails
   (	
    cveId int NOT NULL PRIMARY KEY, 
	cveName VARCHAR(50), 
	vendorProject VARCHAR(50),
	product VARCHAR(50), 
    vulnerabilityName VARCHAR(50), 
    dateAdded date, 
    shortDescription text, 
    requiredAction text, 
    dueDate date,
    notes VARCHAR(50)
   ) ;

-- truncate the table first
TRUNCATE TABLE cve.cveDetails;

 
LOAD DATA INFILE '/etc/mysql/known_exploited_vulnerabilities.csv' 
INTO TABLE cveDetails 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;