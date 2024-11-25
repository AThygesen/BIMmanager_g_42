from database import window_to_then_wall
import ifcopenshell
import pandas as pd

# This code processes IFC building model data to extract information about doors, walls, and windows,
# combining it with cost data from a database to calculate quantities and costs.
# It creates a DataFrame with details like element type, quantity, unit price, and total cost,
# and exports the results to an Excel file. The main function also maps element categories and quantities
# to cost data for detailed analysis.
# The example database is in this case an Excel file

# Load the IFC file
ifc_file = ifcopenshell.open("PLACEHOLDER")
database = 'eksempel_database.xlsx'

cost_df = pd.read_excel(database, usecols='B, D', skiprows=2)
# runs script
window_to_then_wall(ifc_file, cost_df)

