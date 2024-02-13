"""converter"""
from Units.AreaUnit import*
from Units.LengthUnit import*
from Units.TemperatureUnit import*
from Units.TimeUnit import*
from Units.VolumeUnit import*
from Units.WeightUnit import*


class UnitConverter:
    """Store and Convert input Value"""

    def __init__(self):
        """initialize value from input in corresponding unit"""
        self._number = 0
        self._unit = ""

    @property
    def number(self):
        """number value"""
        return self._number

    def set_number(self, number):
        """set self._number"""
        self._number = number

    @property
    def unit(self):
        """unit value"""
        return self._unit

    def set_unit(self, unit):
        """set self._unit"""
        self._unit = unit

    def get_units(self, unittype):
        """get enum unit list"""
        return list(unittype)

    def convert(self, unit):
        """convert original unit to desired unit
        :param unit: str
        :return self
        """
        # convert accordingly to each unit
        # use state/get instance
        if unit in [i.value for i in self.get_units(Area)]:
            return AreaConverter(self).convert(unit)
        elif unit in [i.value for i in self.get_units(Temperature)]:
            return TemperatureConverter(self).convert(unit)
        elif unit in [i.value for i in self.get_units(Time)]:
            return TimeConverter(self).convert(unit)
        elif unit in [i.value for i in self.get_units(Volume)]:
            return VolumeConverter(self).convert(unit)
        elif unit in [i.value for i in self.get_units(Weight)]:
            return WeightConverter(self).convert(unit)
        elif unit in [i.value for i in self.get_units(Length)]:
            return LengthConverter(self).convert(unit)

