CREATE DATABASE microbialites;

CREATE TABLE Test;

--User Interface
CREATE TABLE User (
    UserID INT PRIMARY KEY,
    LogInID VARCHAR(255) UNIQUE,
    HashedPassword VARCHAR(255),
    RoleID INT,
    FOREIGN KEY (RoleID) REFERENCES UserRole(RoleID)
);

CREATE TABLE UserInteractions (
    InteractionID INT PRIMARY KEY,
    UserID INT,
    InteractionTimeStamp DATETIME,
    SubEntityType VARCHAR(255),
    SubEntityID INT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (SubEntityID) REFERENCES Waypoint(SubEntityID)
);

CREATE TABLE CustomerSupport (
    TicketID INT PRIMARY KEY,
    UserID INT,
    AssignedToUserID INT,
    Description TEXT,
    Status VARCHAR(50),
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
    RoleName VARCHAR(255),
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
    PermissionName VARCHAR(255),
    PermissionDescription TEXT
);

--MacroStructure
CREATE TABLE MacroStructure (
    MacrostructureID INT PRIMARY KEY,
    WayptID INT,
    FOREIGN KEY (WayptID) REFERENCES Waypoint(WayptID)
);

CREATE TABLE MacroStructurePhotos (
    MacroStructureID INT,
    PhotoID INT,
    WaypointID INT,
    InReport BOOLEAN,
    OutcropPhoto BOOLEAN,
    Photomicrograph BOOLEAN,
    OtherImage BOOLEAN,
    CLImage BOOLEAN,
    OtherDocument BOOLEAN,
    ReferenceLink VARCHAR(255),
    PRIMARY KEY (MacroStructureID, PhotoID),
    FOREIGN KEY (MacroStructureID) REFERENCES MacroStructure(MacrostructureID),
    FOREIGN KEY (WaypointID) REFERENCES Waypoint(WayptID)
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
    FOREIGN KEY (MacrostructureID) REFERENCES MacroStructure(MacrostructureID),
    FOREIGN KEY (MegaStructureTypeID) REFERENCES MegaStructureType(TypeID),
    FOREIGN KEY (MegastructureShapeID) REFERENCES MegastructureShape(ShapeID),
    FOREIGN KEY (MegaStructureSizeID) REFERENCES MegaStructureSize(SizeID),
    FOREIGN KEY (SubstrateID) REFERENCES Substrate(SubstrateID),
    FOREIGN KEY (InitiationID) REFERENCES Initiation(InitiationID),
    FOREIGN KEY (PlanViewID) REFERENCES PlanView(PlanViewID),
    FOREIGN KEY (LinkageID) REFERENCES Linkage(LinkageID),
    FOREIGN KEY (SpacingID) REFERENCES Spacing(SpacingID),
    FOREIGN KEY (ShapeID) REFERENCES Shape(ShapeID),
    FOREIGN KEY (ShapeLayeringID) REFERENCES ShapeLayering(ShapeLayeringID),
    FOREIGN KEY (ShapeDomeID) REFERENCES ShapeDome(ShapeDomeID),
    FOREIGN KEY (ConicalShapeID) REFERENCES ConicalShape(ConicalShapeID),
    FOREIGN KEY (AspectRatioID) REFERENCES AspectRatio(AspectRatioID),
    FOREIGN KEY (GrowthVariabilityID) REFERENCES GrowthVariability(GrowthVariabilityID),
    FOREIGN KEY (AttitudeID) REFERENCES Attitude(AttitudeID),
    FOREIGN KEY (BranchingStyleID) REFERENCES BranchingStyle(BranchingStyleID),
    FOREIGN KEY (BranchingModeID) REFERENCES BranchingMode(BranchingModeID),
    FOREIGN KEY (BranchingAngleID) REFERENCES BranchingAngle(BranchingAngleID),
    FOREIGN KEY (ColumnShapeID) REFERENCES ColumnShape(ColumnShapeID),
    FOREIGN KEY (MacrostructureTypesID) REFERENCES MacroStructureTypes(MacrostructureTypesID)
);

CREATE TABLE MegaStructureType (
    TypeID INT PRIMARY KEY,
    Type VARCHAR(255)
);

CREATE TABLE MegastructureShape (
    ShapeID INT PRIMARY KEY,
    Shape VARCHAR(255)
);

CREATE TABLE MegaStructureSize (
    SizeID INT PRIMARY KEY,
    Size VARCHAR(255)
);

CREATE TABLE Substrate (
    SubstrateID INT PRIMARY KEY,
    SubstrateName VARCHAR(255)
);

CREATE TABLE PlanView (
    PlanViewID INT PRIMARY KEY,
    PlanViewName VARCHAR(255)
);

CREATE TABLE Linkage (
    LinkageID INT PRIMARY KEY,
    LinkageName VARCHAR(255)
);

CREATE TABLE Initiation (
    InitiationID INT PRIMARY KEY,
    InitiationName VARCHAR(255)
);

CREATE TABLE Spacing (
    SpacingID INT PRIMARY KEY,
    SpacingName VARCHAR(255)
);

CREATE TABLE Shape (
    ShapeID INT PRIMARY KEY,
    ShapeName VARCHAR(255)
);

CREATE TABLE ShapeLayering (
    ShapeLayeringID INT PRIMARY KEY,
    ShapeLayeringName VARCHAR(255)
);

CREATE TABLE ColumnShape (
    ColumnShapeID INT PRIMARY KEY,
    ColumnShapeName VARCHAR(255)
);

CREATE TABLE ShapeDome (
    ShapeDomeID INT PRIMARY KEY,
    ShapeDomeName VARCHAR(255)
);

CREATE TABLE ConicalShape (
    ConicalShapeID INT PRIMARY KEY,
    ConicalShapeName VARCHAR(255)
);

CREATE TABLE Attitude (
    AttitudeID INT PRIMARY KEY,
    AttitudeName VARCHAR(255)
);

CREATE TABLE BranchingStyle (
    BranchingStyleID INT PRIMARY KEY,
    BranchingStyleName VARCHAR(255)
);

CREATE TABLE AspectRatio (
    AspectRatioID INT PRIMARY KEY,
    AspectRatioName VARCHAR(255)
);

CREATE TABLE GrowthVariability (
    GrowthVariabilityID INT PRIMARY KEY,
    GrowthVariabilityName VARCHAR(255)
);

CREATE TABLE BranchingMode (
    BranchingModeID INT PRIMARY KEY,
    BranchingModeName VARCHAR(255)
);

CREATE TABLE BranchingAngle (
    BranchingAngleID INT PRIMARY KEY,
    BranchingAngleName VARCHAR(255)
);

CREATE TABLE MacroStructureTypes (
    MacroStructureTypesID INT PRIMARY KEY,
    MacroStructureName VARCHAR(255),
    FormDescription TEXT
);




-- ThinStructures Table
CREATE TABLE ThinStructures (
    ThinStructureID INT PRIMARY KEY,
    WaypointID INT,
    MacroStructureID INT,
    MesoStructureID INT,
    FOREIGN KEY (WaypointID) REFERENCES Waypoints(WaypointID),
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

