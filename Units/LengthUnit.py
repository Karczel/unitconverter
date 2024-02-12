import abc
import enum


class Length(enum.Enum):
    """Store and Convert Length input Value"""
    mm = "millimeter"
    cm = "centimeter"
    inch = "inch"
    ft = "foot"
    m = "meter"
    wa = "wa"
    km = "kilometer"
    mile = "mile"

    def __str__(self):
        """Return the unittype name suitable for printing."""
        return self.value


class LengthConverter:
    """LengthConverter state"""

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
        order_full = [i.value for i in list(Length)]
        meter_num = LengthUnit.get_instance(self.converter._unit).to_meter(self.converter.number)
        desired_base_value = LengthUnit.get_instance(unit.lower()).base
        index1 = self.get_index(order_full, self.converter._unit)
        index2 = self.get_index(order_full, unit)
        if index2 > index1:
            self.converter._number = meter_num / desired_base_value
        else:
            self.converter._number = meter_num * desired_base_value
        self.converter._unit = LengthUnit.get_instance(unit.lower())
        return self.converter


class LengthUnit(abc.ABC):
    """abstract class for all Length unit"""

    def __init__(self):
        pass

    @abc.abstractmethod
    def to_meter(self, number):
        """ We make 1 unit as standard for all other unit
        to eliminate multiple if...elif in all LengthUnit subclasses
        And so;
           0.001 = 1 millimeter
            0.01 = 1 centimeter
          0.0254 = 1 inch
          0.3048 = 1 foot
               1 = 1 meter
               2 = 1 wa
            1000 = 1 kilometer
        1609.344 = 1 mile

        so firstly,
            we divide the original value with their original unit
            to meter unit, then use this value to convert to our desired unit
        which would look roughly like:
            Original -> meter -> desired
            original -> meter unit
            self.value._number/self._base (of original unit)
            -> desired
            self.value._number (in meter unit) * self._base (of desired unit)

        which simplified via design pattern(in convert class):
        (pseudocode at the moment)
        self._number.to_meter * new_unit._base

        :param number: int, float
        :return int, float

        """

    def get_instance(string):
        """get class for unit"""
        # if string not in [
        #     'millimeter', 'mm', 'centimeter', 'cm', 'meter', 'm',
        #     'kilometer', 'km', 'foot', 'ft', 'inch', 'in', 'mile', 'mi', 'wa'
        # ]:
        #     raise ValueError("unit not available in current converter")
        if string in ['millimeter', 'mm']:
            return MillimeterLengthUnit()
        if string in ['centimeter', 'cm']:
            return CentimeterLengthUnit()
        if string in ['meter', 'm']:
            return MeterLengthUnit()
        if string in ['kilometer', 'km']:
            return KilometerLengthUnit()
        if string in ['foot', 'ft']:
            return FootLengthUnit()
        if string in ['inch', 'in']:
            return InchLengthUnit()
        if string in ['mile', 'mi']:
            return MillimeterLengthUnit()
        if string in ['wa']:
            return WaLengthUnit()
        return None


class MillimeterLengthUnit(LengthUnit):
    """base value is 0.001"""
    _base = 0.001

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_meter(self, number):
        """get meter value (without changing the original value)"""
        return number * self._base


class CentimeterLengthUnit(LengthUnit):
    """base value is 0.01"""
    _base = 0.01

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_meter(self, number):
        """get meter value (without changing the original value)"""
        return number * self._base


class MeterLengthUnit(LengthUnit):
    """base value is 1"""
    _base = 1

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_meter(self, number):
        """get meter value (without changing the original value)"""
        return number * self._base


class KilometerLengthUnit(LengthUnit):
    """base value is 1000"""
    _base = 1000

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_meter(self, number):
        """get meter value (without changing the original value)"""
        return number * self._base


class FootLengthUnit(LengthUnit):
    """base value is 0.3048"""
    _base = 0.3048

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_meter(self, number):
        """get meter value (without changing the original value)"""
        return number * self._base


class InchLengthUnit(LengthUnit):
    """base value is 0.0254"""
    _base = 0.0254

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_meter(self, number):
        """get meter value (without changing the original value)"""
        return number * self._base


class MileLengthUnit(LengthUnit):
    """base value is 1609.344"""
    _base = 1609.344

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_meter(self, number):
        """get meter value (without changing the original value)"""
        return number * self._base


class WaLengthUnit(LengthUnit):
    """base value is 2"""
    _base = 2

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_meter(self, number):
        """get meter value (without changing the original value)"""
        return number * self._base
