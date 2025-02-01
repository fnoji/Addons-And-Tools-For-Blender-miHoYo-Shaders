bl_info = {
    "name": "Setup Wizard - WuWa Beta Version 2025/02/01",
    "author": "Mken, OctavoPE, Enthralpy, fnoji",
    "version": (2, 6, 4),
    "blender": (3, 3, 0),
    "location": "3D View > Sidebar > Genshin Impact / Honkai Star Rail / Punishing Gray Raven / Wuthering Waves",
    "description": "An addon to streamline the character model setup process when using Festivity, Nya222's or JaredNyts' Shaders",
    "warning": "",
    "doc_url": "",
    "support": 'COMMUNITY',
    "category": "HoYoverse",
    "tracker_url": "",
    "doc_url": ""
}

import bpy
import importlib
import setup_wizard.cache_operator
from setup_wizard.cache_operator import ClearCacheOperator
from setup_wizard.genshin_import_materials import GI_OT_SetUpMaterials, HSR_OT_SetUpMaterials
from setup_wizard.genshin_import_outlines import GI_OT_SetUpOutlines, HSR_OT_SetUpOutlines
from setup_wizard.misc_final_steps import GI_OT_FinishSetup, HSR_OT_FinishSetup
from setup_wizard.character_rig_setup.character_rigger_operator import GI_OT_RigCharacter
from setup_wizard.character_rig_setup.character_rigger_props import CharacterRiggerPropertyGroup, \
    CharacterRiggerPropertyManager
from setup_wizard.genshin_compositing_node_setup import GI_OT_PostProcessingCompositingSetup

import setup_wizard.ui.gi_ui_setup_wizard_menu
from setup_wizard.ui.gi_ui_setup_wizard_menu import \
    UI_Properties, \
    GI_PT_Setup_Wizard_UI_Layout, \
    GI_PT_Basic_Setup_Wizard_UI_Layout, \
    GI_PT_Advanced_Setup_Wizard_UI_Layout, \
    GI_PT_UI_Character_Model_Menu, \
    GI_PT_UI_Materials_Menu, \
    GI_PT_UI_Outlines_Menu, \
    GI_PT_UI_Finish_Setup_Menu, \
    GI_PT_UI_Character_Rig_Setup_Menu, \
    GI_PT_UI_Post_Processing_Setup_Menu, \
    GI_PT_UI_Post_Processing_Node_Editor_Setup_Menu
from setup_wizard.ui.hsr_ui_setup_wizard_menu import \
    HSR_PT_Setup_Wizard_UI_Layout, \
    HSR_PT_Basic_Setup_Wizard_UI_Layout, \
    HSR_PT_Advanced_Setup_Wizard_UI_Layout, \
    HSR_PT_UI_Character_Model_Menu, \
    HSR_PT_UI_Materials_Menu, \
    HSR_PT_UI_Outlines_Menu, \
    HSR_PT_UI_Finish_Setup_Menu, \
    HSR_PT_UI_Character_Rig_Setup_Menu
    # HSR_PT_UI_Compositing_Panel_Post_Processing_UI_Layout
from setup_wizard.ui.pgr_ui_setup_wizard_menu import \
    PGR_PT_Setup_Wizard_UI_Layout, \
    PGR_PT_Basic_Setup_Wizard_UI_Layout, \
    PGR_PT_Advanced_Setup_Wizard_UI_Layout, \
    PGR_PT_UI_Character_Model_Menu, \
    PGR_PT_UI_Materials_Menu, \
    PGR_PT_UI_Outlines_Menu, \
    PGR_PT_UI_Finish_Setup_Menu
from setup_wizard.ui.ww_ui_setup_wizard_menu import \
    WW_PT_Setup_Wizard_UI_Layout, \
    WW_PT_Basic_Setup_Wizard_UI_Layout, \
    WW_PT_Advanced_Setup_Wizard_UI_Layout, \
    WW_PT_UI_Character_Model_Menu, \
    WW_PT_UI_Materials_Menu, \
    WW_PT_UI_Outlines_Menu, \
    WW_PT_UI_Finish_Setup_Menu

