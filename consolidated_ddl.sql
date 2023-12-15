-- MacroStructure
USE microbialites;

CREATE TABLE MacroStructure (
    MacrostructureID INT PRIMARY KEY AUTO_INCREMENT,
    WayptID INT NOT NULL,
    FOREIGN KEY (WayptID) REFERENCES Waypoint(WayptID) ON DELETE CASCADE   
);

CREATE TABLE MacroStructurePhotos (
    MacroStructureID INT,
    PhotoID INT NOT NULL,
    WayptID INT NOT NULL, 
    InReport BOOLEAN,
    OutcropPhoto BOOLEAN,
    Photomicrograph BOOLEAN,
    OtherImage BOOLEAN,
    CLImage BOOLEAN,
    OtherDocument BOOLEAN,
    ReferenceLink VARCHAR(255) NOT NULL,
    PRIMARY KEY (MacroStructureID, PhotoID),
    FOREIGN KEY (MacroStructureID) REFERENCES MacroStructure(MacrostructureID) ON DELETE CASCADE,
    FOREIGN KEY (WayptID) REFERENCES Waypoint(WayptID) ON DELETE CASCADE
);

CREATE TABLE MegaStructureType (
    TypeID INT AUTO_INCREMENT PRIMARY KEY,
	Megastructure VARCHAR(100) NOT NULL
);

CREATE TABLE MegaStructureShape (
    ShapeID INT AUTO_INCREMENT PRIMARY KEY,
    Megastructure VARCHAR(100) NOT NULL
    
);

CREATE TABLE MegaStructureSize (
    SizeID INT AUTO_INCREMENT PRIMARY KEY,
    Megastructure VARCHAR(255) NOT NULL
   
);

CREATE TABLE Substrate (
    SubstrateID INT AUTO_INCREMENT PRIMARY KEY,
    SubstrateName VARCHAR(255) NOT NULL
);

CREATE TABLE PlanView (
    PlanViewID INT AUTO_INCREMENT PRIMARY KEY,
    PlanViewName VARCHAR(255) NOT NULL
);

CREATE TABLE Linkage (
    LinkageID INT AUTO_INCREMENT PRIMARY KEY,
    LinkageName VARCHAR(255) NOT NULL
);

CREATE TABLE Initiation (
    InitiationID INT AUTO_INCREMENT PRIMARY KEY,
    InitiationName VARCHAR(255) NOT NULL
);

CREATE TABLE Spacing (
    SpacingID INT AUTO_INCREMENT PRIMARY KEY,
    SpacingName VARCHAR(255) NOT NULL
);

CREATE TABLE Shape (
    ShapeID INT AUTO_INCREMENT PRIMARY KEY,
    ShapeName VARCHAR(255) NOT NULL
);

CREATE TABLE ShapeLayering (
    ShapeLayeringID INT AUTO_INCREMENT PRIMARY KEY,
    ShapeLayeringName VARCHAR(255) NOT NULL
);

CREATE TABLE ColumnShape (
    ColumnShapeID INT AUTO_INCREMENT PRIMARY KEY,
    ColumnShapeName VARCHAR(255) NOT NULL
);

CREATE TABLE ShapeDome (
    ShapeDomeID INT AUTO_INCREMENT PRIMARY KEY,
    ShapeDomeName VARCHAR(255) NOT NULL
);

CREATE TABLE ConicalShape (
    ConicalShapeID INT AUTO_INCREMENT PRIMARY KEY,
    ConicalShapeName VARCHAR(255) NOT NULL
);

CREATE TABLE Attitude (
    AttitudeID INT AUTO_INCREMENT PRIMARY KEY,
    AttitudeName VARCHAR(255) NOT NULL
);

CREATE TABLE BranchingStyle (
    BranchingStyleID INT AUTO_INCREMENT PRIMARY KEY,
    BranchingStyleName VARCHAR(255) NOT NULL
);

CREATE TABLE AspectRatio (
    AspectRatioID INT AUTO_INCREMENT PRIMARY KEY,
    AspectRatioName VARCHAR(255) NOT NULL
);

CREATE TABLE GrowthVariability (
    GrowthVariabilityID INT AUTO_INCREMENT PRIMARY KEY,
    GrowthVariabilityName VARCHAR(255) NOT NULL
);

CREATE TABLE BranchingMode (
    BranchingModeID INT AUTO_INCREMENT PRIMARY KEY,
    BranchingModeName VARCHAR(255) NOT NULL
);

CREATE TABLE BranchingAngle (
    BranchingAngleID INT AUTO_INCREMENT PRIMARY KEY,
    BranchingAngleName VARCHAR(255) NOT NULL
);

CREATE TABLE MacroStructureTypes (
    MacroStructureTypesID INT AUTO_INCREMENT PRIMARY KEY,
    MacroStructureName VARCHAR(255) NOT NULL,
    FormDescription TEXT
    
);

