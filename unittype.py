"""An enumeration of known types of units."""
import enum


class UnitType(enum.Enum):
    """Define the unittypes here.  The value is the printable type name."""
    LENGTH = "Length"
    AREA = "Area"    # you can change Area to some other unittype
    TEMPERATURE = "Temperature"
    VOLUME = "Volume"
    WEIGHT = "Weight"
    TIME = "Time"

    def __str__(self):
        """Return the unittype name suitable for printing."""
        return self.value
