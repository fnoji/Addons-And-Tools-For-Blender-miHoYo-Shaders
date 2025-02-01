# Author: michael-gh1

import bpy
from bpy.types import Panel, UILayout

from setup_wizard import bl_info
from setup_wizard.domain.game_types import GameType

rigging_global_settings_feature_flag = False

class UI_Properties:
    @staticmethod
    def create_custom_ui_properties():
        if rigging_global_settings_feature_flag:
            bpy.types.WindowManager.setup_wizard_full_run_rigging_enabled = bpy.props.BoolProperty(
                name = " Rigging Enabled",
                default = True
            )

        # bpy.types.WindowManager.setup_wizard_join_meshes_enabled = bpy.props.BoolProperty(
        #     name = " Join Meshes Enabled",
        #     default = True
        # )

        bpy.types.WindowManager.cache_enabled = bpy.props.BoolProperty(
            name = "Cache Enabled",
            default = True
        )

        bpy.types.WindowManager.setup_wizard_betterfbx_enabled = bpy.props.BoolProperty(
            name = "BetterFBX Enabled",
            default = True
        )


class WW_PT_Setup_Wizard_UI_Layout(Panel):
    bl_label = "Wuthering Waves Setup Wizard"
    bl_idname = "WW_PT_Setup_Wizard_UI_Layout"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Wuthering Waves"

    def draw(self, context):
        layout = self.layout
        window_manager = context.window_manager

        version_text = layout.row()
        version_text.label(text='v' + '.'.join([str(version_num) for version_num in bl_info.get('version')]))

        sub_layout = layout.box()
        OperatorFactory.create(
            sub_layout,
            'wuthering_waves.setup_wizard_ui',
            'Run Entire Setup',
            'PLAY',
            game_type=GameType.WUTHERING_WAVES.name
        )

        expy_kit_installed = bpy.context.preferences.addons.get('Expy-Kit-main')
        betterfbx_installed = bpy.context.preferences.addons.get('better_fbx')
        rigify_installed = bpy.context.preferences.addons.get('rigify')

        if (not expy_kit_installed or not betterfbx_installed or not rigify_installed) and rigging_global_settings_feature_flag:
            sub_layout.label(text='Rigging Disabled', icon='ERROR')

        settings_box = layout.box()
        settings_box.label(text='Global Settings', icon='WORLD')

        row = settings_box.row()
        row.prop(window_manager, 'cache_enabled')
        OperatorFactory.create(
            row,
            'genshin.clear_cache_operator',
            'Clear Cache',
            'TRASH',
            game_type=GameType.WUTHERING_WAVES.name,
        )

        if betterfbx_installed:
            row2 = settings_box.row()
            row2.prop(window_manager, 'setup_wizard_betterfbx_enabled')

        # settings_box.prop(window_manager, 'setup_wizard_join_meshes_enabled')
        if rigging_global_settings_feature_flag:
            settings_box.prop(window_manager, 'setup_wizard_full_run_rigging_enabled')

class WW_PT_Basic_Setup_Wizard_UI_Layout(Panel):
    bl_label = 'Basic Setup'
    bl_idname = 'WW_PT_UI_Basic_Setup_Layout'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Wuthering Waves"

    def draw(self, context):
        layout = self.layout
        sub_layout = layout.box()

        OperatorFactory.create(
            sub_layout,
            'genshin.set_up_character',
            'Set Up Character',
            icon='OUTLINER_OB_ARMATURE',
            game_type=GameType.WUTHERING_WAVES.name,
        )
        OperatorFactory.create(
            sub_layout,
            'genshin.set_up_materials',
            'Set Up Materials',
            icon='MATERIAL',
            game_type=GameType.WUTHERING_WAVES.name,
        )
        if bpy.app.version >= (3,3,0):
            OperatorFactory.create(
                sub_layout,
                'genshin.set_up_outlines',
                'Set Up Outlines',
                icon='GEOMETRY_NODES',
                game_type=GameType.WUTHERING_WAVES.name,
            )
        else:
            layout.label(text='(Outlines Disabled < v3.3.0)')
        OperatorFactory.create(
            sub_layout,
            'genshin.finish_setup',
            'Finish Setup',
            icon='CHECKMARK',
            game_type=GameType.WUTHERING_WAVES.name,
        )

