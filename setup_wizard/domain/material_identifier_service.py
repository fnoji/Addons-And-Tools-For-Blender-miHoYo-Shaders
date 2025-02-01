# Author: michael-gh1

import bpy, re
from typing import Optional

from setup_wizard.domain.shader_material_names import JaredNytsPunishingGrayRavenShaderMaterialNames, JaredNytsWutheringWavesShaderMaterialNames


class PunishingGrayRavenMaterialIdentifierService:
    def get_body_part_name(self, full_name):
        try:
            last_index_of_first_group_of_numbers = self.__find_second_group_of_numbers(full_name)

            if last_index_of_first_group_of_numbers:
                # If there's an exact match then use that name (no body part at end of material name)
                # Otherwise try getting the body part at the end of the material name
                mesh_body_part_name = \
                    self.__exact_material_name_match_check(full_name, last_index_of_first_group_of_numbers) or \
                    full_name[last_index_of_first_group_of_numbers + 1:]
                return mesh_body_part_name
        except:
            return None
        return None

    def __find_second_group_of_numbers(self, input_string):
        # Find the first occurrence of numbers
        match = re.search(r'\d+', input_string)
        len_first_match = len(match.group())
        
        if match:
            # Find the second occurrence of numbers starting from the end of the first match
            match = re.search(r'\d+', input_string[match.span()[1]:])
            
            if match:
                numbers = match.group()
                last_index = match.span()[1] + len_first_match
                return last_index
        return None

    # Handle materials that are exact matches with the texture names (Lamiya's Trident)
    def __exact_material_name_match_check(self, full_name, last_index_of_first_group_of_numbers):
        exact_match_material = bpy.data.materials.get(
            f'{JaredNytsPunishingGrayRavenShaderMaterialNames.MATERIAL_PREFIX}{full_name[:last_index_of_first_group_of_numbers + 1]}'
        )
        if exact_match_material:
            return full_name[:last_index_of_first_group_of_numbers + 1]
        return None

    # Search original materials for a user of the texture name
    def search_original_material_user_for_body_part_name(self, texture_name):
        try:
            last_index_of_first_group_of_numbers = self.__find_second_group_of_numbers(texture_name)
        except:
            return None

        base_texture_name = texture_name[:last_index_of_first_group_of_numbers + 1]
        original_materials = [material for material in bpy.data.materials if 
                              JaredNytsPunishingGrayRavenShaderMaterialNames.MATERIAL_PREFIX not in material.name]
        
        for original_material in original_materials:
            try:
                base_color_texture_image_name = original_material.node_tree.nodes.get('Principled BSDF').inputs.get('Base Color').links[0].from_node.image.name_full
            except:
                continue

            if f'{base_texture_name}.png' == base_color_texture_image_name:
                body_part_name = original_material.name[last_index_of_first_group_of_numbers + 1:]
                return body_part_name

        # No texture image found, check if Chibi material
        if original_material.name == 'XDefaultMaterial':
            return 'XDefaultMaterial'
        return None

    # Get "real" body part name via original texture for this material (Cloth01 using Cloth)
    def get_body_part_name_of_shared_material(self, material_name):
        # Eye and Eyes will run into some funky logic, just keep using original results from `get_body_part_name()`
        if 'Eye' in material_name:
            return None

        try:
            base_color_texture_image_name = bpy.data.materials.get(material_name).node_tree.nodes.get('Principled BSDF').inputs.get('Base Color').links[0].from_node.image.name_full
        except:
            return None
        base_color_texture_image_name = base_color_texture_image_name.replace('.png', '')

        try:
            last_index_of_first_group_of_numbers = self.__find_second_group_of_numbers(base_color_texture_image_name)
            if last_index_of_first_group_of_numbers is None:
                return None
        except:
            return None

        body_part_name = base_color_texture_image_name[last_index_of_first_group_of_numbers + 1:]
        return body_part_name

class WutheringWavesMaterialIdentifierService:
    BODY_PART_NAMES = ['Up', 'Down', 'Leisi', 'Bangs', 'Eye', 'Face', 'Hair', 'Main', 'Outlines', 'Resonator']

    def get_body_part_name(self, material_name: str) -> Optional[str]:
        # 数字と特殊文字を除去して最後の有効な部位名を抽出
        cleaned_name = re.sub(r'[\d_]', '', material_name)  # 数字とアンダースコアを除去
        for body_part in self.BODY_PART_NAMES:
            if body_part in cleaned_name:
                return body_part
        # マッチしない場合は最後の大文字文字列を抽出
        matches = re.findall(r'[A-Z][a-z]*', material_name)
        return matches[-1] if matches else None

    def __find_second_group_of_numbers(self, input_string):
        # Find the first occurrence of numbers
        match = re.search(r'\d+', input_string)
        len_first_match = len(match.group())
        
        if match:
            # Find the second occurrence of numbers starting from the end of the first match
            match = re.search(r'\d+', input_string[match.span()[1]:])
            
            if match:
                numbers = match.group()
                last_index = match.span()[1] + len_first_match
                return last_index
        return None

    # Handle materials that are exact matches with the texture names (Lamiya's Trident)
    def __exact_material_name_match_check(self, full_name, last_index_of_first_group_of_numbers):
        exact_match_material = bpy.data.materials.get(
            f'{JaredNytsWutheringWavesShaderMaterialNames.MATERIAL_PREFIX}{full_name[:last_index_of_first_group_of_numbers + 1]}'
        )
        if exact_match_material:
            return full_name[:last_index_of_first_group_of_numbers + 1]
        return None

    # Search original materials for a user of the texture name
    def search_original_material_user_for_body_part_name(self, texture_name):
        try:
            last_index_of_first_group_of_numbers = self.__find_second_group_of_numbers(texture_name)
        except:
            return None

        base_texture_name = texture_name[:last_index_of_first_group_of_numbers + 1]
        original_materials = [material for material in bpy.data.materials if 
                              JaredNytsWutheringWavesShaderMaterialNames.MATERIAL_PREFIX not in material.name]
        
        for original_material in original_materials:
            try:
                base_color_texture_image_name = original_material.node_tree.nodes.get('Principled BSDF').inputs.get('Base Color').links[0].from_node.image.name_full
            except:
                continue

            if f'{base_texture_name}.png' == base_color_texture_image_name:
                body_part_name = original_material.name[last_index_of_first_group_of_numbers + 1:]
                return body_part_name

        # No texture image found, check if Chibi material
        if original_material.name == 'XDefaultMaterial':
            return 'XDefaultMaterial'
        return None

    # Get "real" body part name via original texture for this material (Cloth01 using Cloth)
    def get_body_part_name_of_shared_material(self, material_name):
        # Eye and Eyes will run into some funky logic, just keep using original results from `get_body_part_name()`
        if 'Eye' in material_name:
            return None

        try:
            base_color_texture_image_name = bpy.data.materials.get(material_name).node_tree.nodes.get('Principled BSDF').inputs.get('Base Color').links[0].from_node.image.name_full
        except:
            return None
        base_color_texture_image_name = base_color_texture_image_name.replace('.png', '')

        try:
            last_index_of_first_group_of_numbers = self.__find_second_group_of_numbers(base_color_texture_image_name)
            if last_index_of_first_group_of_numbers is None:
                return None
        except:
            return None

        body_part_name = base_color_texture_image_name[last_index_of_first_group_of_numbers + 1:]
        return body_part_name
