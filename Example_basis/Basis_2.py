import ifcopenshell
import numpy as np

ifc_ark = 'LLYN - ARK.ifc'
ifc_el  = 'LLYN - EL.ifc'
ifc_kon = 'LLYN - STRU.ifc'

def beam_length(ifc_file):
    total_beam_Length = 0
    ifc_file = ifcopenshell.open(ifc_file)
    for entity in ifc_file.by_type("IfcBeam"):

        #we need to get the attributes
       for relDefinesByProperties in entity.IsDefinedBy:
            for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                #and then get the attribute we are looking for
                if prop.Name == 'Length':
                    #add the length to the total length
                    total_beam_length += prop.NominalValue.wrappedValue


    print(f"\nThere are {total_beam_Length} meters of beam in the model")