#        paint_helpers = sub_layout.box()
#        paint_helpers.label(text='Vertex/Texture Paint Helpers')
#        OperatorFactory.create(
#            paint_helpers,
#            'punishing_gray_raven.paint_vertex_colors',
#            'Paint Vertex Colors',
#            'VPAINT_HLT',
#            game_type=GameType.WUTHERING_WAVES.name,
#        )
#        OperatorFactory.create(
#            paint_helpers,
#            'punishing_gray_raven.paint_face_shadow_texture',
#            'Paint Face Shadow Texture',
#            'TPAINT_HLT',
#            game_type=GameType.WUTHERING_WAVES.name,
#        )
#        OperatorFactory.create(
#            paint_helpers,
#            'punishing_gray_raven.paint_vertex_erase_face_alpha',
#            'Erase Face Alpha',
#            'GPBRUSH_ERASE_HARD',
#            game_type=GameType.WUTHERING_WAVES.name,
#        )

#        chibi_helpers = sub_layout.box()
#        chibi_helpers.label(text='Chibi Face Setup')
#        OperatorFactory.create(
#            chibi_helpers,
#            'punishing_gray_raven.set_up_chibi_face_mesh',
#            'Set Up Chibi Face Mesh',
#            'OUTLINER_OB_MESH',
#            game_type=GameType.WUTHERING_WAVES.name,
#        )
#        OperatorFactory.create(
#            chibi_helpers,
#            'punishing_gray_raven.import_chibi_face_texture',
#            'Import Face Texture',
#           'TEXTURE',
#            game_type=GameType.WUTHERING_WAVES.name,
#        )


class WW_PT_Advanced_Setup_Wizard_UI_Layout(Panel):
    bl_label = 'Advanced Setup'
    bl_idname = 'WW_PT_UI_Advanced_Setup_Layout'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Wuthering Waves"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout


class WW_PT_UI_Character_Model_Menu(Panel):
    bl_label = 'Set Up Character Menu'
    bl_idname = 'WW_PT_UI_Character_Model_Menu'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'WW_PT_UI_Advanced_Setup_Layout'

    def draw(self, context):
        layout = self.layout
        sub_layout = layout.column()

        OperatorFactory.create(
            sub_layout,
            'genshin.import_model',
            'Import Character Model',
            'OUTLINER_OB_ARMATURE',
        )
        OperatorFactory.create(
            sub_layout,
            'genshin.delete_empties',
            'Delete Empties',
            'TRASH'
        )


class WW_PT_UI_Materials_Menu(Panel):
    bl_label = 'Set Up Materials Menu'
    bl_idname = 'WW_PT_UI_Materials_Menu'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'WW_PT_UI_Advanced_Setup_Layout'

    def draw(self, context):
        layout = self.layout
        sub_layout = layout.column()

        OperatorFactory.create(
            sub_layout,
            'genshin.import_materials',
            'Import WW Materials',
            'MATERIAL',
            game_type=GameType.WUTHERING_WAVES.name,
        )
        OperatorFactory.create(
            sub_layout,
            'genshin.replace_default_materials',
            'Replace Default Materials',
            'ARROW_LEFTRIGHT',
            game_type=GameType.WUTHERING_WAVES.name,
        )
        OperatorFactory.create(
            sub_layout,
            'genshin.import_textures',
            'Import Character Textures',
            'TEXTURE',
            game_type=GameType.WUTHERING_WAVES.name,
        )
        OperatorFactory.create(
            sub_layout,
            'ww.unmute_material_nodes',
            'Unmute Material Nodes',
            'NODE',
            game_type=GameType.WUTHERING_WAVES.name,
        )


