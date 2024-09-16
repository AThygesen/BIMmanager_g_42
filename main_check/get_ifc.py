import os

def get_ifc():
    # find Ifc_files
    path = os.getcwd()
    folder = os.listdir(path)
    ifc_files = []

    for ifc in folder:
        if '.ifc' in ifc:
            ifc_files.append(ifc)
    print(f'These are the files that have been found {ifc_files}')
    return ifc_files