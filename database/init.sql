-- Verwijderen tabellen

DROP TABLE if exists  dbo.cve;

--------------------------------------------------------
--  DB INFORMATIEVE BOEKEN - FREDERIK CRAUWELS  
--------------------------------------------------------

--------------------------------------------------------
--  Table UITGEVER
--------------------------------------------------------

  CREATE TABLE cve
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
TRUNCATE TABLE dbo.cve;
GO
 
-- import the file
BULK INSERT dbo.cve
FROM 'known_exploited_vulnerabilities.csv'
WITH
(
        FORMAT='CSV',
        FIRSTROW=2
)
GO