class WW_PT_UI_Outlines_Menu(Panel):
    bl_label = 'Set Up Outlines Menu'
    bl_idname = 'WW_PT_UI_Outlines_Menu'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'WW_PT_UI_Advanced_Setup_Layout'

    def draw(self, context):
        layout = self.layout
        sub_layout = layout.column()
        scene = context.scene

        if bpy.app.version >= (3,3,0):
            OperatorFactory.create(
                sub_layout,
                'genshin.import_outlines',
                'Import Outlines',
                'FILE_FOLDER',
                game_type=GameType.WUTHERING_WAVES.name,
            )
            OperatorFactory.create(
                sub_layout,
                'genshin.setup_geometry_nodes',
                'Set Up Geometry Nodes',
                'GEOMETRY_NODES',
                game_type=GameType.WUTHERING_WAVES.name,
            )
            OperatorFactory.create(
                sub_layout,
                'genshin.import_outline_lightmaps',
                'Import Outline Lightmaps',
                'FILE_FOLDER',
                game_type=GameType.WUTHERING_WAVES.name,
            )

            sub_layout = layout.box()
            sub_layout.prop_search(scene, 'setup_wizard_material_for_material_data_import', bpy.data, 'materials')
            sub_layout.prop_search(scene, 'setup_wizard_outlines_material_for_material_data_import', bpy.data, 'materials')
            OperatorFactory.create(
                sub_layout,
                'genshin.import_material_data',
                'Import Material Data',
                'FILE',
                game_type=GameType.WUTHERING_WAVES.name,
                setup_mode='ADVANCED',
            )
        else:
            layout.label(text='(Outlines Disabled < v3.3.0)')


class WW_PT_UI_Finish_Setup_Menu(Panel):
    bl_label = 'Finish Setup Menu'
    bl_idname = 'WW_PT_UI_Misc_Setup_Menu'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'WW_PT_UI_Advanced_Setup_Layout'

    def draw(self, context):
        layout = self.layout
        sub_layout = layout.column()

        #OperatorFactory.create(
        #    sub_layout,
        #    'genshin.fix_transformations',
        #    'Fix Transformations',
        #    'OBJECT_DATA'
        #)
        OperatorFactory.create(
            sub_layout,
            'genshin.setup_head_driver',
            'Set Up Head Driver',
            'CONSTRAINT',
            game_type=GameType.WUTHERING_WAVES.name,
        )
        OperatorFactory.create(
            sub_layout,
            'genshin.set_color_management_to_standard',
            'Set Color Mgmt to Standard',
            'SCENE'
        )
        OperatorFactory.create(
            sub_layout,
            'hoyoverse.set_up_screen_space_reflections',
            'Enable SSR',
            'SCENE',
            game_type=GameType.WUTHERING_WAVES.name,
        )
        OperatorFactory.create(
            sub_layout,
            'hoyoverse.rename_shader_materials',
            'Rename Shader Materials',
            'GREASEPENCIL',
            game_type=GameType.WUTHERING_WAVES.name,
        )

        # OperatorFactory.create(
        #     sub_layout,
        #     'hoyoverse.join_meshes_on_armature',
        #     'Join Meshes on Armature',
        #     'RNA',
        #     game_type=GameType.WUTHERING_WAVES.name
        # )


'''
    This factory is intended to help create a UI element's operator (or the action it takes) when pressed.
    While it currently doesn't do anything too grand, it may provide future flexibility.
'''
class OperatorFactory:
    @staticmethod
    def create(
        ui_object: UILayout,
        operator: str,
        text: str,
        icon: str,
        operator_context='EXEC_DEFAULT',
        **kwargs
    ):
        ui_object.operator_context = operator_context
        ui_object = ui_object.operator(
            operator=operator,
            text=text,
            icon=icon,
        )

        for key, value in kwargs.items():
            setattr(ui_object, key, value)
