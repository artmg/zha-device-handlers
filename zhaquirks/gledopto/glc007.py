"""GLEDOPTO GL-C-007 device."""
from zigpy.profiles import zll, zha
from zigpy.zcl.clusters.general import (
    Basic, OnOff, Identify, LevelControl, Scenes, Groups
)
from zigpy.zcl.clusters.lighting import Color
from zigpy.zcl.clusters.lightlink import LightLink
from zigpy.quirks import CustomDevice

GLC007_PROFILE = 49246

class GLC007(CustomDevice):
    """GLEDOPTO GL-C-007 device."""

	# The GL-C-007 device is a ZLL 5-way LED driver,
	# designed for LED strips with RGB + CCT (CW + WW).
	# Their 5-way drivers are available in two different models:
	#
	# 1 id - the RGB and Whites are both controlled by the same entity
	# but, when selecting RGB, the CCT SMDs turn off and vice-versa
	#
	# 2 id - two separate entities are responsible for the RGB SMDs 
	# and the CCT/Whites SMDs, and both may be on at the same time
	#
	# The current version of this file is based on a 2ID device

    signature = {
		# <SimpleDescriptor endpoint=11 profile=49246 device_type=528 
		# device_version=2 
		# input_clusters=[0, 3, 4, 5, 6, 8, 768] 
		# output_clusters=[]>
        11: {
            'manufacturer': 'GLEDOPTO',
            'model': 'GL-C-007',
            'profile_id': GLC007_PROFILE,
            'device_type': 528,
            #'device_type': zha.DeviceType.COLOR_DIMMABLE_LIGHT,
            'input_clusters': [
                Basic.cluster_id,
                Identify.cluster_id,
                Groups.cluster_id,
                Scenes.cluster_id,
                OnOff.cluster_id,
                LevelControl.cluster_id,
                Color.cluster_id
            ],
            'output_clusters': [
            ],
        },
		
		# Endpoint 15 refers to self as    Model: GL-C-006
		# <SimpleDescriptor endpoint=15 profile=49246 device_type=544 
		# device_version=2 
		# input_clusters=[0, 3, 4, 5, 6, 8, 768] 
		# output_clusters=[]>

        15: {
            'profile_id': GLC007_PROFILE,
            'device_type': 544,
            #'device_type': zll.DeviceType.EXTENDED_COLOR_LIGHT,
            'input_clusters': [
                Basic.cluster_id,
                Identify.cluster_id,
                Groups.cluster_id,
                Scenes.cluster_id,
                OnOff.cluster_id,
                LevelControl.cluster_id,
                Color.cluster_id
            ],
            'output_clusters': [
            ],
        },



		# <SimpleDescriptor endpoint=13 profile=49246 device_type=57694 
		# device_version=2 
		# input_clusters=[4096] 
		# output_clusters=[4096]>
        13: {
            'profile_id': GLC007_PROFILE,
            'device_type': 57694,
            'input_clusters': [
                LightLink.cluster_id
            ],
            'output_clusters': [
                LightLink.cluster_id
            ],
        },
    }

    replacement = {
        'endpoints': {
		   11: {
				'profile_id': GLC007_PROFILE,
				'device_type': 528,
				#'device_type': zha.DeviceType.COLOR_DIMMABLE_LIGHT,
				'input_clusters': [
					Basic.cluster_id,
					Identify.cluster_id,
					Groups.cluster_id,
					Scenes.cluster_id,
					OnOff.cluster_id,
					LevelControl.cluster_id,
					Color.cluster_id
				],
				'output_clusters': [
				],
			},

			15: {
				'profile_id': GLC007_PROFILE,
				# 'device_type': zll.DeviceType.EXTENDED_COLOR_LIGHT,
				'device_type': 0x0220,
				'input_clusters': [
					Basic.cluster_id,
					Identify.cluster_id,
					Groups.cluster_id,
					Scenes.cluster_id,
					OnOff.cluster_id,
					LevelControl.cluster_id,
					Color.cluster_id
				],
				'output_clusters': [
				],
			}

        }
    }
