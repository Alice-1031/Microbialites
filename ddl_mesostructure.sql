USE microbialites;

CREATE TABLE MesoStructure (
    MesoStructureID INT PRIMARY KEY auto_increment,
    MacroStructureID INT NOT NULL,
    WayptID INT NOT NULL,
    FOREIGN KEY (WayptID) REFERENCES Waypoint(WayptID) ON DELETE CASCADE ,
    FOREIGN KEY(MacrostructureID) REFERENCES MacroStructure(MacrostructureID) ON DELETE CASCADE 
);


CREATE TABLE MesoStructurePhotos (
    MesoStructureID INT,
    PhotoID INT,
    WayptID INT,
    MacroStructureID INT,
    InReport BOOLEAN, 
    OutcropPhoto BOOLEAN,
    Photomicrograph BOOLEAN,
    OtherImage BOOLEAN,
    CLImage BOOLEAN,
    OtherDocument BOOLEAN,
    RefrenceLink VARCHAR(255) NOT NULL,
    PRIMARY KEY (MacroStructureID, PhotoID),
    FOREIGN KEY (MacroStructureID) REFERENCES MacroStructure(MacroStructureID) ON DELETE CASCADE,
    FOREIGN KEY (WaypointID) REFERENCES Waypoint(WayptID) ON DELETE CASCADE
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
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure (MesoStructureID) ON DELETE CASCADE,
    FOREIGN KEY (GrainTypeID) REFERENCES MesoGrainType (GrainTypeID) ON DELETE SET NULL,
    FOREIGN KEY (GeneralTypeID) REFERENCES GeneralType (GeneralTypeID) ON DELETE SET NULL,
    FOREIGN KEY (ThinSectionPriorityID) REFERENCES ThinSectionPriority (ThinSectionPriorityID) ON DELETE SET NULL,
    FOREIGN KEY (MesoInhertianceID) REFERENCES MesoInheritance (MesoInhertianceID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStructureTypeID) REFERENCES MesoStructureType (MesoStructureTypeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStructureLaminaID) REFERENCES MesoStructureLamina (MesoStructureLaminaID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStructureLaminaPatternID) REFERENCES MesoStructureLaminaPattern (MesoStructurePatternID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStackingOverlapID) REFERENCES MesoStackingOverlap (MesoStackingOverlapID) ON DELETE SET NULL,
    FOREIGN KEY (MesoAlterationID) REFERENCES MesoAlteration (MesoAlterationID) ON DELETE SET NULL,
    FOREIGN KEY (MesoWavinessID) REFERENCES MesoWaviness (MesoWavinessID) ON DELETE SET NULL,
    FOREIGN KEY (MesoModalityID) REFERENCES MesoModalitySkewness (MesoModalityID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStackingOverlapID) REFERENCES MesoStackingOverlap (MesoStackingOverlapID) ON DELETE SET NULL,
    FOREIGN KEY (MesoAlterationID) REFERENCES MesoAlteration (MesoAlterationID) ON DELETE SET NULL,
    FOREIGN KEY (MesoWavinessID) REFERENCES MesoWaviness (MesoWavinessID) ON DELETE SET NULL,
    FOREIGN KEY (MesoModalityID) REFERENCES MesoModality (MesoModalityID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLaminaProfileID) REFERENCES MesoModalityProfile (MesoLaminaProfileID) ON DELETE SET NULL,
    FOREIGN KEY (MesoSynopticReliefID) REFERENCES MesoSynopticRelief (MesoSynopticReliefID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLaminaInhertianceID) REFERENCES MesoLaminaInhertiance (MesoLaminaInhertianceID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLateralContinuityID) REFERENCES MesoLateralContinuity (MesoLateralContinuityID) ON DELETE SET NULL,
    FOREIGN KEY (MesoWallID) REFERENCES MesoWall(MesoWallID) ON DELETE SET NULL,
    FOREIGN KEY (MesoMacroLaminaeID) REFERENCES MesoMacroLaminae (MesoMacroLaminaeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLaminaShapeID) REFERENCES MesoLaminaShape (MesoLaminaShapeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStructureTypeID) REFERENCES MesoStructureType (MesoStructureTypeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoMacroLaminaeID) REFERENCES MesoMacroLaminae (MesoMacroLaminaeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLaminaShapeID) REFERENCES MesoLaminaShape (MesoLaminaShapeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStructureTypeID) REFERENCES MesoStructureType (MesoStructureTypeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoClotTypeID) REFERENCES MesoClotType (MesoClotTypeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoClotShapeID) REFERENCES MesoClotShape (MesoClotShapeID) ON DELETE SET NULL

    PRIMARY KEY (MesoStructureID, PhotoID),
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure(MesoStructureID) ON DELETE CASCADE,
    FOREIGN KEY (WayptID) REFERENCES Waypoint(WayptID) ON DELETE CASCADE
);

