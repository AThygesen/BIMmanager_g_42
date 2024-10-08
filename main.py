import ifcopenshell

#from .external.BIManalyst_g_40_new import Week 3
from external.BIManalyst_g_41.rules import BikeSpace
#from .external.BIManalyst_g_44.rules import ColumnVolumesAndCost

model_arc = ifcopenshell.open("C:/Users/August Thygesen/OneDrive/DTU/7. semester/Advanced BIM/Models/CES_BLD_24_06_ARC.ifc")
model_str = ifcopenshell.open("C:/Users/August Thygesen/OneDrive/DTU/7. semester/Advanced BIM/Models/CES_BLD_24_06_STR.ifc")

#beam_rule = beamCheck(model)
Bikespace_result = BikeSpace.count_furniture_shelving_storage(model_arc)
#Column_price = ColumnVolumesAndCost.calculate_total_column_volume(model_str)

#print("Beam rule:", beam_rule)
print("Bikespace:", Bikespace_result)
#print("column price:", Column_price)