from setup_wizard.genshin_import_character_model import GI_OT_SetUpCharacter, HSR_OT_SetUpCharacter

import setup_wizard.genshin_setup_wizard
from setup_wizard.genshin_setup_wizard import GI_OT_GenshinSetupWizardUI, HSR_OT_HonkaiStarRailSetupWizardUI, PGR_OT_SetupWizardUI, WW_OT_SetupWizardUI, register as register_genshin_setup_wizard, setup_dependencies

from setup_wizard.ww_unmute_material_nodes import WW_OT_UnmuteMaterialNodes

register_genshin_setup_wizard()
setup_dependencies()

modules = [
    setup_wizard.ui.gi_ui_setup_wizard_menu,
    setup_wizard.genshin_setup_wizard,
    setup_wizard.cache_operator
]

classes = [
    CharacterRiggerPropertyGroup,
    CharacterRiggerPropertyManager,
    GI_PT_Setup_Wizard_UI_Layout, 
    GI_PT_Basic_Setup_Wizard_UI_Layout,
    GI_PT_Advanced_Setup_Wizard_UI_Layout,
    GI_PT_UI_Character_Model_Menu, 
    GI_PT_UI_Materials_Menu, 
    GI_PT_UI_Outlines_Menu, 
    GI_PT_UI_Finish_Setup_Menu,
    GI_PT_UI_Character_Rig_Setup_Menu,
    GI_PT_UI_Post_Processing_Setup_Menu,
    GI_PT_UI_Post_Processing_Node_Editor_Setup_Menu,
    GI_OT_GenshinSetupWizardUI,
    GI_OT_SetUpCharacter,
    GI_OT_SetUpMaterials,
    GI_OT_SetUpOutlines,
    GI_OT_FinishSetup,
    GI_OT_RigCharacter,
    GI_OT_PostProcessingCompositingSetup,
    HSR_PT_Setup_Wizard_UI_Layout,
    HSR_PT_Basic_Setup_Wizard_UI_Layout,
    HSR_PT_Advanced_Setup_Wizard_UI_Layout,
    HSR_PT_UI_Character_Model_Menu,
    HSR_PT_UI_Materials_Menu,
    HSR_PT_UI_Outlines_Menu,
    HSR_PT_UI_Finish_Setup_Menu,
    HSR_PT_UI_Character_Rig_Setup_Menu,
    # HSR_PT_UI_Compositing_Panel_Post_Processing_UI_Layout,
    HSR_OT_HonkaiStarRailSetupWizardUI,
    HSR_OT_SetUpCharacter,
    HSR_OT_SetUpMaterials,
    HSR_OT_SetUpOutlines,
    HSR_OT_FinishSetup,
    PGR_OT_SetupWizardUI,
    PGR_PT_Setup_Wizard_UI_Layout,
    PGR_PT_Basic_Setup_Wizard_UI_Layout,
    PGR_PT_Advanced_Setup_Wizard_UI_Layout,
    PGR_PT_UI_Character_Model_Menu,
    PGR_PT_UI_Materials_Menu,
    PGR_PT_UI_Outlines_Menu,
    PGR_PT_UI_Finish_Setup_Menu,
    WW_PT_Setup_Wizard_UI_Layout,
    WW_PT_Basic_Setup_Wizard_UI_Layout,
    WW_PT_Advanced_Setup_Wizard_UI_Layout,
    WW_PT_UI_Character_Model_Menu,
    WW_PT_UI_Materials_Menu,
    WW_PT_UI_Outlines_Menu,
    WW_PT_UI_Finish_Setup_Menu,
    WW_OT_SetupWizardUI,
    ClearCacheOperator,
    WW_OT_UnmuteMaterialNodes,
]

for module in modules:
    try:
        importlib.reload(module)
    except ModuleNotFoundError:
        pass  # likely new class

register, unregister = bpy.utils.register_classes_factory(classes)
UI_Properties.create_custom_ui_properties()


'''
For auto_loading, but right now we're doing simple loading to have
direct control for the order of class registration.
'''
'''
# from setup_wizard import auto_load
# auto_load.init()


# def register():
#     # auto_load.register()


# def unregister():
#     # auto_load.unregister()
'''