CREATE TABLE InternationalSampleNumber(
    MesoStructureID INT PRIMARY KEY,
    IGSNIntlGeoSampleNumber INT,
    FOREIGN KEY (MesoStructureID) REFERENCES  MesoStructure (MesoStructureID) ON DELETE CASCADE
);

CREATE TABLE MesoStructureSampleName(
	MesoStructureID INT PRIMARY KEY,
    MesoStructureName VARCHAR(100) UNIQUE,
    FOREIGN KEY (MesoStructureID) REFERENCES  MesoStructure (MesoStructureID) ON DELETE CASCADE
);

CREATE TABLE TextureType (
    TextureTypeID INT PRIMARY KEY auto_increment,
	MesoStructureTextureType VARCHAR(100)
);

CREATE TABLE MesoStructureTextureTypes (
    MesoStructureID INT,
    TextureTypeID INT,
    PRIMARY KEY (MesoStructureID, TextureTypeID),
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure (MesoStructureID) ON DELETE CASCADE,
    FOREIGN KEY (TextureTypeID) REFERENCES TextureType (TextureTypeID) ON DELETE CASCADE
);

CREATE TABLE Architecture (
    ArchitectureID INT PRIMARY KEY auto_increment,
    ArchitectureType VARCHAR(100)
);

CREATE TABLE MesoStructureArchitecture (
    MesoStructureID INT,
    ArchitectureID INT,
    PRIMARY KEY (MesoStructureID, ArchitectureID),
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure (MesoStructureID) ON DELETE CASCADE,
    FOREIGN KEY (ArchitectureID) REFERENCES Architecture (ArchitectureID) ON DELETE CASCADE
);

CREATE TABLE MesoGrainType (
    GrainTypeID INT PRIMARY KEY,
    GrainType VARCHAR(100)
);

CREATE TABLE ThinSectionPriority(
    ThinSectionPriorityID INT PRIMARY KEY auto_increment,
    PriorityType VARCHAR(50)
);

CREATE TABLE MesoInheritance(
    MesoInheritanceID INT PRIMARY KEY,
    Inheritance VARCHAR(50)
);

CREATE TABLE MesoStructureType (
   MesoStructureTypeID INT PRIMARY KEY,
   Mesostructure VARCHAR(50)
);

CREATE TABLE MesoStructureLaminaPattern (
    MesoStructureLaminaPatternID INT PRIMARY KEY,
    PatternCouplet VARCHAR(50)
);

CREATE TABLE MesoStackingOverlap (
    MesoStackingOverlapID INT PRIMARY KEY,
    StackingOverlap VARCHAR(20)

);

CREATE TABLE MesoAlternation (
    MesoAlterationID INT PRIMARY KEY,
    Alternation VARCHAR(20)
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
    LamProfile VARCHAR(20)
);

CREATE TABLE MesoSynopticRelief (

    MesoSynopticReliefID INT PRIMARY KEY,
    SynopticRelief VARCHAR(20)
);


