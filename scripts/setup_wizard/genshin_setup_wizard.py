# Structure for class comes from a script initially written by Zekium from Discord
# Written by Mken from Discord

import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty
from bpy.types import Operator

import os


class GI_OT_GenshinSetupWizard(Operator, ImportHelper):
    """Setup Wizard Process"""
    bl_idname = "file.genshin_setup_wizard"
    bl_label = "0_Genshin: Setup Wizard -  Select Festivity's Shaders Folder"

    # ImportHelper mixin class uses this
    filename_ext = "*.*"
    
    import_path: StringProperty(
        name = "Path",
        description = "Path to the folder containing the files to import",
        default = "",
        subtype = 'DIR_PATH'
        )

    filter_glob: StringProperty(
        default="*.*",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    def execute(self, context):
        invoke_next_step = setup_dependencies(self.filepath)
        invoke_next_step(
            1, 
            file_path_to_cache = self.filepath, 
            path_to_streamlined_setup=os.path.join(self.filepath, 'scripts/' 'setup_wizard/')
        )

        return {'FINISHED'}


def register():
    bpy.utils.register_class(GI_OT_GenshinSetupWizard)


# Specifically done this way because path is dependent on where Blender is started
# We ask for the filepath to Festivity's shaders that way we can set up the scripts in the path
# I hate this, hopefully there's a better way
def setup_dependencies(filepath):
    directory = os.path.dirname(filepath)
    print(f'Setting up sys.path with {directory}')

    import sys
    if filepath not in sys.path:
        sys.path.append(directory)

    from scripts.setup_wizard.import_order import invoke_next_step
    from scripts.setup_wizard.genshin_import_materials import GI_OT_GenshinImportMaterials
    from scripts.setup_wizard.genshin_import_character_model import GI_OT_GenshinImportModel
    from scripts.setup_wizard.genshin_replace_default_materials import GI_OT_GenshinReplaceDefaultMaterials
    from scripts.setup_wizard.genshin_import_textures import GI_OT_GenshinImportTextures
    from scripts.setup_wizard.genshin_import_outlines import GI_OT_GenshinImportOutlines
    from scripts.setup_wizard.genshin_import_outline_lightmaps import GI_OT_GenshinImportOutlineLightmaps
    from scripts.setup_wizard.genshin_import_material_data import GI_OT_GenshinImportMaterialData

    # Originally I tried checking, but this way is less bug-prone and is more Pythonic
    # Tried checking for attributes (on bpy.ops.file.xxx), but it seemed to always return true
    for class_to_register in [
        GI_OT_GenshinImportMaterials, 
        GI_OT_GenshinImportModel, 
        GI_OT_GenshinReplaceDefaultMaterials,
        GI_OT_GenshinImportTextures, 
        GI_OT_GenshinImportOutlines, 
        GI_OT_GenshinImportMaterialData, 
        GI_OT_GenshinImportOutlineLightmaps]:
        try:
            bpy.utils.register_class(class_to_register)
        except ValueError:
            pass  # expected if class is already registered
    return invoke_next_step


# Need to have run setup_dependencies in order to unregister, otherwise sys.path 
# will be missing the filepath to the scripts folder
def unregister():
    from scripts.setup_wizard.genshin_import_materials import GI_OT_GenshinImportMaterials
    from scripts.setup_wizard.genshin_import_character_model import GI_OT_GenshinImportModel
    from scripts.setup_wizard.genshin_replace_default_materials import GI_OT_GenshinReplaceDefaultMaterials
    from scripts.setup_wizard.genshin_import_textures import GI_OT_GenshinImportTextures
    from scripts.setup_wizard.genshin_import_outlines import GI_OT_GenshinImportOutlines
    from scripts.setup_wizard.genshin_import_outline_lightmaps import GI_OT_GenshinImportOutlineLightmaps
    from scripts.setup_wizard.genshin_import_material_data import GI_OT_GenshinImportMaterialData

    bpy.utils.unregister_class(GI_OT_GenshinImportMaterials)
    bpy.utils.unregister_class(GI_OT_GenshinImportModel)
    bpy.utils.unregister_class(GI_OT_GenshinReplaceDefaultMaterials)
    bpy.utils.unregister_class(GI_OT_GenshinImportTextures)
    bpy.utils.unregister_class(GI_OT_GenshinImportOutlines)
    bpy.utils.unregister_class(GI_OT_GenshinImportOutlineLightmaps)
    bpy.utils.unregister_class(GI_OT_GenshinImportMaterialData)


if __name__ == "__main__":
    register()
