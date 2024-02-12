import abc
import enum


class Weight(enum.Enum):
    mg = "milligram"
    cg = "centigram"
    dg = "decigram"
    g = "gram"
    kg = "kilogram"
    pound = "lbs"
    ton = "ton"

    def __str__(self):
        """Return the unittype name suitable for printing."""
        return self.value


class WeightConverter:
    """abstract class for all Weight unit"""

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
        order_full = [i.value for i in list(Weight)]
        one_num = WeightUnit.get_instance(self.converter._unit).to_gram(self.converter.number)
        desired_base_value = WeightUnit.get_instance(unit.lower()).base
        index1 = self.get_index(order_full, self.converter._unit)
        index2 = self.get_index(order_full, unit)
        if index2 > index1:
            self.converter._number = one_num / desired_base_value
        else:
            self.converter._number = one_num * desired_base_value
        self.converter._unit = WeightUnit.get_instance(unit.lower())
        return self.converter


class WeightUnit(abc.ABC):
    """abstract class for all Time unit"""

    def __init__(self):
        pass

    @abc.abstractmethod
    def to_gram(self, number):
        """ We make 1 unit as standard for all other unit
        to eliminate multiple if...elif in all WeightUnit subclasses
        And so;
          0.001 = 1 milligram
           0.01 = 1 centigram
            0.1 = 1 decigram
              1 = 1 gram
        453.592 = 1 lbs
           1000 = 1 kilogram
        1000000 = 1 ton

        :param number: int, float
        :return int, float
        """

    def get_instance(string):
        """get class for unit"""
        if string == "milligram":
            return MilligramWeightUnit()
        if string == "centigram":
            return CentigrammWeightUnit()
        if string == "decigram":
            return DecigramWeightUnit()
        if string == "gram":
            return GramWeightUnit()
        if string == "lbs":
            return LbsWeightUnit()
        if string == "kilogram":
            return KilogramWeightUnit()
        if string == "ton":
            return TonWeightUnit()


class MilligramWeightUnit(WeightUnit):
    """base value is 0.001"""
    _base = 0.001

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_gram(self, number):
        """get gram value (without changing the original value)"""
        return number * self._base


class CentigrammWeightUnit(WeightUnit):
    """base value is 0.01"""
    _base = 0.01

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_gram(self, number):
        """get gram value (without changing the original value)"""
        return number * self._base


class DecigramWeightUnit(WeightUnit):
    """base value is 0.1"""
    _base = 0.1

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_gram(self, number):
        """get gram value (without changing the original value)"""
        return number * self._base


class GramWeightUnit(WeightUnit):
    """base value is 1"""
    _base = 1

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_gram(self, number):
        """get gram value (without changing the original value)"""
        return number * self._base


class LbsWeightUnit(WeightUnit):
    """base value is 453.592"""
    _base = 453.592

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_gram(self, number):
        """get gram value (without changing the original value)"""
        return number * self._base


class KilogramWeightUnit(WeightUnit):
    """base value is 1000"""
    _base = 1000

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_gram(self, number):
        """get gram value (without changing the original value)"""
        return number * self._base


class TonWeightUnit(WeightUnit):
    """base value is 1000000"""
    _base = 1000000

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_gram(self, number):
        """get gram value (without changing the original value)"""
        return number * self._base
