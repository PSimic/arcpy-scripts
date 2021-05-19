import arcpy

feature_class = arcpy.GetParameterAsText(0)
attribute = arcpy.GetParameterAsText(1)

arcpy.env.workspace = feature_class
arcpy.AddField_management(feature_class,"unique","TEXT","","",5)

unique_list = []

cursor = arcpy.UpdateCursor(feature_class)
for row in cursor:
    if row.getValue(attribute) in unique_list:
        row.setValue('unique','False')
        cursor.updateRow(row)
    else:
        unique_list.append(row.getValue(attribute))
        row.setValue('unique','True')
        cursor.updateRow(row)

if int(arcpy.GetCount_management(feature_class).getOutput(0)) == len(unique_list):
    arcpy.AddWarning("All {a}s are unique.".format(a=attribute))
    arcpy.DeleteField_management(feature_class, "unique")
else:
    arcpy.AddWarning("There are dupliace values in {a}.".format(a=attribute))