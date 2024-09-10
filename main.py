import ifcopenshell

from .external.BIManalyst_g_40.rules import doorRule
from .external.BIManalyst_g_41.rules import Qty_Of_Structural_Elements
from .external.BIManalyst_g_44 import beam_price_based_on_meter


model = ifcopenshell.open("path/to/ifcfile.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
