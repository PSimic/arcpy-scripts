from oletools.oleid import olefile

def mxd_version(filename):
    ofile = olefile.OleFileIO(filename)
    stream = ofile.openstream('Version')
    data = stream.read().decode('utf-16')
    version = data.split('\x00')[1]
    return version

import os
import glob
folder = r'C:\Users\PetarSimic\Desktop\QP_Refinery_GIS_15122020'
mxdFiles = glob.glob(os.path.join(folder, '*.mxd'))
for mxdFile in mxdFiles:
    fileName = os.path.basename(mxdFile)
    version = mxd_version(mxdFile)
    print version, fileName