CREATE TABLE MesoLaminaInheritance (
    MesoLaminaInheritanceID INT PRIMARY KEY,
    Inheritance VARCHAR(20)
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


CREATE TABLE MesoLaminaShape (
    MesoLaminaShapeID INT PRIMARY KEY,
    LaminaShape VARCHAR(20),
    Description VARCHAR(100)
);


CREATE TABLE MesoClotType (

    MesoClotTypeID INT PRIMARY KEY,
    ClotType VARCHAR(20)
);

CREATE TABLE MesoClotShape (

    MesoClotShapeID INT PRIMARY KEY,
    ClotShape VARCHAR(20)
);


CREATE TABLE Priority(
	ID INT auto_increment PRIMARY KEY,
    Priority VARCHAR(50)
);

CREATE TABLE MesoStructureProperties (

    MesoStructureID INT PRIMARY KEY,
    GrainTypeID INT,
    ThinSectionPriorityID INT,
    MesoInheritanceID INT,
    MesoStructureLaminaPatternID INT,
    MesoStackingOverlapID INT,
    MesoAlterationID INT,
    MesoWavinessID INT,
    MesoModalityID INT,
    MesoLaminaProfileID INT,
    LaminaThickness DECIMAL(5,2),
    MesoSynopticReliefID INT,
    MesoLaminaInheritanceID INT,
    MesoLateralContinuityID INT, 
    MesoWallsID INT,
    MesoMacroLaminaeID INT,
    MesoLaminaShapeID INT,
    MesoStructureTypeID INT,
    MesoClotShapeID INT,
    MesoClotSize DECIMAL(5,2),
    InTheFRUInterval BOOLEAN,
    AnalysisPriority INT,
    MacroStructureID INT,
    FieldDescription VARCHAR (100), 
    Lithology VARCHAR(20),
    RockDescription VARCHAR(100),
    SampleSize VARCHAR(100),
    PeelAndSEMPriority VARCHAR(15),
    ThinSectionMade BOOLEAN,
    C_N_Priority INT,
    Wavelength FLOAT,
    AmplitudeOrHeight FLOAT,
    MicrobialiteType VARCHAR(20),
    MesoClotTypeID INT,
    BriefNotes VARCHAR(100),
    FOREIGN KEY (MesoStructureID) REFERENCES MesoStructure (MesoStructureID) ON DELETE CASCADE,
    FOREIGN KEY (GrainTypeID) REFERENCES MesoGrainType (GrainTypeID) ON DELETE SET NULL,
    FOREIGN KEY (ThinSectionPriorityID) REFERENCES ThinSectionPriority (ThinSectionPriorityID) ON DELETE SET NULL,
    FOREIGN KEY (MesoInheritanceID) REFERENCES MesoInheritance (MesoInheritanceID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStructureTypeID) REFERENCES MesoStructureType (MesoStructureTypeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStructureLaminaPatternID) REFERENCES MesoStructureLaminaPattern (MesoStructureLaminaPatternID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStackingOverlapID) REFERENCES MesoStackingOverlap (MesoStackingOverlapID) ON DELETE SET NULL,
    FOREIGN KEY (MesoAlterationID) REFERENCES MesoAlternation (MesoAlterationID) ON DELETE SET NULL,
    FOREIGN KEY (MesoWavinessID) REFERENCES MesoWaviness (MesoWavinessID) ON DELETE SET NULL,
    FOREIGN KEY (MesoModalityID) REFERENCES MesoModalitySkewness (MesoModalityID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStackingOverlapID) REFERENCES MesoStackingOverlap (MesoStackingOverlapID) ON DELETE SET NULL,
    FOREIGN KEY (MesoWavinessID) REFERENCES MesoWaviness (MesoWavinessID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLaminaProfileID) REFERENCES MesoLaminaProfile (MesoLaminaProfileID) ON DELETE SET NULL,
    FOREIGN KEY (MesoSynopticReliefID) REFERENCES MesoSynopticRelief (MesoSynopticReliefID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLaminaInheritanceID) REFERENCES MesoLaminaInheritance (MesoLaminaInheritanceID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLateralContinuityID) REFERENCES MesoLateralContinuity (MesoLateralContinuityID) ON DELETE SET NULL,
    FOREIGN KEY (MesoWallsID) REFERENCES MesoWalls(MesoWallsID) ON DELETE SET NULL,
    FOREIGN KEY (MesoMacroLaminaeID) REFERENCES MesoMacroLaminae (MesoMacroLaminaeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLaminaShapeID) REFERENCES MesoLaminaShape (MesoLaminaShapeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoStructureTypeID) REFERENCES MesoStructureType (MesoStructureTypeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoMacroLaminaeID) REFERENCES MesoMacroLaminae (MesoMacroLaminaeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoLaminaShapeID) REFERENCES MesoLaminaShape (MesoLaminaShapeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoClotTypeID) REFERENCES MesoClotType (MesoClotTypeID) ON DELETE SET NULL,
    FOREIGN KEY (MesoClotShapeID) REFERENCES MesoClotShape (MesoClotShapeID) ON DELETE SET NULL,
    FOREIGN KEY(AnalysisPrioriy) REFERENCES Priority (ID) ON DELETE SET NULL,
    FOREIGN KEY(MacroStructureID) REFERENCES MacroStructure(MacroStructureID) ON DELETE CASCADE
);

