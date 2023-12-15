--ClasticGrainTypesSorted
SELECT
    ClasticGrainsID,
    ClasticGrainType
FROM
    ClasticGrains
ORDER BY
    ClasticGrainsID;


--ImageReport
SELECT
    mst.MesoStructure,
    tt.MesoStructureTextureType,
    ms.MesoStructureID,
    p.PhotoLinkName
FROM 
    MesoStructure ms
LEFT JOIN 
    MesoStructurePhotos msp ON ms.MesoStructureID = msp.MesoStructureID
RIGHT JOIN 
    Photos p ON msp.PhotoID = p.PhotoID
LEFT JOIN 
    TextureType tt ON ms.MesoStructureID = tt.TextureTypeID
RIGHT JOIN
    MesoStructureType mst ON ms.MesoStructureID = mst.MesoStructureTypeID
ORDER BY
    ms.MesoStructureID;

--MacroStructureDataSorted
SELECT
    MS.MacrostructureID,
    MS.WayptID,  -- Getting WayptID from MacroStructure table
    MST.MacroStructureName,
    MSP.SectionHeight,
    MSP.Comments
FROM
    MacroStructureProperties MSP
    JOIN MacroStructureTypes MST ON MSP.MacrostructureTypesID = MST.MacroStructureTypesID
    JOIN MacroStructure MS ON MSP.MacrostructureID = MS.MacrostructureID  -- Added JOIN for MacroStructure

ORDER BY
    MS.WayptID;

--MacroStructurePhotosSorted
SELECT
    msp.PhotoID,
    p.PhotoLinkName,
    msp.MacroStructureID,
    msp.OutcropPhoto,
    msp.Photomicrograph,
    msp.CLImage,
    msp.OtherImage,
    msp.OtherDocument
FROM
    MacroStructurePhotos msp
JOIN
    Photos p ON msp.PhotoID = p.PhotoID
ORDER BY
    msp.MacroStructureID;

--MacroStructureTypesSorted
SELECT
    MacroStructureTypesID,
    MacroStructureName,
    FormDescription
FROM
    MacroStructureTypes
ORDER BY
    MacroStructureTypesID;

--MakeAMesoStructureReport
SELECT
    t.MesoStructureTextureType,
    msp.MesoStructureID,
    msp.ThinSectionMade,
    msph.InReport,  -- from MesoStructurePhotos
    msp.FieldDescription,
    msp.RockDescription,
    msp.MacroStructureID,
    msp.LaminaThickness,
    msr.SynopticRelief, -- from MesoSynopticRelief
    msp.Wavelength,
    msp.AmplitudeOrHeight,
    gt.GrainType, -- from MesoGrainType
    msph.OutcropPhoto, -- from MesoStructurePhotos
    p.PhotoLinkName, -- from MesoStructurePhotos
    OtherImage -- from MesoStructurePhotos
FROM 
    MesoStructureProperties msp
LEFT JOIN MesoStructureTextureTypes mstt ON msp.MesoStructureID = mstt.MesoStructureID
LEFT JOIN TextureType t ON mstt.TextureTypeID = t.TextureTypeID
LEFT JOIN MesoGrainType gt ON msp.GrainTypeID = gt.GrainTypeID
LEFT JOIN MesoSynopticRelief msr ON msp.MesoSynopticReliefID = msr.MesoSynopticReliefID
LEFT JOIN MesoStructurePhotos msph ON msp.MesoStructureID = msph.MesoStructureID
LEFT JOIN Photos p ON msph.PhotoID = p.PhotoID
ORDER BY
    msp.MesoStructureTypeID;

--MesoStructureDataSorted
SELECT
    p.PhotoID,
    msph.MesoStructureID,
    msp.ThinSectionMade,
    tsp.PriorityType, -- from ThinSectionPriority
    mst.Mesostructure, -- from MesoStructureType
    tt.MesoStructureTextureType, -- from TextureType
    msp.MacroStructureID,
    msp.SampleSize,
    msp.FieldDescription,
    msp.RockDescription,
    mgt.GrainType, -- from MesoGrainType
    msp.LaminaThickness,
    msr.SynopticRelief, -- from MesoSynopticRelief
    msp.Wavelength,
    msp.AmplitudeOrHeight
FROM 
    MesoStructurePhotos msph
RIGHT JOIN Photos p ON msph.PhotoID = p.PhotoID
RIGHT OUTER JOIN MesoStructureProperties msp ON msp.MesoStructureID = msp.MesoStructureID
RIGHT OUTER JOIN MesoStructureType mst ON msp.MesoStructureTypeID = mst.MesoStructureTypeID
RIGHT OUTER JOIN MesoStructureTextureTypes mstt ON msp.MesoStructureID = mstt.MesoStructureID
RIGHT OUTER JOIN TextureType tt ON mstt.TextureTypeID = tt.TextureTypeID
RIGHT OUTER JOIN MesoGrainType mgt ON msp.GrainTypeID = mgt.GrainTypeID
LEFT OUTER JOIN MesoSynopticRelief msr ON msp.MesoSynopticReliefID = msr.MesoSynopticReliefID
RIGHT OUTER JOIN ThinSectionPriority tsp ON msp.ThinSectionPriorityID = tsp.ThinSectionPriorityID
ORDER BY
    msp.MesoStructureID;

