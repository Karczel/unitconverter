import abc
import enum


class Temperature(enum.Enum):
    K = "Kelvin"
    C = "Celsius"
    F = "Fahrenheit"

    def __str__(self):
        """Return the unittype name suitable for printing."""
        return self.value


class TemperatureConverter:
    """abstract class for all Temperature unit"""

    def __init__(self, converter):
        """initialize value from input in corresponding unit"""
        self.converter = converter

    def convert(self, unit):
        """convert original unit to desired unit
        Temperature is a little different
            :param unit: str
            :return self
            """
        if self.converter._unit == unit.title():
            return self.converter
        one_num = TemperatureUnit.get_instance(self.converter._unit).to_kelvin(self.converter.number)
        desired_mul_value = TemperatureUnit.get_instance(unit.title()).mul
        desired_base_value = TemperatureUnit.get_instance(unit.title()).base
        self.converter._number = one_num * desired_mul_value + desired_base_value
        self.converter._unit = TemperatureUnit.get_instance(unit.title())
        return self.converter


class TemperatureUnit(abc.ABC):
    """abstract class for all Time unit"""

    def __init__(self):
        pass

    @abc.abstractmethod
    def to_kelvin(self, number):
        """ We make 1 unit as standard for all other unit
        to eliminate multiple if...elif in all TemperatureUnit subclasses
        But take into consideration that Temperature Unit conversion is
        different
        And so;
                                         (0) = (0) Kelvin
                                (0) - 273.15 = (0) Celsius
                   ((0) - 273.15)*(9/5) + 32 = (0) Fahrenheit
                                             or
        (0) * (9/5) + (-273.15) * (9/5) + 32 = (0) Fahrenheit

        :param number: int, float
        :return int, float
        """

    def get_instance(string):
        """get class for unit"""
        if string == "Kelvin":
            return KelvinTemperatureUnit()
        if string == "Celsius":
            return CelsiusTemperatureUnit()
        if string == "Fahrenheit":
            return FahrenheitTemperatureUnit()


class KelvinTemperatureUnit(TemperatureUnit):
    """base value is 0 and mul value is 1"""
    _base = 0
    _mul = 1

    @property
    def base(self):
        """read-only value"""
        return self._base

    @property
    def mul(self):
        """read-only value"""
        return self._mul

    def to_kelvin(self, number):
        """get kelvin value (without changing the original value)"""
        return (number - self._base) / self._mul


class CelsiusTemperatureUnit(TemperatureUnit):
    """base value is - 273.15 and mul value is 1"""
    _base = - 273.15
    _mul = 1

    @property
    def base(self):
        """read-only value"""
        return self._base

    @property
    def mul(self):
        """read-only value"""
        return self._mul

    def to_kelvin(self, number):
        """get kelvin value (without changing the original value)"""
        return (number - self._base) / self._mul


class FahrenheitTemperatureUnit(TemperatureUnit):
    """base value is (-273.15) * (9/5) + 32 and mul value is 9/5"""
    _base = (-273.15) * (9 / 5) + 32
    _mul = 9 / 5

    @property
    def base(self):
        """read-only value"""
        return self._base

    @property
    def mul(self):
        """read-only value"""
        return self._mul

    def to_kelvin(self, number):
        """get kelvin value (without changing the original value)"""
        return (number - self._base) / self._mul
