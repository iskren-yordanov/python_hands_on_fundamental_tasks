"""Code for class Distance"""
class Distance():
    """Class Distance"""
    def __init__(self, meters: int, centimeters: int, milimeters: int):
        self._meters = meters
        self._centimeters = centimeters
        self._milimeters = milimeters
        self._total_dist = meters * 1000 + centimeters * 10 + milimeters

    # alll setters and getters
    @property
    def meters(self):
        """meters getter"""
        return self._meters

    @meters.setter
    def meters(self, value):
        """meters setter"""
        self._meters = value

    @property
    def centimeters(self):
        """centimeters getter"""
        return self._centimeters

    @centimeters.setter
    def centimeters(self, value):
        """centimeters setter"""
        self._centimeters = value

    @property
    def milimeters(self):
        """milimeters getter"""
        return self._milimeters

    @milimeters.setter
    def milimeters(self, value):
        """milimeters setter"""
        self._milimeters = value

    def get_total_dist_as_milimeters(self):
        """get total distance represented as milimeters value"""
        return self._total_dist

    def set_total_distance(self, total_milimeters: int):
        """set object total distance represented as milimeters value
        This will calculated automatically the meters, centimeters and milimeters of the object
        """
        self.meters = total_milimeters // 1000
        self.centimeters = (total_milimeters - self.meters * 1000) // 10
        self.milimeters = total_milimeters - self.meters*1000 - self.centimeters*10

    def __str__(self):
        return f"{self.meters}m, {self.centimeters}sm, {self.milimeters}mm"

    def __repr__(self):
        return f"Distance({self.meters}, {self.centimeters}, {self.milimeters})"

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        obj1_dist = self.get_total_dist_as_milimeters()
        obj2_dist = other.get_total_dist_as_milimeters()

        new_obj = Distance(0,0,0)
        new_obj.set_total_distance(obj1_dist + obj2_dist)
        return new_obj

    def __iadd__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        self.set_total_distance(self.get_total_dist_as_milimeters() +
                                other.get_total_dist_as_milimeters())
        return self

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand for -: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        obj1_dist = self.get_total_dist_as_milimeters()
        obj2_dist = other.get_total_dist_as_milimeters()
        if obj1_dist >= obj2_dist:
            new_obj = Distance(0, 0, 0)
            new_obj.set_total_distance(obj1_dist - obj2_dist)
        else:
            raise ValueError(
                "value error (negative distance) when performing operation: "
                f"'{type(self).__name__}' - '{type(other).__name__}'"
            )
        return new_obj

    def __isub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand for -: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        if self.get_total_dist_as_milimeters() >= other.get_total_dist_as_milimeters():
            self.set_total_distance(self.get_total_dist_as_milimeters() -
                                    other.get_total_dist_as_milimeters())
        else:
            raise ValueError(
                "value error (negative distance) when performing operation: "
                f"'{type(self).__name__}' - '{type(other).__name__}'"
            )

        return self
