import abc
import enum


class Volume(enum.Enum):
    ml = "milliliter"
    lit = "liter"
    m3 = "cubic meter"
    in3 = "cubic inch"
    ft3 = "cubic foot"
    pt = "pint"
    qt = "quart"
    gal = "gallon"
    bbl = "barrel"

    def __str__(self):
        """Return the unittype name suitable for printing."""
        return self.value


class VolumeConverter:
    """abstract class for all Volume unit"""

    def __init__(self, converter):
        """initialize value from input in corresponding unit"""
        self.converter = converter

    def get_index(self, lst, string):
        """get index of string in given list"""
        if lst[0] == string:
            return 1
        return 1 + self.get_index(lst[1:], string)

    def convert(self, unit):
        """convert original unit to desired unit
            :param unit: str
            :return self
            """
        if self.converter._unit == unit.lower():
            return self.converter
        order_full = [i.value for i in list(Volume)]
        one_num = VolumeUnit.get_instance(self.converter._unit).to_cubic_meter(self.converter.number)
        desired_base_value = VolumeUnit.get_instance(unit.lower()).base
        index1 = self.get_index(order_full, self.converter._unit)
        index2 = self.get_index(order_full, unit)
        if index2 > index1:
            self.converter._number = one_num / desired_base_value
        else:
            self.converter._number = one_num * desired_base_value
        self.converter._unit = VolumeUnit.get_instance(unit.lower())
        return self.converter


class VolumeUnit(abc.ABC):
    """abstract class for all Time unit"""

    def __init__(self):
        pass

    @abc.abstractmethod
    def to_cubic_meter(self, number):
        """ We make 1 unit as standard for all other unit
        to eliminate multiple if...elif in all VolumeUnit subclasses
        And so;
              0.000001 = 1 milliliter
        0.000016387064 = 1 cubic inch
        0.000473176473 = 1 pint
        0.000946352946 = 1 quart
        0.003785411784 = 1 gallon
                 0.001 = 1 liter
        0.028316846592 = 1 cubic foot
        0.119240471196 = 1 barrel
                     1 = 1 cubic meter

        :param number: int, float
        :return int, float
        """

    def get_instance(string):
        """get class for unit"""
        if string == "milliliter":
            return MilliliterVolumeUnit()
        if string == "cubic inch":
            return CubicInchVolumeUnit()
        if string == "pint":
            return PintVolumeUnit()
        if string == "quart":
            return QuartVolumeUnit()
        if string == "gallon":
            return GallonVolumeUnit()
        if string == "liter":
            return LiterVolumeUnit()
        if string == "cubic foot":
            return CubicFootVolumeUnit()
        if string == "barrel":
            return BarrelVolumeUnit()
        if string == "cubic meter":
            return CubicMeterVolumeUnit()


class MilliliterVolumeUnit(VolumeUnit):
    """base value is 0.000001"""
    _base = 0.000001

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base


class LiterVolumeUnit(VolumeUnit):
    """base value is 0.001"""
    _base = 0.001

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base


class CubicMeterVolumeUnit(VolumeUnit):
    """base value is 1"""
    _base = 1

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base


class CubicInchVolumeUnit(VolumeUnit):
    """base value is 0.000016387064"""
    _base = 0.000016387064

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base


class CubicFootVolumeUnit(VolumeUnit):
    """base value is 0.028316846592"""
    _base = 0.028316846592

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base


class PintVolumeUnit(VolumeUnit):
    """base value is 0.000473176473"""
    _base = 0.000473176473

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base


class QuartVolumeUnit(VolumeUnit):
    """base value is 0.000946352946"""
    _base = 0.000946352946

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base


class GallonVolumeUnit(VolumeUnit):
    """base value is 0.003785411784"""
    _base = 0.003785411784

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base


class BarrelVolumeUnit(VolumeUnit):
    """base value is 0.119240471196"""
    _base = 0.119240471196

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_cubic_meter(self, number):
        """get cubic_meter value (without changing the original value)"""
        return number * self._base
