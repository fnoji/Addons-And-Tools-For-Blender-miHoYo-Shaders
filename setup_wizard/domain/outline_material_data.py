# Author: michael-gh1

from bpy.types import Material


class OutlineMaterialGroup:
    def __init__(self, material: Material, outlines_material: Material):
        self.material = material
        self.outlines_material = outlines_material
