import ifcopenshell

from .external.BIManalyst_g_40.rules import windowRule
from .external.BIManalyst_g_44.rules import doorRule

model = ifcopenshell.open("path/to/ifcfile.ifc")

windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
