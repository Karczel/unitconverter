import abc
import enum


class Area(enum.Enum):
    cm2 = "square centimeter"
    in2 = "square inch"
    ft2 = "square foot"
    yd2 = "square yard"
    m2 = "square meter"
    ac = "acre"
    ha = "hectare"
    km2 = "square kilometer"
    mi2 = "square mile"

    def __str__(self):
        """Return the unittype name suitable for printing."""
        return self.value


class AreaConverter:

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
        order_full = [i.value for i in list(Area)]
        one_num = AreaUnit.get_instance(self.converter._unit).to_square_meter(self.converter.number)
        desired_base_value = AreaUnit.get_instance(unit.lower()).base
        index1 = self.get_index(order_full, self.converter._unit)
        index2 = self.get_index(order_full, unit)
        if index2 > index1:
            self.converter._number = one_num / desired_base_value
        else:
            self.converter._number = one_num * desired_base_value
        self.converter._unit = AreaUnit.get_instance(unit.lower())
        return self.converter


class AreaUnit(abc.ABC):
    """abstract class for all Area unit"""

    def __init__(self):
        pass

    @abc.abstractmethod
    def to_square_meter(self, number):
        """ We make 1 unit as standard for all other unit
        to eliminate multiple if...elif in all Unit subclasses
        And so;
              0.0001 = 1 square centimeter
          0.00064516 = 1 square inch
          0.09290304 = 1 square foot
          0.83612736 = 1 square yard
                   1 = 1 square meter
        4046.8564224 = 1 acre
               10000 = 1 hectare
             1000000 = 1 square kilometer
        2589988.1103 = 1 square mile

        :param number: int, float
        :return int, float
        """

    def get_instance(string):
        """get class for unit"""
        if string == "square centimeter":
            return SquareCentimeterAreaUnit()
        if string == "square inch":
            return SquareInchAreaUnit()
        if string == "square foot":
            return SquareFootAreaUnit()
        if string == "square yard":
            return SquareYardAreaUnit()
        if string == "square meter":
            return SquareMeterAreaUnit()
        if string == "acre":
            return AcreAreaUnit()
        if string == "hectare":
            return HectareAreaUnit()
        if string == "square kilometer":
            return SquareKilometerAreaUnit()
        if string == "square mile":
            return SquareMileAreaUnit()


class SquareCentimeterAreaUnit(AreaUnit):
    """base value is 0.0001"""
    _base = 0.0001

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base


class SquareInchAreaUnit(AreaUnit):
    """base value is 0.00064516"""
    _base = 0.00064516

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base


class SquareFootAreaUnit(AreaUnit):
    """base value is 0.09290304"""
    _base = 0.09290304

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base


class SquareYardAreaUnit(AreaUnit):
    """base value is 0.83612736"""
    _base = 0.83612736

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base


class SquareMeterAreaUnit(AreaUnit):
    """base value is 1"""
    _base = 1

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base


class AcreAreaUnit(AreaUnit):
    """base value is 4046.8564224"""
    _base = 4046.8564224

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base


class HectareAreaUnit(AreaUnit):
    """base value is 10000"""
    _base = 10000

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base


class SquareKilometerAreaUnit(AreaUnit):
    """base value is 1000000"""
    _base = 1000000

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base


class SquareMileAreaUnit(AreaUnit):
    """base value is 2589988.1103"""
    _base = 2589988.1103

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_square_meter(self, number):
        """get square_meter value (without changing the original value)"""
        return number * self._base
