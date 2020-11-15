# ---------------------------------------------------------------------------
# ImportRelationshipClasses.py
# Created on: 2020-11-02
# Description: Created by PetarSimic
# ---------------------------------------------------------------------------

import arcpy

Feature_Dataset = arcpy.GetParameterAsText(0)
location_of_table = arcpy.GetParameterAsText(1)

arcpy.env.workspace = Feature_Dataset

# Creating Relationship Classes
cursor = arcpy.SearchCursor(location_of_table)

for row in cursor:
    arcpy.CreateRelationshipClass_management(row.getValue("origin"), row.getValue("destina"), row.getValue("out_rc"), row.getValue("r_type"), row.getValue("forw_label"), row.getValue("back_label"), row.getValue("msg_dir"), row.getValue("cardin"), row.getValue("attrib"), row.getValue("prim_key"), row.getValue("fore_key"), "", "")