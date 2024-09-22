import ifcopenshell
import numpy as np

def spaces_amount(ifc_file):
    ifc_file = ifcopenshell.open(ifc_file)
    spaces_in_model = len(ifc_file.by_type("IfcSpace"))
    spaces_required = 21

    print(f"\nThere are {spaces_in_model} spaces in the model")

    if spaces_required is spaces_in_model:
        print ('RESULT: The number of spaces is correct')
    else:
        print ('RESULT: The number of doors is wrong')

spaces_amount('LLYN - ARK.ifc')