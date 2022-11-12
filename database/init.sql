-- Verwijderen tabellen

DROP TABLE if exists  cve.cveDetails;
DROP SCHEMA if exists cve;

--  DB CVE FREDERIK CRAUWELS  

CREATE SCHEMA cve;
USE cve;

-- Table cveDetails

  CREATE TABLE cveDetails
   (	
    cveID int NOT NULL, 
    cveName VARCHAR(50), 
	  vendorProject text,
	  product text, 
    vulnerabilityName text, 
    dateAdded date, 
    shortDescription text, 
    requiredAction text, 
    dueDate date,
    notes text
    CONSTRAINT pk_cveDetails PRIMARY KEY(cveID)
   ) ;

-- truncate the table first
TRUNCATE TABLE cve.cveDetails;

LOAD DATA INFILE '/var/lib/mysql-files/known_exploited_vulnerabilities.csv' 
INTO TABLE cveDetails 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;