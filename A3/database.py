import ifcopenshell
import numpy as np
import pandas as pd



def window_to_then_wall(ifc_file,cost_df):
    # IFC files = open ifc file
    # cost_df = Cost data frame a pandas dataframe
    # Extract all physical elements
    ifc_types = ['Door','Wall','Window']
    physical_elements = []
    for typ in ifc_types:
         physical_elements.append(ifc_file.by_type('Ifc'+typ))

    # Prepare data for DataFrame
    data = []
    for q in physical_elements:
        for element in q:
            element_data = {
                'GlobalId': element.GlobalId,
                'Name': element.Name,
                'Type': element.is_a(),
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

    # Print all the unique types
    type = df['Type']

    type_u = type.unique().transpose()

    cat = []
    for i in type_u:
        indeks = type[i == type].index[0]
        cat.append(df['Category'][indeks])

    # print(type_u)
    # importing the database:
    type_df = cost_df['Type']
    ep_df = cost_df['Enhedspris']
    cost_dict = dict()

    for t in type_u:
        indeks = type_df[t == type_df].index[0]
        cost_dict[t] = ep_df[indeks]

    con = type.to_numpy()
    count= {}
    for d in type_u:
        count[d] = (np.count_nonzero(con == d))

    amount = {}
    for u in type_u:
        indek = df[u == df['Type']].index
        mng = 0
        for i in indek:
            mng += df['Area'][i]
        amount[u] = mng

    pris = []
    enhed = []
    ep = []
    mngde = []
    ind = 0
    for i in type_u:
        if cat[ind] == cat[0]:
            enhed.append('stk')
            mngde.append(count[i])
            pris.append(count[i]*cost_dict[i])
            ep.append(cost_dict[i])
        else:
            enhed.append('m2')
            mngde.append(amount[i])
            pris.append(amount[i] * cost_dict[i])
            ep.append(cost_dict[i])
        ind += 1
    un_df = pd.DataFrame({'Type': type_u,'Ehned': enhed, 'Mængde': mngde, 'Enhedspris': ep,'Pris': pris})

    # Export DataFrame to Excel
    un_df.to_excel('Cost_of_elements.xlsx', index=False)
    #
    print("Data has been exported to Cost_of_elements.xlsx")

    return


