from gardena.base_gardena_device_class import BaseGardenaDeviceClass


class WaterControl(BaseGardenaDeviceClass):
    """Class to communicate with a sensor"""

    watering_valve_open = None
    watering_manual_override = None

    """Used to map data between 'mower' ability fields and class fields"""
    watering_outlet_ability_fields = {
        "valve_open": "watering_valve_open",
        "manual_override": "watering_manual_override",
    }

    water_control_ability_type_maps = {
        "watering_outlet": watering_outlet_ability_fields
    }

    def update_information(self, information):
        super(WaterControl, self).update_information(information)
        if "abilities" in information:
            self.handle_abilities(information["abilities"])

    def get_device_specific_ability_type_maps(self):
        return self.water_control_ability_type_maps