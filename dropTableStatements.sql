-- Drop the tables in reverse order to avoid foreign key constraints

-- Drop ThinStructures
DROP TABLE IF EXISTS ThinStructureClasticGrains;
DROP TABLE IF EXISTS ThinStructureMineralogyTypes;
DROP TABLE IF EXISTS ThinStructureCementTypes;
DROP TABLE IF EXISTS ThinStructurePorosityType;
DROP TABLE IF EXISTS ThinStructureTextureTypes;
DROP TABLE IF EXISTS ThinStructurePhotos;
DROP TABLE IF EXISTS ThinStructureProperties;
DROP TABLE IF EXISTS ThinStructure;

-- Drop MesoStructures
DROP TABLE IF EXISTS MesoStructureClasticGrains;
DROP TABLE IF EXISTS MesoStructureMineralogies;
DROP TABLE IF EXISTS MesoStructureCements;
DROP TABLE IF EXISTS MesoStructureGrains;
DROP TABLE IF EXISTS MesoStructurePorosityTypes;
DROP TABLE IF EXISTS MesoStructureTextureTypes;
DROP TABLE IF EXISTS MesoStructurePhotos;
DROP TABLE IF EXISTS MesoStructureProperties;
DROP TABLE IF EXISTS MesoStructure;

-- Drop MacroStructures
DROP TABLE IF EXISTS MacroStructureProperties;
DROP TABLE IF EXISTS MacroStructurePhotos;
DROP TABLE IF EXISTS MacroStructure;

-- Drop User Interface
DROP TABLE IF EXISTS UserRoles;
DROP TABLE IF EXISTS UserRole;
DROP TABLE IF EXISTS UserInteractions;
DROP TABLE IF EXISTS User;

-- Drop Photos
DROP TABLE IF EXISTS Photos;

-- Drop Waypoint
DROP TABLE IF EXISTS Coordinates;
DROP TABLE IF EXISTS Waypoint;

-- Drop Lookup Tables
DROP TABLE IF EXISTS MesoClotShape;
DROP TABLE IF EXISTS MesoClotTypes;
DROP TABLE IF EXISTS MesoStructureLaminaShape;
DROP TABLE IF EXISTS MesoMacroLaminae;
DROP TABLE IF EXISTS MesoWalls;
DROP TABLE IF EXISTS MesoLateralContinuity;
DROP TABLE IF EXISTS MesoLaminaInheritance;
DROP TABLE IF EXISTS MesoSynopticRelief;
DROP TABLE IF EXISTS MesoLaminaProfile;
DROP TABLE IF EXISTS MesoModalitySkewness;
DROP TABLE IF EXISTS MesoWaviness;
DROP TABLE IF EXISTS MesoAlternation;
DROP TABLE IF EXISTS MesoStackingOverlap;
DROP TABLE IF EXISTS MesoStructureLaminaPattern;
DROP TABLE IF EXISTS MesoStructureLamina;
DROP TABLE IF EXISTS MesoStructureType;
DROP TABLE IF EXISTS MesoInheritance;
DROP TABLE IF EXISTS ThinTextureTypes;
DROP TABLE IF EXISTS TextureTypes;
DROP TABLE IF EXISTS CementTypes;
DROP TABLE IF EXISTS ClasticGrains;
DROP TABLE IF EXISTS PorosityType;
DROP TABLE IF EXISTS MineralogyTypes;
DROP TABLE IF EXISTS MegaStructureSize;
DROP TABLE IF EXISTS MegaStructureShape;
DROP TABLE IF EXISTS MegaStructureType;
DROP TABLE IF EXISTS MacroStructureTypes;
DROP TABLE IF EXISTS BranchingAngle;
DROP TABLE IF EXISTS BranchingMode;
DROP TABLE IF EXISTS BranchingStyle;
DROP TABLE IF EXISTS Attitude;
DROP TABLE IF EXISTS ConicalShape;
DROP TABLE IF EXISTS ShapeDome;
DROP TABLE IF EXISTS ShapeLayering;
DROP TABLE IF EXISTS Shape;
DROP TABLE IF EXISTS Spacing;
DROP TABLE IF EXISTS Initiation;
DROP TABLE IF EXISTS Linkage;
DROP TABLE IF EXISTS PlanView;
DROP TABLE IF EXISTS Substrate;
DROP TABLE IF EXISTS GrowthVariability;

-- Drop Customer Support
DROP TABLE IF EXISTS CustomerSupport;

-- Drop Roles and Permissions
DROP TABLE IF EXISTS RolePermissions;
DROP TABLE IF EXISTS Permissions;
DROP TABLE IF EXISTS Role;

-- Drop the database if needed
-- DROP DATABASE IF EXISTS YourDatabaseName;