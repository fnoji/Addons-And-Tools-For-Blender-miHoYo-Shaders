import bpy
from bpy.types import Operator
from setup_wizard.setup_wizard_operator_base_classes import CustomOperatorProperties
from setup_wizard.domain.game_types import GameType

class WW_OT_UnmuteMaterialNodes(Operator, CustomOperatorProperties):
    """指定されたマテリアルノードのミュートを解除"""
    bl_idname = "ww.unmute_material_nodes"
    bl_label = "Unmute Material Nodes"
    
    game_type: bpy.props.StringProperty(default=GameType.WUTHERING_WAVES.name)

    def execute(self, context):
        # BangsマテリアルのGroup.002ノード
        bangs_material = bpy.data.materials.get('WW - Bangs')
        if bangs_material and bangs_material.node_tree:
            group_node = bangs_material.node_tree.nodes.get('Group.002')
            if group_node:
                group_node.mute = False
        
        bangs_material = bpy.data.materials.get('WW - Hair')
        if bangs_material and bangs_material.node_tree:
            group_node = bangs_material.node_tree.nodes.get('Group.002')
            if group_node:
                group_node.mute = False
        
        # FaceマテリアルのGroup.003ノード
        face_material = bpy.data.materials.get('WW - Face')
        if face_material and face_material.node_tree:
            group_node = face_material.node_tree.nodes.get('Group.003')
            if group_node:
                group_node.mute = False
        
        # FaceマテリアルのGroup.004ノードのinput_5を設定
        face_material = bpy.data.materials.get('WW - Face')
        if face_material and face_material.node_tree:
            group_node = face_material.node_tree.nodes.get('Shadow Mask Converter')
            if group_node:
                # ノードの実際の入力ソケット名が異なるためインデックス指定に変更
                group_node.inputs[2].default_value = 1  # インデックス2が正しい入力ソケット
        
        # EyeマテリアルのGroup.003ノード
        eye_material = bpy.data.materials.get('WW - Eye')
        if eye_material and eye_material.node_tree:
            group_node = eye_material.node_tree.nodes.get('Group.003')
            if group_node:
                group_node.mute = False
                
        # BodyマテリアルのGroup.004ノードのinput_5を設定
        body_material = bpy.data.materials.get('WW - Up')
        if body_material and body_material.node_tree:
            group_node = body_material.node_tree.nodes.get('Group.004')
            if group_node:
                # input_5の値を1に設定
                group_node.inputs[5].default_value = 1
        
        # BodyマテリアルのGroup.004ノードのinput_5を設定
        body_material = bpy.data.materials.get('WW - Down')
        if body_material and body_material.node_tree:
            group_node = body_material.node_tree.nodes.get('Group.004')
            if group_node:
                # input_5の値を1に設定
                group_node.inputs[5].default_value = 1
                
        return {'FINISHED'}