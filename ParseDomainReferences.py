import arcpy, os, sys

relPath = sys.path[0]
gdb = arcpy.GetParameterAsText(0) 
arcpy.AddMessage ("gdb: " + str(gdb))
arcpy.AddMessage (" ")

arcpy.env.workspace = gdb


def ParseFieldList (fc, fcPath):
    # get field list
    fldList = arcpy.ListFields (fc)
    if len (fldList) > 0:
      for fld in fldList:
        s = ""
        if fld.domain != None:
          if fld.domain != "":
            s = ", domain [" + fld.domain + "]"
        arcpy.AddMessage ("  fld " + fld.name + s)
      arcpy.AddMessage (" ")

      # get subtype list
      subDict = arcpy.da.ListSubtypes (fcPath)
      if len (subDict) > 0:
        for stCode in subDict.iteritems():
          #arcpy.AddMessage ("Subtype Code: {0}".format(stCode))
          valkey, vallist = stCode
          arcpy.AddMessage ("Subtype Code: {0}".format(valkey))
          i = 0
          for subCode in vallist.iteritems():
            i += 1
            if i < 4:
              arcpy.AddMessage ("subCode: {0}".format(subCode))
            else:
              fldkey, fldlist = subCode
              arcpy.AddMessage (fldkey)
              for fld in fldlist.iteritems():
                fldName, fldDefs = fld
                deflt, dom = fldDefs
                s1 = "[no default]"
                if deflt != None:
                  s1 = str(deflt)
                s2 = "[no domain]"
                if dom != None:
                  s2 = dom.name
                arcpy.AddMessage ("fldName: " + fldName + ", default: " + s1 + ", domain: " + s2)
          arcpy.AddMessage (" ")
        arcpy.AddMessage (" ")

fcList = arcpy.ListFeatureClasses()
if len(fcList) > 0:
  for fc in fcList:
    arcpy.AddMessage ("fc at root level: " + str(fc))
    fcPath = os.path.join (gdb, fc)
    ParseFieldList (fc, fcPath)

tblList = arcpy.ListTables()
if len(tblList) > 0:
  for tbl in tblList:
    arcpy.AddMessage ("tbl at root level: " + str(tbl))
    tblPath = os.path.join (gdb, tbl)
    ParseFieldList (tbl, tblPath)

dsList = arcpy.ListDatasets()
if len(dsList) > 0:
  for ds in dsList:
    arcpy.AddMessage ("feature dataset: " + str(ds))
    arcpy.AddMessage (" ")

    fcList = arcpy.ListFeatureClasses (feature_dataset=ds)
    if len (fcList) > 0:
      for fc in fcList:
        arcpy.AddMessage ("fc at fds level: " + str(fc))
        fcPath = os.path.join (gdb, fc)
        ParseFieldList (fc, fcPath)
