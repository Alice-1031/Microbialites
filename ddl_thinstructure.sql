USE microbialites;

CREATE TABLE ThinStructures (
    ThinStructureID INT PRIMARY KEY AUTO_INCREMENT,
    WayptID INT NOT NULL,
    MacroStructureID INT NOT NULL,
    MesoStructureID INT NOT NULL,
    FOREIGN KEY (WayptID) REFERENCES Waypoint(WayptID) ON DELETE CASCADE,
    FOREIGN KEY (MacroStructureID) REFERENCES MacroStructure(MacroStructureID) ON DELETE CASCADE,
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure(MesoStructureID) ON DELETE CASCADE
);

CREATE TABLE ThinStructurePhotos (
    ThinStructureID INT,
    PhotoID INT,
    InReport BOOLEAN,
    OutcropPhoto BOOLEAN,
    Photomicrograph BOOLEAN,
    OtherImage BOOLEAN,
    CLImage BOOLEAN,
    OtherDocument BOOLEAN,
    ReferenceLink VARCHAR(255),
    PRIMARY KEY (ThinStructureID, PhotoID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID) ON DELETE CASCADE,
    FOREIGN KEY (PhotoID) REFERENCES photos(PhotoID) ON DELETE CASCADE
);

-- ThinStructureProperties Table
CREATE TABLE ThinStructureProperties (
    ThinStructureID INT PRIMARY KEY,
    PorosityPercentEst DECIMAL,
    CementFilledPorosity DECIMAL,
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID) ON DELETE CASCADE
);

-- ThinTextureTypes Table
CREATE TABLE ThinTextureTypes (
    ThinTextureTypeID INT PRIMARY KEY auto_increment,
    Texture VARCHAR(255)
);

-- ThinStructureTextureTypes Table
CREATE TABLE ThinStructureTextureTypes (
    ThinStructureID INT,
    ThinTextureTypeID INT,
    PRIMARY KEY (ThinStructureID, ThinTextureTypeID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID) ON DELETE CASCADE,
    FOREIGN KEY (ThinTextureTypeID) REFERENCES ThinTextureTypes(ThinTextureTypeID) ON DELETE CASCADE
);

-- ClasticGrains Table
CREATE TABLE ClasticGrains (
    ClasticGrainsID INT PRIMARY KEY,
<<<<<<< HEAD
    ClasticGrainType VARCHAR(255),
    Sort INT
=======
    ClasticGrainType VARCHAR(255)
);

-- ThinStructureClasticGrains Table
CREATE TABLE ThinStructureClasticGrains (
    ThinStructureID INT,
    ClasticGrainsID INT,
    PRIMARY KEY (ThinStructureID, ClasticGrainsID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID) ON DELETE CASCADE,
    FOREIGN KEY (ClasticGrainsID) REFERENCES ClasticGrains(ClasticGrainsID) ON DELETE CASCADE
>>>>>>> 52a8a9a (Final updates to ddl files complete with cascades)
);

-- CementTypes Table
CREATE TABLE CementTypes (
    CementTypeID INT PRIMARY KEY,
    Cement VARCHAR(255),
    CementDesc VARCHAR(255)
);

-- ThinStructureCementTypes Table
CREATE TABLE ThinStructureCementTypes (
    ThinStructureID INT,
    CementTypeID INT,
    PRIMARY KEY (ThinStructureID, CementTypeID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID) ON DELETE CASCADE,
    FOREIGN KEY (CementTypeID) REFERENCES CementTypes(CementTypeID) ON DELETE CASCADE
);


-- MineralogyTypes Table
CREATE TABLE MineralogyTypes (
    MineralogyID INT PRIMARY KEY,
    Mineralogy VARCHAR(255),
    MineralDesc VARCHAR(255)
);

-- ThinStructureMineralogyTypes Table
CREATE TABLE ThinStructureMineralogyTypes (
    ThinStructureID INT,
    MineralogyID INT,
    PRIMARY KEY (ThinStructureID, MineralogyID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID) ON DELETE CASCADE,
    FOREIGN KEY (MineralogyID) REFERENCES MineralogyTypes(MineralogyID) ON DELETE CASCADE
);

-- PorosityType Table
CREATE TABLE PorosityType (
    PorosityTypeID INT PRIMARY KEY,
    Porosity VARCHAR(255)   
    
);

-- ThinStructurePorosityType Table
CREATE TABLE ThinStructurePorosityType (
    ThinStructureID INT,
    PorosityID INT,
    PRIMARY KEY (ThinStructureID, PorosityID),
    FOREIGN KEY (ThinStructureID) REFERENCES ThinStructures(ThinStructureID) ON DELETE CASCADE,
    FOREIGN KEY (PorosityID) REFERENCES PorosityType(PorosityTypeID) ON DELETE CASCADE
);



