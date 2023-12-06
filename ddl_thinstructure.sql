-- ThinStructures Table
USE microbialites;

CREATE TABLE ThinStructures (
    ThinStructureID INT PRIMARY KEY AUTO_INCREMENT,
    WaypointID INT NOT NULL,
    MacroStructureID INT NOT NULL,
    MesoStructureID INT NOT NULL,
    FOREIGN KEY (WaypointID) REFERENCES Waypoint(WaypointID),
    FOREIGN KEY (MacroStructureID) REFERENCES MacroStructures(MacroStructureID),
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructures(MesoStructureID)
);

-- ThinStructureProperties Table
CREATE TABLE ThinStructureProperties (
    ThinStructureID INT PRIMARY KEY,
    PorosityPercentEst DECIMAL,
    CementFilledPorosity DECIMAL,
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID)
);

-- ThinStructureTextureTypes Table
CREATE TABLE ThinStructureTextureTypes (
    ThinStructureID INT,
    ThinTextureTypeID INT,
    PRIMARY KEY (ThinStructureID, ThinTextureTypeID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID),
    FOREIGN KEY (ThinTextureTypeID) REFERENCES ThinTextureTypes(ThinTextureTypeID)
);

-- ThinStructureClasticGrains Table
CREATE TABLE ThinStructureClasticGrains (
    ThinStructureID INT,
    ClasticGrainsID INT,
    PRIMARY KEY (ThinStructureID, ClasticGrainsID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID),
    FOREIGN KEY (ClasticGrainsID) REFERENCES ClasticGrains(ClasticGriansID)
);

-- ThinStructureCementTypes Table
CREATE TABLE ThinStructureCementTypes (
    ThinStructureID INT,
    CementTypeID INT,
    PRIMARY KEY (ThinStructureID, CementTypeID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID),
    FOREIGN KEY (CementTypeID) REFERENCES CementTypes(CementTypeID)
);

-- ThinStructureMineralogyTypes Table
CREATE TABLE ThinStructureMineralogyTypes (
    ThinStructureID INT,
    MineralogyID INT,
    PRIMARY KEY (ThinStructureID, MineralogyID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID),
    FOREIGN KEY (MineralogyID) REFERENCES MineralogyTypes(MineralogyID)
);

-- ThinStructurePorosityType Table
CREATE TABLE ThinStructurePorosityType (
    ThinStructureID INT,
    PorosityID INT,
    PRIMARY KEY (ThinStructureID, PorosityID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID),
    FOREIGN KEY (PorosityID) REFERENCES PorosityType(PorosityTypeID)
);

-- ThinStructurePhotos Table
CREATE TABLE ThinStructurePhotos (
    ThinStructureID INT,
    PhotoID INT,
    WaypointID INT,
    InReport BOOLEAN,
    OutcropPhoto BOOLEAN,
    Photomicrograph BOOLEAN,
    OtherImage BOOLEAN,
    CLImage BOOLEAN,
    OtherDocument BOOLEAN,
    ReferenceLink VARCHAR(255),
    PRIMARY KEY (ThinStructureID, PhotoID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID),
    FOREIGN KEY (WaypointID) REFERENCES Waypoints(WaypointID)
);

-- ThinTextureTypes Table
CREATE TABLE ThinTextureTypes (
    ThinTextureTypeID INT PRIMARY KEY,
    Texture VARCHAR(255),
    Sort INT
);

-- ClasticGrains Table
CREATE TABLE ClasticGrains (
    ClasticGriansID INT PRIMARY KEY,
    ClasticGrainType VARCHAR(255),
    Sort INT
);

-- CementTypes Table
CREATE TABLE CementTypes (
    CementTypeID INT PRIMARY KEY,
    Cement VARCHAR(255),
    CementDesc VARCHAR(255),
    Sort INT
);

-- MineralogyTypes Table
CREATE TABLE MineralogyTypes (
    MineralogyID INT PRIMARY KEY,
    Mineralogy VARCHAR(255),
    MineralDesc VARCHAR(255)
);

-- PorosityType Table
CREATE TABLE PorosityType (
    PorosityTypeID INT PRIMARY KEY,
    Porosity VARCHAR(255),
    Sort INT
);

