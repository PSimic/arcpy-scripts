# ---------------------------------------------------------------------------
# DeleteAttrSrcRelationshipClasses.py
# Created on: 2021-01-19
# Description: Created by PetarSimic
# ---------------------------------------------------------------------------

import arcpy

geodatabase = arcpy.GetParameterAsText(0) # Choose database in witch you want to delete relationships classes

for fc in arcpy.Describe(geodatabase).children:
    if fc.datatype == "RelationshipClass":
        type_of_relationship = fc.name.split("_")[-1]
        if type_of_relationship == "AttrSrcRC" or type_of_relationship == "AttrSrcRT" or type_of_relationship == "AttributeSource":
            arcpy.Delete_management(fc.catalogPath)
            arcpy.AddMessage("Relationship class: " + fc.name + " deleted")