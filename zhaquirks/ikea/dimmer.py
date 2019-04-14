"""Ikea dimmer control."""
import logging

from zigpy.profiles import zha
from zigpy.zcl.clusters.general import (
    Groups, Identify, Ota, Scenes, Basic, PowerConfiguration, PollControl,
    LevelControl, OnOff
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
                OnOff.cluster_id,
                IKEA_DIMMER_CLUSTER,
                LightLink.cluster_id
            ],
            'output_clusters': [
                Basic.cluster_id,
                Groups.cluster_id,
                LightLink.cluster_id
            ],
        },
    }
    replacement = {
        'endpoints': {
            1: {
                'manufacturer': 'LUMI',
                'model': 'lumi.sensor_switch.aq2',
                'device_type': zha.DeviceType.REMOTE_CONTROL,
                'input_clusters': [
                    BasicCluster,
                    PowerConfigurationCluster,
                    TemperatureMeasurementCluster,
                    XIAOMI_CLUSTER_ID
                ],
                'output_clusters': [
                    Basic.cluster_id,
                    Groups.cluster_id,
                    XIAOMI_CLUSTER_ID,
                    OnOff.cluster_id,
                ],
            }
        },
    }
