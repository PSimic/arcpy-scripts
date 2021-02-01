import arcpy

database = arcpy.GetParameterAsText(0) 
txtFile = arcpy.GetParameterAsText(1)

logfile = open(txtFile, 'w')

def log_results(message):
    print(message)
    logfile.write(message)
    logfile.flush()
    return

def print_fc(list):
    for fc in list:
        desc = arcpy.Describe(fc)
        log_results ("\n Feature Class Name : {0}  \n Geometry Type      : {1}  \n Has Spatial Index  : {2}  \n Spatial Reference  : {3}".format(fc,desc.shapeType,str(desc.hasSpatialIndex),desc.spatialReference.name))
        fields = arcpy.ListFields(fc)
        fldCnt = 0

        for field in fields:
            log_results ("\n    Field Name : {0: <24}  Field Type : {1: <20}  Field Length : {2}".format(field.name, field.type, field.length))
            fldCnt += 1

        log_results ("\n # of Fields in Feature Class '{0}' = {1} \n".format(fc, fldCnt))

def listFcsInGDB(gdb):
    try:
        wk = arcpy.env.workspace = gdb
        
        if not arcpy.Exists(wk):
            log_results("\n" + "Database DOES NOT EXIST!\n")
        else:
            fldCnt = 0

            # Inside Feature datasets:
            fdList = arcpy.ListDatasets(feature_type="feature")
            
            for fds in fdList:
                log_results ("\n ---- Feature dataset: {0} ---- \n".format(fds))
                fcListInside = arcpy.ListFeatureClasses(feature_dataset=fds)
                print_fc(fcListInside)

            # Stand-alone feature classes:
            log_results ("\n ---- Stand-alone feature classes ---- \n")
            fcListOutside = arcpy.ListFeatureClasses()
            print_fc(fcListOutside)
            
            log_results ("\n\n COMPLETED!! \n")

        logfile.close()

    except arcpy.ExecuteError:
        log_results (arcpy.GetMessages(2))

    except Exception as e:
        log_results (e[0])

if __name__ == '__main__':
    listFcsInGDB(database)