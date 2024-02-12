import abc
import enum


class Time(enum.Enum):
    NANOSECOND = "nanosecond"
    MICROSECOND = "microsecond"
    MILLISECOND = "millisecond"
    SECOND = "second"
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

    def __str__(self):
        """Return the unittype name suitable for printing."""
        return self.value


class TimeConverter:
    """Time Converter state"""

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
        order_full = [i.value for i in list(Time)]
        one_num = TimeUnit.get_instance(self.converter._unit).to_second(self.converter.number)
        desired_base_value = TimeUnit.get_instance(unit.lower()).base
        index1 = self.get_index(order_full, self.converter._unit)
        index2 = self.get_index(order_full, unit)
        if index2 > index1:
            self.converter._number = one_num / desired_base_value
        else:
            self.converter._number = one_num * desired_base_value
        self.converter._unit = TimeUnit.get_instance(unit.lower())
        return self.converter


class TimeUnit(abc.ABC):
    """abstract class for all Time unit"""

    def __init__(self):
        pass

    @abc.abstractmethod
    def to_second(self, number):
        """ We make 1 unit as standard for all other unit
        to eliminate multiple if...elif in all TimeUnit subclasses
        And so;
        0.000000001 = 1 nanosecond
           0.000001 = 1 microsecond
              0.001 = 1 millisecond
                  1 = 1 second
                 60 = 1 minute
               3600 = 1 hour
              86400 = 1 day
             604800 = 1 week
            2628000 = 1 month
           31556952 = 1 year

        :param number: int, float
        :return int, float
        """

    def get_instance(string):
        """get class for unit"""
        if string == "nanosecond":
            return NanosecondTimeUnit()
        if string == "microsecond":
            return MicrosecondTimeUnit()
        if string == "millisecond":
            return MillisecondTimeUnit()
        if string == "second":
            return SecondTimeUnit()
        if string == "minute":
            return MinuteTimeUnit()
        if string == "hour":
            return HourTimeUnit()
        if string == "day":
            return DayTimeUnit()
        if string == "week":
            return WeekTimeUnit()
        if string == "month":
            return MonthTimeUnit()
        if string == "year":
            return YearTimeUnit()


class NanosecondTimeUnit(TimeUnit):
    """base value is 0.000000001"""
    _base = 0.000000001

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class MicrosecondTimeUnit(TimeUnit):
    """base value is 0.000001"""
    _base = 0.000001

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class MillisecondTimeUnit(TimeUnit):
    """base value is 0.001"""
    _base = 0.001

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class SecondTimeUnit(TimeUnit):
    """base value is 1"""
    _base = 1

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class MinuteTimeUnit(TimeUnit):
    """base value is 60"""
    _base = 60

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class HourTimeUnit(TimeUnit):
    """base value is 3600"""
    _base = 3600

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class DayTimeUnit(TimeUnit):
    """base value is 86400"""
    _base = 86400

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class WeekTimeUnit(TimeUnit):
    """base value is 604800"""
    _base = 604800

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class MonthTimeUnit(TimeUnit):
    """base value is 2628000"""
    _base = 2628000

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base


class YearTimeUnit(TimeUnit):
    """base value is 31556952"""
    _base = 31556952

    @property
    def base(self):
        """read-only value"""
        return self._base

    def to_second(self, number):
        """get second value (without changing the original value)"""
        return number * self._base
