import pefile
import os
import sys

def search(dllname,strsearch):
    pe = pefile.PE(dllname, fast_load=True)
    pe.parse_data_directories()
    e=0
    try:
        pe.DIRECTORY_ENTRY_EXPORT.symbols
        e=1        
    except:
        exit;
    if e==1:
        for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            fun = hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal
            if strsearch in str(fun[1]):
                print("[+] "+dllname)
                print("\t-"+str(fun[1]))

z=os.listdir("./")
if  len(sys.argv)>2:
                search(sys.argv[2],sys.argv[1])
else:
    for i in z:
        if ".dll" in i:
            search(i,sys.argv[1])
