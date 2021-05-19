import arcpy

ProjectCode = arcpy.GetParameterAsText(0)
ProjectStatus = arcpy.GetParameterAsText(1)
DataInputFormat = arcpy.GetParameterAsText(2)
DataInputMethod = arcpy.GetParameterAsText(3)
Owner = arcpy.GetParameterAsText(4)
DateCreated = arcpy.GetParameterAsText(5)
EditedBy = arcpy.GetParameterAsText(6)
FeatureLevel = arcpy.GetParameterAsText(7)
Agency = arcpy.GetParameterAsText(8)

FeatureClass = arcpy.GetParameterAsText(9)
FieldNames = [field.name for field in arcpy.ListFields(FeatureClass)]

if "PROJECT_CODE" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["PROJECT_CODE"]) as cursor:
        for row in cursor:
            row[0]=ProjectCode
            cursor.updateRow(row)
else:
    arcpy.AddError("PROJECT_CODE attribute does not exist.")

if "PROJECT_STATUS" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["PROJECT_STATUS"]) as cursor:
        for row in cursor:
            row[0]=ProjectStatus
            cursor.updateRow(row)
else:
    arcpy.AddError("PROJECT_STATUS attribute does not exist.")

if "SOURCE_DATA_INPUT_FORMAT" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["SOURCE_DATA_INPUT_FORMAT"]) as cursor:
        for row in cursor:
            row[0]=DataInputFormat
            cursor.updateRow(row)
else:
    arcpy.AddError("SOURCE_DATA_INPUT_FORMAT attribute does not exist.")
   
if "DATA_INPUT_METHOD" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["DATA_INPUT_METHOD"]) as cursor:
        for row in cursor:
            row[0]=DataInputMethod
            cursor.updateRow(row)
else:
    arcpy.AddError("DATA_INPUT_METHOD attribute does not exist.")

if "OWNER" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["OWNER"]) as cursor:
        for row in cursor:
            row[0]=Owner
            cursor.updateRow(row)
else:
    arcpy.AddError("OWNER attribute does not exist.")

if "DATE_CREATED" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["DATE_CREATED"]) as cursor:
        for row in cursor:
            row[0]=DateCreated
            cursor.updateRow(row)
else:
    arcpy.AddError("DATE_CREATED attribute does not exist.")

if "EDITED_BY" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["EDITED_BY"]) as cursor:
        for row in cursor:
            row[0]=EditedBy
            cursor.updateRow(row)
else:
    arcpy.AddError("EDITED_BY attribute does not exist.")

if "FEATURE_LEVEL" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["FEATURE_LEVEL"]) as cursor:
        for row in cursor:
            row[0]=FeatureLevel
            cursor.updateRow(row)
else:
    arcpy.AddError("FEATURE_LEVEL attribute does not exist.")

if "AGENCY_NAME" in FieldNames:
    with arcpy.da.UpdateCursor(FeatureClass,["AGENCY_NAME"]) as cursor:
        for row in cursor:
            row[0]=Agency
            cursor.updateRow(row)
else:
    arcpy.AddError("AGENCY_NAME attribute does not exist.")