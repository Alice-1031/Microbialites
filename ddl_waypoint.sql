USE microbialites;

-- Creating the Waypoint table
CREATE TABLE Waypoint (
    WayptID INT PRIMARY KEY AUTO_INCREMENT,
    WaypointName VARCHAR(50), -- allow users to have their own naming convention
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
    Latitude DECIMAL(10, 2),
    Longitude DECIMAL(10, 2),
    Northing DECIMAL(10, 2),
    Easting DECIMAL(10, 2),
    FOREIGN KEY (WayptID) REFERENCES Waypoint(WayptID)
);


