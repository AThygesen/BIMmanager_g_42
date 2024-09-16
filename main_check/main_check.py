from Check_model import check
from get_ifc import get_ifc

# Get the files from the current folder.
ifc_files = get_ifc()

# Define the IfcType
item = 'IfcFace'


check(item, ifc_files)

#### When the script is running, remember to be patient, it can take some time

