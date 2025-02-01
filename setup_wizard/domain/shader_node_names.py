# Author: michael-gh1


class ShaderNodeNames:
    BODY_SHADER = ''
    HAIR_SHADER = ''
    FACE_SHADER = ''
    FACE_MATERIAL_ID = ''
    USE_SHADOW_RAMP = ''
    USE_LIGHTMAP_AO = ''
    DEPTH_BASED_RIM = ''

    # StellarToon
    ENABLE_STOCKINGS = ''

    # PGR
    MAIN_SHADER = ''
    USE_LUT = ''


class V2_GenshinShaderNodeNames(ShaderNodeNames):
    BODY_SHADER = 'Group.006'
    HAIR_SHADER = 'Group.006'
    FACE_SHADER = 'Group.006'
    FACE_MATERIAL_ID = 'Face Material ID'
    USE_SHADOW_RAMP = 'Use Shadow Ramp'
    USE_LIGHTMAP_AO = 'Use Lightmap AO'
    DEPTH_BASED_RIM = 'Group.010'


class V3_GenshinShaderNodeNames(ShaderNodeNames):
    BODY_SHADER = 'Body Shader'
    HAIR_SHADER = 'Body Shader'  # Not a typo
    FACE_SHADER = 'Face Shader'
    BODY_HAIR_RAMPS = 'Body / Hair Ramps'
    FACE_MATERIAL_ID = 'Face Material ID'
    USE_SHADOW_RAMP = 'Use Shadow Ramp'
    USE_LIGHTMAP_AO = 'Use Lightmap AO'


class StellarToonShaderNodeNames(ShaderNodeNames):
    MAIN_SHADER = 'Group.006'
    BODY_SHADER = 'Group.006'
    OUTLINES_SHADER = 'Group.006'
    ENABLE_STOCKINGS = 'Enable Stockings'

class JaredNyts_PunishingGrayRavenNodeNames(ShaderNodeNames):
    MAIN_SHADER = 'Group.001'
    FACE_SHADER = 'Group'
    USE_LUT = 'Use LUT = 1, No LUT = 0'

class JaredNyts_WutheringWavesNodeNames(ShaderNodeNames):
    MAIN_SHADER = 'Main Shader'
    FACE_SHADER = 'Face Shader'
    HAIR_SHADER = 'Hair Shader'
    USE_LUT = 'Use LUT = 1, No LUT = 0'
    