CREATE TABLE MacroStructureProperties (
    MacrostructureID INT PRIMARY KEY,
    MegaStructureTypeID INT,
    SectionHeight DECIMAL,
    Comments TEXT,
    MegastructureShapeID INT,
    MegaStructureSizeID INT,
    SubstrateID INT,
    InitiationID INT,
    PlanViewID INT,
    LinkageID INT,
    SpacingID INT,
    ShapeID INT,
    ShapeLayeringID INT,
    ShapeDomeID INT,
    ConicalShapeID INT, 
    AspectRatioID INT,
    GrowthVariabilityID INT,
    AttitudeID INT,
    BranchingStyleID INT,
    BranchingModeID INT,
    BranchingAngleID INT,
    ColumnShapeID INT,
    MacrostructureTypesID INT,
    FOREIGN KEY (MacrostructureID) REFERENCES MacroStructure(MacrostructureID) ON DELETE CASCADE,
    FOREIGN KEY (MegaStructureTypeID) REFERENCES MegaStructureType(TypeID) ON DELETE SET NULL,
    FOREIGN KEY (MegastructureShapeID) REFERENCES MegastructureShape(ShapeID) ON DELETE SET NULL,
    FOREIGN KEY (MegaStructureSizeID) REFERENCES MegaStructureSize(SizeID) ON DELETE SET NULL,
    FOREIGN KEY (SubstrateID) REFERENCES Substrate(SubstrateID) ON DELETE SET NULL,
    FOREIGN KEY (InitiationID) REFERENCES Initiation(InitiationID) ON DELETE SET NULL,
    FOREIGN KEY (PlanViewID) REFERENCES PlanView(PlanViewID) ON DELETE SET NULL,
    FOREIGN KEY (LinkageID) REFERENCES Linkage(LinkageID) ON DELETE SET NULL,
    FOREIGN KEY (SpacingID) REFERENCES Spacing(SpacingID) ON DELETE SET NULL,
    FOREIGN KEY (ShapeID) REFERENCES Shape(ShapeID) ON DELETE SET NULL,
    FOREIGN KEY (ShapeLayeringID) REFERENCES ShapeLayering(ShapeLayeringID) ON DELETE SET NULL,
    FOREIGN KEY (ShapeDomeID) REFERENCES ShapeDome(ShapeDomeID) ON DELETE SET NULL,
    FOREIGN KEY (ConicalShapeID) REFERENCES ConicalShape(ConicalShapeID) ON DELETE SET NULL,
    FOREIGN KEY (AspectRatioID) REFERENCES AspectRatio(AspectRatioID) ON DELETE SET NULL,
    FOREIGN KEY (GrowthVariabilityID) REFERENCES GrowthVariability(GrowthVariabilityID) ON DELETE SET NULL,
    FOREIGN KEY (AttitudeID) REFERENCES Attitude(AttitudeID) ON DELETE SET NULL,
    FOREIGN KEY (BranchingStyleID) REFERENCES BranchingStyle(BranchingStyleID) ON DELETE SET NULL,
    FOREIGN KEY (BranchingModeID) REFERENCES BranchingMode(BranchingModeID) ON DELETE SET NULL,
    FOREIGN KEY (BranchingAngleID) REFERENCES BranchingAngle(BranchingAngleID) ON DELETE SET NULL,
    FOREIGN KEY (ColumnShapeID) REFERENCES ColumnShape(ColumnShapeID) ON DELETE SET NULL,
    FOREIGN KEY (MacrostructureTypesID) REFERENCES MacroStructureTypes(MacrostructureTypesID) ON DELETE SET NULL
);



-- Mesostructure
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



--Photos
ALTER TABLE mesostructurephotos 
CHANGE RefrenceLink ReferenceLink VARCHAR(255) ;

CREATE TABLE Photos (
    PhotoID INT PRIMARY KEY AUTO_INCREMENT,
    PhotoLinkName VARCHAR(255) NOT NULL
);



--Thin Structure
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
    ClasticGrainsID INT PRIMARY KEY,
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



--Users
USE microbialites;

CREATE TABLE User (
    UserID INT PRIMARY KEY,
    LogInID VARCHAR(255) UNIQUE,
    HashedPassword VARCHAR(255) NOT NULL,
    RoleID INT,
    FOREIGN KEY (RoleID) REFERENCES UserRole(RoleID)
);

CREATE TABLE UserInteractions (
    InteractionID INT PRIMARY KEY,
    UserID INT NOT NULL,
    InteractionTimeStamp DATETIME NOT NULL,
    SubEntityType VARCHAR(255),
    SubEntityID INT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (SubEntityID) REFERENCES Waypoint(SubEntityID)
);

CREATE TABLE CustomerSupport (
    TicketID INT PRIMARY KEY,
    UserID INT NOT NULL,
    AssignedToUserID INT,
    Description TEXT,
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (AssignedToUserID) REFERENCES User(UserID)
);

CREATE TABLE UserRole (
    UserID INT,
    RoleID INT,
    Description TEXT,
    DateAssigned DATE,
    PRIMARY KEY (UserID, RoleID),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (RoleID) REFERENCES Role(RoleID)
);

CREATE TABLE Role (
    RoleID INT PRIMARY KEY,
    RoleName VARCHAR(255) NOT NULL,
    RoleDescription TEXT
);

CREATE TABLE RolePermissions (
    RoleID INT,
    PermissionsID INT,
    Description TEXT,
    PRIMARY KEY (RoleID, PermissionsID),
    FOREIGN KEY (RoleID) REFERENCES Role(RoleID),
    FOREIGN KEY (PermissionsID) REFERENCES Permissions(PermissionID)
);

CREATE TABLE Permissions (
    PermissionID INT PRIMARY KEY,
    PermissionName VARCHAR(255) NOT NULL,
    PermissionDescription TEXT
);



--Waypoint
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


