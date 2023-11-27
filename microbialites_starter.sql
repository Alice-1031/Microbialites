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
