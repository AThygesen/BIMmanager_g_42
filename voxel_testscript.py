import ifcopenshell 
import voxec

file = parse(r"C:\Users\August Thygesen\OneDrive\DTU\7. semester\Advanced BIM\Models\CES_BLD_24_06_ARC.ifc")
slabss = create_geometry(file, include={"IfcSlab"})
roofss = create_geometry(file, include={"IfcRoof"})
slabs = voxelize(slabss)
roofs = voxelize(roofss)
floors_surface = subtract(slabs, roofs)
floor_volume = volume2(floors_surface)
floors = union(floors_surface, floor_volume)
floors_surface = collapse(floors, 0, 0, -1)
num = count(floors_surface)