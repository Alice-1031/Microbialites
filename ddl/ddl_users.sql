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
