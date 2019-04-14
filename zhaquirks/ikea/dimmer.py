"""Ikea dimmer control."""
import logging

from zigpy.profiles import zha
# https://github.com/zigpy/zigpy/blob/master/zigpy/zcl/clusters/general.py
from zigpy.zcl.clusters.general import (
    Basic, PowerConfiguration, Identify, Alarms, Groups, OnOff,
    LevelControl, Ota # , Scenes, Basic, PollControl 
)
from zigpy.zcl.clusters.lighting import Color
from zigpy.zcl.clusters.lightlink import LightLink
from zigpy.quirks import CustomDevice

IKEA_DIMMER_DEVICE = 0x0810  # 2064 base 10
IKEA_DIMMER_CLUSTER = 0x0b05  # 2821 base 10

_LOGGER = logging.getLogger(__name__)

class IkeaDimmer(CustomDevice):
    """Ikea dimmer control."""

    signature = {
        # <SimpleDescriptor endpoint=1 profile=260 device_type=2064 
        # device_version=2 
        # input_clusters=[0, 1, 3, 9, 2821, 4096] 
        # output_clusters=[3, 4, 6, 8, 25, 4096]>
        1: {
            'manufacturer': 'IKEA of Sweden',
            'model': 'TRADFRI wireless dimmer',
            'profile_id': zha.PROFILE_ID,
            'device_type': IKEA_DIMMER_DEVICE,
            'input_clusters': [
                Basic.cluster_id,
                PowerConfiguration.cluster_id,
                Identify.cluster_id,
                Alarms.cluster_id,
                IKEA_DIMMER_CLUSTER,
                LightLink.cluster_id
            ],
            'output_clusters': [
                Identify.cluster_id,
                Groups.cluster_id,
                OnOff.cluster_id, 
                LevelControl.cluster_id, 
                Ota.cluster_id, 
                LightLink.cluster_id
            ],
        },
    }
    replacement = {
        'endpoints': {
            1: {
                'manufacturer': 'IKEA of Sweden',
                'model': 'TRADFRI wireless dimmer',
                'device_type': zha.DeviceType.REMOTE_CONTROL,
                'input_clusters': [
                    BasicCluster,
                    PowerConfigurationCluster,
                    IdentifyCluster,
                    AlarmsCluster,
                    IKEA_DIMMER_CLUSTER,
                    LightLinkCluster
                ],
                'output_clusters': [
                    Identify.cluster_id,
                    Groups.cluster_id,
                    OnOff.cluster_id, 
                    LevelControl.cluster_id, 
                    Ota.cluster_id, 
                    LightLink.cluster_id
                ],
            },
        },
    }
