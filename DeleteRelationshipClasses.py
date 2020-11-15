# ---------------------------------------------------------------------------
# DeleteRelationshipClasses.py
# Created on: 2020-11-02
# Description: Created by PetarSimic
# ---------------------------------------------------------------------------

import arcpy

Feature_Dataset = arcpy.GetParameterAsText(0)

for fc in arcpy.Describe(Feature_Dataset).children:
    if fc.datatype == "RelationshipClass":
         arcpy.Delete_management(fc.catalogPath)
         arcpy.AddMessage("Relationship class: " + fc.name + " deleted")