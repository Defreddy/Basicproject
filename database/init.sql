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
--	CONSTRAINT pk_uitgever PRIMARY KEY(uitgeverId),
--       UNIQUE(naam)
   ) ;

-- truncate the table first
TRUNCATE TABLE cve.cveDetails;
GO
 
-- import the file
BULK INSERT cve.cveDetails
FROM '/etc/mysql/known_exploited_vulnerabilities.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
        FIELDTERMINATOR = ',',  --CSV field delimiter
        ROWTERMINATOR = '\n',   --Use to shift the control to next row
        TABLOCK
)
GO