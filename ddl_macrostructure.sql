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

