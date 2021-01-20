# ---------------------------------------------------------------------------
# ImportAttrSrcRelationshipClasses.py
# Created on: 2021-01-19
# Description: Created by PetarSimic
# ---------------------------------------------------------------------------

import arcpy

geodatabase = arcpy.GetParameterAsText(0) #Choose database in witch you want to import relationships classes
location_of_table = arcpy.GetParameterAsText(1) #Choose location where .dbf table is stored

arcpy.env.workspace = geodatabase

# Creating Relationship Classes
cursor = arcpy.SearchCursor(location_of_table)

for row in cursor:
    try:
        arcpy.CreateRelationshipClass_management(row.getValue("origin"), row.getValue("destina"), row.getValue("out_rc"), row.getValue("r_type"), row.getValue("forw_label"), row.getValue("back_label"), row.getValue("msg_dir"), row.getValue("cardin"), row.getValue("attrib"), row.getValue("prim_key"), row.getValue("fore_key"), "", "")
        arcpy.AddMessage(row.getValue("out_rc") + " imported")
    except arcpy.ExecuteError:
        arcpy.AddError(row.getValue("out_rc") + " is not imported and the reason is:") 
        arcpy.AddError(arcpy.GetMessages(2))
        