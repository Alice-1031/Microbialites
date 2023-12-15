USE microbialites;

ALTER TABLE mesostructurephotos 
CHANGE RefrenceLink ReferenceLink VARCHAR(255) ;

CREATE TABLE Photos (
    PhotoID INT PRIMARY KEY AUTO_INCREMENT,
    PhotoLinkName VARCHAR(255) NOT NULL
);