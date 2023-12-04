USE microbialites;

CREATE TABLE MesoStructure (
    MesoStructureID INT PRIMARY KEY,
    WayptID INT,
    FOREIGN KEY (WayptID) REFRENCES Waypoint(WayptID)
);


CREATE TABLE MesoStructurePhotos (
    MesoStructureID INT,
    PhotoID INT,
    WayptID INT,
    MacroStructureID,
    InReport BOOLEAN, 
    OutcropPhoto BOOLEAN,
    Photomicrograph BOOLEAN,
    OtherImage BOOLEAN,
    CLImage BOOLEAN,
    OtherDocument BOOLEAN,
    RefrenceLink VARCHAR(255) NOT NULL,
    PRIMARY KEY (MacroStructureID, PhotoID),
    FOREIGN KEY (MacroStructureID) REFERENCES MacroStructure(MacroStructureID),
    FOREIGN KEY (WaypointID) REFERENCES Waypoint(WayptID)
);

#fielddescription might need to be made larger
#lithology type might be incorrect but there was no entires for it on access
CREATE TABLE MesoStructureProperties (

    MesoStructureID INT PRIMARY KEY,
    GrainTypeID INT,
    GeneralTypeID INT,
    ThinSectionPriorityID INT,
    MesoInhertianceID INT,
    MesoStructureTypeID INT,
    MesoStructureLaminaID INT,
    MesoStructureLaminaPatternID INT,
    MesoStackingOverlapID INT,
    MesoAlterationID INT,
    MesoWavinessID INT,
    MesoModailityID INT,
    MesoLaminaProfileID INT,
    MesoSynopticReliefID INT,
    MesoLaminaInhertianceID INT,
    MesoLateralContinuityID INT, 
    MesoWallID INT,
    MesoMacroLaminaeID INT,
    MesoLaminaShapeID INT,
    MesoStructureTypeID INT,
    MesoClotTypeID INT,
    MesoClotShapeID INT,
    InTheFRUInterval INT,
    AnaylsisPriority VARCHAR(15),
    MacroStructureID INT,
    FieldDescription VARCHAR (100), 
    Lithology VARCHAR(20),
    RockDescription VARCHAR(100),
    SampleSize INT,
    PeelAndSEMPriority VARCHAR(15),
    ThinSectionMade BOOLEAN,
    C_N_Priority VARCHAR(15),
    WaveLength FLOAT,
    AmplitudeOrHeight FLOAT,
    MicrobialiteType VARCHAR(20),
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure (MesoStructureID),
    FOREIGN KEY (GrainTypeID) REFERENCES MesoGrainType (GrainTypeID),
    FOREIGN KEY (GeneralTypeID) REFERENCES GeneralType (GeneralTypeID),
    FOREIGN KEY (ThinSectionPriorityID) REFERENCES ThinSectionPriority (ThinSectionPriorityID),
    FOREIGN KEY (MesoInhertianceID) REFERENCES MesoInheritance (MesoInhertianceID),
    FOREIGN KEY (MesoStructureTypeID) REFERENCES MesoStructureType (MesoStructureTypeID),
    FOREIGN KEY (MesoStructureLaminaID) REFERENCES MesoStructureLamina (MesoStructureLaminaID),
    FOREIGN KEY (MesoStructureLaminaPatternID) REFERENCES MesoStructureLaminaPattern (MesoStructurePatternID),
    FOREIGN KEY (MesoStackingOverlapID) REFERENCES MesoStackingOverlap (MesoStackingOverlapID),
    FOREIGN KEY (MesoAlterationID) REFERENCES MesoAlteration (MesoAlterationID),
    FOREIGN KEY (MesoWavinessID) REFERENCES MesoWaviness (MesoWavinessID),
    FOREIGN KEY (MesoModalityID) REFERENCES MesoModalitySkewness (MesoModalityID),
    FOREIGN KEY (MesoStackingOverlapID) REFERENCES MesoStackingOverlap (MesoStackingOverlapID),
    FOREIGN KEY (MesoAlterationID) REFERENCES MesoAlteration (MesoAlterationID),
    FOREIGN KEY (MesoWavinessID) REFERENCES MesoWaviness (MesoWavinessID),
    FOREIGN KEY (MesoModalityID) REFERENCES MesoModality (MesoModalityID),
    FOREIGN KEY (MesoLaminaProfileID) REFERENCES MesoModalityProfile (MesoLaminaProfileID),
    FOREIGN KEY (MesoSynopticReliefID) REFERENCES MesoSynopticRelief (MesoSynopticReliefID),
    FOREIGN KEY (MesoLaminaInhertianceID) REFERENCES MesoLaminaInhertiance (MesoLaminaInhertianceID),
    FOREIGN KEY (MesoLateralContinuityID) REFERENCES MesoLateralContinuity (MesoLateralContinuityID),
    FOREIGN KEY (MesoWallID) REFERENCES MesoWall(MesoWallID),
    FOREIGN KEY (MesoMacroLaminaeID) REFERENCES MesoMacroLaminae (MesoMacroLaminaeID),
    FOREIGN KEY (MesoLaminaShapeID) REFERENCES MesoLaminaShape (MesoLaminaShapeID),
    FOREIGN KEY (MesoStructureTypeID) REFERENCES MesoStructureType (MesoStructureTypeID),
    FOREIGN KEY (MesoMacroLaminaeID) REFERENCES MesoMacroLaminae (MesoMacroLaminaeID),
    FOREIGN KEY (MesoLaminaShapeID) REFERENCES MesoLaminaShape (MesoLaminaShapeID),
    FOREIGN KEY (MesoStructureTypeID) REFERENCES MesoStructureType (MesoStructureTypeID),
    FOREIGN KEY (MesoClotTypeID) REFERENCES MesoClotType (MesoClotTypeID),
    FOREIGN KEY (MesoClotShapeID) REFERENCES MesoClotShape (MesoClotShapeID)

);

