import ifcopenshell

def door(ifc_file):
    ifc_file = ifcopenshell.open(ifc_file)

    doors_required = 14  ### <- Expected value of doors ###
    doors_in_model = len(ifc_file.by_type("IfcDoor"))
    min_width_door = 0.77
    valid_doors = 0
    invalid_doors = 0

    print('\n')

    # initial check to establish if we have the 'correct' number of doors
    if doors_required is doors_in_model:
        print("Result matches expected value ({})".format(doors_required))
    elif doors_required > doors_in_model:
        print("There are more doors than expected")
    elif doors_required < doors_in_model:
        print("There are less doors than expected")
    print('\n')
    # check each door to see if it complies and count the valid ones
    for door in ifc_file.by_type("IfcDoor"):
        print("door with width: " + str(door.OverallWidth))
        if door.OverallWidth >= min_width_door:
            valid_doors += 1
        # now we have finished the counting we can pull back the indents and print the result
    print(f"\nThe width of {valid_doors} doors is according to the Danish Regulations")
    print(f"The width of {doors_in_model - valid_doors} doors is not according to the Danish Regulations")

