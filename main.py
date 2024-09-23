import ifcopenshell

#from .external.BIManalyst_g_40_new import Week 3
from .external.BIManalyst_g_41.rules import BikeSpace
#from .external.BIManalyst_g_44.rules import beam_price_based_on_meter

model = ifcopenshell.open("C:\Users\August Thygesen\OneDrive\DTU\7. semester\Advanced BIM\Models\LLYN - ARK.ifc")

#beam_rule = beamCheck(model)
Bikespace_result = BikeSpace.count_furniture_shelving_storage(model)
#beam_price = beam_price_based_on_meter.checkRule(model)

#print("Beam rule:", beam_rule)
print("Bikespace:", Bikespace_resultl)
#print("Beam price:", beam_price)