CREATE TABLE InternationalSampleNumber(

    MesoStructureID INT PRIMARY KEY,
    IGSNInt1GeoSampleNumberID INT,
    FOREIGN KEY (MesoStructureID) REFERENCES  MesoStructure (MesoStructureID)

);

CREATE TABLE MesoStructureTextureTypes (

    MesoStructureID INT,
    TextureTypesID INT,
    Desciption VARCHAR(30),
    PRIMARY KEY (MesoStructureID, TextureTypeID),
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure (MesoStructureID),
    FOREIGN KEY (TextureTypeID) REFERENCES TextureType (TextureTypeID)
);

CREATE TABLE MesoStructureArchitecture (

    MesoStructureID INT,
    ArchitectureID INT,
    Desciption VARCHAR(30),
    PRIMARY KEY (MesoStructureID, ArchitectureID),
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure (MesoStructureID),
    FOREIGN KEY (ArchitectureID) REFERENCES Architecture (ArchitectureID)
);

CREATE TABLE MesoGrainType (

    GrainTypeID INT PRIMARY KEY,
    GrainType VARCHAR(20)
);

CREATE TABLE GeneralType (

    GeneralTypeID INT PRIMARY KEY,
    MesoStructure VARCHAR(20)
);

CREATE TABLE ThinSectionPriority(

    ThinSectionPriorityID INT PRIMARY KEY,
    PriorityType VARCHAR(20)
);

CREATE TABLE MesoInheritance(

    MesoInheritanceID INT PRIMARY KEY,
    Inheritance VARCHAR(20)
);

CREATE TABLE MesoStructureType (

   MesoStructureTypeID INT PRIMARY KEY,
   MesoStructure VARCHAR(20)
);

CREATE TABLE MesoStructureLamina (

    MesoStructureLaminaID INT PRIMARY KEY,
    LaminaThickness VARCHAR(20),
    LaminaProfile VARCHAR(20)
);

CREATE TABLE MesoStructureLaminaPattern (

    MesoStructureLaminaPatternID INT PRIMARY KEY,
    PatternCouplet VARCHAR(20)
);

CREATE TABLE MesoStackingOverlap (

    MesoStackingOverlapID INT PRIMARY KEY,
    StackingOverlap VARCHAR(20)

);

CREATE TABLE MesoAlternation (

    MesoAlterationID INT PRIMARY KEY,
    Alteration VARCHAR(20)
);

CREATE TABLE MesoWaviness (

    MesoWavinessID INT PRIMARY KEY,
    Waviness VARCHAR(20)
);

CREATE TABLE MesoModalitySkewness (

    MesoModalityID INT PRIMARY KEY,
    ModalitySkewness VARCHAR(20)
);

CREATE TABLE MesoLaminaProfile (

    MesoLaminaProfileID INT PRIMARY KEY,
    LaminaProfile VARCHAR(20)
);

CREATE TABLE MesoSynopticRelief (

    MesoSynopticReliefID INT PRIMARY KEY,
    SynopticRelief VARCHAR(20)
);

#Im not sure if field was correct
CREATE TABLE MesoLaminaIneritance (

    MesoLaminaInheritanceID INT PRIMARY KEY,
    FIELD1 VARCHAR(20)
);

CREATE TABLE MesoLateralContinuity (

    MesoLateralContinuityID INT PRIMARY KEY,
    LateralContinuity VARCHAR(20)
);

CREATE TABLE MesoWalls (

    MesoWallsID INT PRIMARY KEY,
    Walls VARCHAR(20)
);

CREATE TABLE MesoMacroLaminae (

    MesoMacroLaminaeID INT PRIMARY KEY,
    MacroLaminae VARCHAR (20)
);

CREATE TABLE Architecture (

    ArchitectureID INT PRIMARY KEY,
    ArchitectureType VARCHAR(20)
);

CREATE TABLE MesoLaminaShape (

    MesoLaminaShapeID INT PRIMARY KEY,
    LaminaShape VARCHAR(20),
    Description VARCHAR(20)
);

CREATE TABLE TextureType (

    TextureTypeID INT PRIMARY KEY,
    MesoStructureTextureType VARCHAR(20)
);

CREATE TABLE MesoClotType (

    MesoClotTypeID INT PRIMARY KEY,
    ClotType VARCHAR(20)
);

CREATE TABLE MesoClotShape (

    MesoClotShapeID INT PRIMARY KEY,
    ClotShape VARCHAR(20)
);