--MesoStructurePhotosWithThinSections
SELECT
    ms.MesoStructureID,
    mst.Mesostructure, -- from MesoStructureType
    msp.ThinSectionMade,
    p.PhotoLinkName, -- from Photos
    c.Northing, -- from Coordinates
    c.Easting, -- from Coordinates
    tt.MesoStructureTextureType -- from TextureType
FROM 
    MesoStructure ms
JOIN MesoStructureProperties msp ON ms.MesoStructureID = msp.MesoStructureID
JOIN MesoStructureType mst ON msp.MesoStructureTypeID = mst.MesoStructureTypeID
JOIN MesoStructureTextureTypes mstt ON ms.MesoStructureID = mstt.MesoStructureID
JOIN TextureType tt ON mstt.TextureTypeID = tt.TextureTypeID
JOIN MesoStructurePhotos msph ON ms.MesoStructureID = msp.MesoStructureID
JOIN Photos p ON msph.PhotoID = p.PhotoID
JOIN Coordinates c ON ms.WayptID = c.WayptID
ORDER BY
    msp.MesoStructureTypeID;

--MesoStructureTexturesSorted
SELECT
    TextureTypeID,
    MesoStructureTextureType
FROM
    TextureType
ORDER BY
    TextureTypeID;

--MesoStructureTypesSorted
SELECT
    MesoStructureTypeID,
    MesoStructure
FROM
    MesoStructureType
ORDER BY
    MesoStructureTypeID;

--PhotoLinksDataSorted
SELECT
    ms.MesoStructureID,
    ms.MacroStructureID,
    ms.WayptID,
    msph.InReport,  -- from MesoStructurePhotos
    p.PhotoLinkName, -- from Photos
    msph.OutcropPhoto, -- from MesoStructurePhotos
    msph.Photomicrograph, -- from MesoStructurePhotos
    msph.CLImage, -- from MesoStructurePhotos
    msph.OtherDocument, -- from MesoStructurePhotos
    msph.PhotoID,
    msp.ThinSectionMade -- from MesoStructureProperties
FROM
    MesoStructure ms
JOIN MesoStructurePhotos msph ON ms.MesoStructureID = msph.MesoStructureID
JOIN Photos p ON msph.PhotoID = p.PhotoID
JOIN MesoStructureProperties msp ON ms.MesoStructureID = msp.MesoStructureID
ORDER BY
    msp.MesoStructureTypeID;

--PhotosBySampleID
SELECT
    ms.MesoStructureID,
    p.PhotoLinkName,
    mst.MesoStructureTypeID
FROM 
    MesoStructure ms
JOIN 
    MesoStructurePhotos msp ON ms.MesoStructureID = msp.MesoStructureID
JOIN 
    Photos p ON msp.PhotoID = p.PhotoID
JOIN 
    MesoStructureTextureTypes mstt ON ms.MesoStructureID = mstt.MesoStructureID
RIGHT JOIN
    TextureType tt ON mstt.TextureTypeID = tt.TextureTypeID
LEFT JOIN
    MesoStructureType mst ON tt.TextureTypeID = mst.MesoStructureTypeID
ORDER BY
    mst.MesoStructureTypeID;

--PhotosBtSampleIDWithThinSections
SELECT
    ms.MesoStructureID,
    p.PhotoLinkName, -- from Photos
    msp.ThinSectionMade, -- from MesoStructureProperties
    mst.Mesostructure, -- from MesoStructureType
    msp.AnalysisPriority -- from MesoStructureProperties
FROM 
    MesoStructure ms
JOIN MesoStructurePhotos msph ON ms.MesoStructureID = msph.MesoStructureID
JOIN Photos p ON msph.PhotoID = p.PhotoID
JOIN MesoStructureProperties msp ON ms.MesoStructureID = msp.MesoStructureID
JOIN MesoStructureType mst ON msp.MesoStructureTypeID = mst.MesoStructureTypeID
ORDER BY
    msp.MesoStructureTypeID;

--PriorityListForAnalysis
SELECT
    ms.MesoStructureID,
    msp.ThinSectionMade, -- from MesoStructureProperties
    tsp.PriorityType -- from ThinSectionPriority
FROM 
    MesoStructure ms
JOIN MesoStructureProperties msp ON ms.MesoStructureID = msp.MesoStructureID
JOIN ThinSectionPriority tsp ON msp.ThinSectionPriorityID = tsp.ThinSectionPriorityID
ORDER BY
    ms.MesoStructureID;

--ThinSectionPhotosSorted
SELECT
    ms.MesoStructureID,
    p.PhotoLinkName, -- from Photos
    msph.OutcropPhoto, -- from MesoStructurePhotos
    msph.Photomicrograph, -- from MesoStructurePhotos
    msph.CLImage, -- from MesoStructurePhotos
    msph.OtherDocument -- from MesoStructurePhotos
FROM
    MesoStructure ms
JOIN MesoStructurePhotos msph ON ms.MesoStructureID = msph.MesoStructureID
JOIN Photos p ON msph.PhotoID = p.PhotoID
ORDER BY
    ms.MesoStructureID;

--WaypointDataSorted
SELECT
    WayptID,
    DateCollected,
    WayptName,
    ProjectName,
    SiteOrLocationName,
    Formation,
    Fieldbook,
    FieldbookPage,
    MeasuredSection,
    SectionName,
    Comments,
    Latitude,
    Longitude,
    Elevation,
    UTMZone1,
    UTMZone2,
    Datum,
    Projection
FROM
    Waypoint
ORDER BY
    DateCollected DESC;