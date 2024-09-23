import ifcopenshell

from .external.BIManalyst_g_40_new import main
#from .external.BIManalyst_g_41.rules import Qty_Of_Structural_Elements
#from .external.BIManalyst_g_44.rules import beam_price_based_on_meter
    

model = ifcopenshell.open("C:/Users/August Thygesen/OneDrive/DTU/7. semester/Advanced BIM\ModelsLLYN - ARK.ifc")

beam_rule = main(model)
#Qty_of_structural = Qty_Of_Structural_Elements.checkRule(model)
#beam_price = beam_price_based_on_meter.checkRule(model)

print("Beam rule:", beam_rule)
#print("Qty of structural elements:", Qty_of_structural)
#print("Beam price:", beam_price)