import ifcopenshell

def check(item, files):

    for file in files: # Iterates through the files that have been provided
        try:
            model = ifcopenshell.open(file)
            thing = model.by_type(f'{item}')
            if thing: # If the Ifc item exists in the file this happens:
                print(f'There are {item} in {file}, the amount is {len(thing)}.')
            else:
                print(f'The item does not exist in the {file}.')
        except Exception as e:
            print(e,f'The error occured in{file}')
