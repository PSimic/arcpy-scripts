# ---------------------------------------------------------------------------
# ExportRelationshipClasses.py
# Created on: 2020-11-02
# Description: Created by PetarSimic
# ---------------------------------------------------------------------------

import arcpy

Feature_Dataset = arcpy.GetParameterAsText(0)
location_of_table = arcpy.GetParameterAsText(1)

# Check for exiting relationship classes
rc_list = [c.name for c in arcpy.Describe(Feature_Dataset).children if c.datatype == "RelationshipClass"]
if len(rc_list) == 0:
    arcpy.AddMessage("There is no relationship classes in " + arcpy.Describe(Feature_Dataset).name +  " feature dataset.")
    sys.exit(0)

# Creating table 
table_name = arcpy.Describe(Feature_Dataset).name + ".dbf"

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

for fc in arcpy.Describe(Feature_Dataset).children:
    if fc.datatype == "RelationshipClass":
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