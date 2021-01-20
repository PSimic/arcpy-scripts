# ---------------------------------------------------------------------------
# ExportAttrSrcRelationshipClasses.py
# Created on: 2021-01-19
# Description: Created by PetarSimic
# ---------------------------------------------------------------------------

import arcpy

geodatabase = arcpy.GetParameterAsText(0) #Choose database from witch you want to export relationships classes
location_of_table = arcpy.GetParameterAsText(1) #Choose folder location where you want to save table with all information from relationships
table_name = arcpy.GetParameterAsText(2) + ".dbf" #In this field put name of table 

# Creating table 
arcpy.CreateTable_management(location_of_table, table_name)
arcpy.env.workspace = location_of_table

arcpy.AddField_management(table_name,"origin","TEXT",30)
arcpy.AddField_management(table_name,"destina","TEXT",30)
arcpy.AddField_management(table_name,"out_rc","TEXT",30)
arcpy.AddField_management(table_name,"r_type","TEXT",30)
arcpy.AddField_management(table_name,"forw_label","TEXT",30)
arcpy.AddField_management(table_name,"back_label","TEXT",30)
arcpy.AddField_management(table_name,"msg_dir","TEXT",30)
arcpy.AddField_management(table_name,"cardin","TEXT",30)
arcpy.AddField_management(table_name,"attrib","TEXT",30)
arcpy.AddField_management(table_name,"prim_key","TEXT",30)
arcpy.AddField_management(table_name,"fore_key","TEXT",30)
arcpy.DeleteField_management(table_name, "Field1")

# Populating table
rows = arcpy.InsertCursor(table_name)

for fc in arcpy.Describe(geodatabase).children:
    if fc.datatype == "RelationshipClass":
        type_of_relationship = fc.name.split("_")[-1]
        if type_of_relationship == "AttrSrcRC" or type_of_relationship == "AttrSrcRT" or type_of_relationship == "AttributeSource":
            row = rows.newRow()

            row.setValue("origin", fc.originClassNames[0])
            row.setValue("destina", fc.destinationClassNames[0])
            row.setValue("out_rc", fc.name)

            if fc.isComposite is True:
                row.setValue("r_type", "COMPOSITE")
            else:
                row.setValue("r_type", "SIMPLE")
            
            row.setValue("forw_label", fc.forwardPathLabel)
            row.setValue("back_label", fc.backwardPathLabel)

            row.setValue("msg_dir", str(fc.notification).upper())

            if (fc.cardinality == "OneToOne"):
                row.setValue("cardin", "ONE_TO_ONE")
            elif (fc.cardinality == "OneToMany"):
                row.setValue("cardin", "ONE_TO_MANY")
            else:
                row.setValue("cardin", "MANY_TO_MANY")

            if fc.isAttributed is True:
                row.setValue("attrib", "ATTRIBUTED")
            else:
                row.setValue("attrib", "NONE")
        
            row.setValue("prim_key", fc.originClassKeys[0][0])
            row.setValue("fore_key", fc.originClassKeys[1][0])

            rows.insertRow(row)
            del row

del rows