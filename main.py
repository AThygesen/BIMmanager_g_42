import ifcopenshell

from .external.BIManalyst_g_40_new import Week_3
from external.BIManalyst_g_41.rules import BikeSpace
from .external.BIManalyst_g_44 import ColumnVolumesAndCost

model_arc = ifcopenshell.open(r"C:\Users\mouss\OneDrive - Danmarks Tekniske Universitet\Kandidat\41934 Advanced Building Information Modeling (BIM), Fall 2024\CES_BLD_24_06_ARC.ifc")
model_str = ifcopenshell.open(r"C:\Users\mouss\OneDrive - Danmarks Tekniske Universitet\Kandidat\41934 Advanced Building Information Modeling (BIM), Fall 2024CES_BLD_24_06_STR.ifc")

#beam_rule = beamCheck(model)
Bikespace_result = BikeSpace.count_furniture_shelving_storage(model_arc)
Column_price = ColumnVolumesAndCost.calculate_total_column_volume(model_str)

print("Beam rule:", Week_3)
print("Bikespace:", Bikespace_result)
print("column price:", Column_price)


