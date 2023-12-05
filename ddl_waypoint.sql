USE microbialites;

-- Creating the Waypoint table
CREATE TABLE Waypoint (
    WaypointID INT PRIMARY KEY,
    Latitude DECIMAL(10, 2),
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
    Comments TEXT,
);

-- Creating the Coordinates table
CREATE TABLE Coordinates (
    Latitude DECIMAL(10, 2),
    Longitude DECIMAL(10, 2),
    Northing DECIMAL(10, 2),
    Easting DECIMAL(10, 2),
    PRIMARY KEY (Latitude, Longitude),
    FOREIGN KEY (Latitude, Longitude) REFERENCES Waypoint(Latitude, Longitude)
);
