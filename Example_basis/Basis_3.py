import ifcopenshell
import numpy as np

# this just gets you the entity, defined here as wall
# feel free to change this to your needs
# appending [0] to the end means that we only get the first entity
# if you remove the [0] you will get all the ifcwall entitities in the model.
# If you are using a model in an older IFC version like 2x3, there are other classes that describe a wall (HINT: IfcWallStandardCase)
def wall_name(ifc_file):
    ifc_file = ifcopenshell.open(ifc_file)
    wall = ifc_file.by_type('IfcWall')[0]
    for definition in wall.IsDefinedBy:
        # To support IFC2X3, we need to filter our results.
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            # Might return Pset_WallCommon
            print(property_set.Name)
