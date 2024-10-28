import ifcopenshell
import pandas as pd

# Load the IFC file
ifc_file = ifcopenshell.open(r"C:\Users\August Thygesen\OneDrive\DTU\7. semester\Advanced BIM\Models\CES_BLD_24_06_ARC.ifc")

# Extract all physical elements
physical_elements = ifc_file.by_type('IfcProduct')

# Prepare data for DataFrame
data = []
for element in physical_elements:
    element_data = {
        'GlobalId': element.GlobalId,
        'Name': element.Name,
        'Type': element.is_a(),
        'Description': element.Description
    }
    
    # Extract quantities
    quantities = ifc_file.by_type('IfcElementQuantity')
    for quantity in quantities:
        if quantity.RelatingPropertyDefinition.is_a('IfcElementQuantity'):
            for q in quantity.RelatingPropertyDefinition.Quantities:
                element_data[q.Name] = q[3]  # q[3] is the value of the quantity
    
    # Extract measurements or sizes
    for definition in element.IsDefinedBy:
        if definition.is_a('IfcRelDefinesByProperties'):
            property_set = definition.RelatingPropertyDefinition
            if property_set.is_a('IfcPropertySet'):
                for prop in property_set.HasProperties:
                    if prop.is_a('IfcPropertySingleValue'):
                        element_data[prop.Name] = prop.NominalValue.wrappedValue
    
    data.append(element_data)

# Create DataFrame
df = pd.DataFrame(data)

# Export DataFrame to Excel
df.to_excel('physical_elements_with_quantities_and_sizes.xlsx', index=False)

print("Data has been exported to physical_elements_with_quantities_and_sizes.xlsx")