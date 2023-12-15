CREATE DATABASE IF NOT EXISTS microbialites;
USE microbialites;

-- Creating the Waypoint table
CREATE TABLE Waypoint (
    WayptID INT PRIMARY KEY AUTO_INCREMENT,-- New auto-incremented ID
    WayptName VARCHAR(50), -- Original WayptName from the old database
    Latitude DECIMAL(10, 2) ,
    Longitude DECIMAL(10, 2),
    UTMZone1 INT,
    UTMZone2 CHAR(1),
    Datum VARCHAR(50),
    Projection VARCHAR(50),
    Fieldbook VARCHAR(100),
    FieldbookPage VARCHAR(50),
    Formation VARCHAR(50),
    SiteOrLocationName VARCHAR(100),
    DateCollected DATETIME,
    Elevation INT,
    ProjectName INT,
    MeasuredSection INT,
    SectionName VARCHAR(255),
    Comments TEXT
);

-- Creating the Coordinates table
CREATE TABLE Coordinates (
    CoordinateID INT PRIMARY KEY AUTO_INCREMENT,
    WayptID INT,
    Latitude DECIMAL(10, 2) ,
    Longitude DECIMAL(10, 2),
    Northing DECIMAL(10, 2),
    Easting DECIMAL(10, 2),
    FOREIGN KEY (WayptID) REFERENCES Waypoint(WayptID)
    ON DELETE CASCADE
);


