
class ValueObject:
    def __init__(self, value):
        self._value = value


class IntValue(ValueObject):
    def __init__(self, value):
        super(IntValue, self).__init__(value)

    def is_valid(self):
        if self.__is_number() and self.__is_range_valid():
            return True
        return False

    def __is_number(self):
        return type(self._value) is int

    def __is_range_valid(self):
        if 0 < self._value < 100:
            return True
        return False

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__


class CharValue(ValueObject):
    def __init__(self, value):
        super(CharValue, self).__init__(value)

    def is_valid(self):
        if self.__is_char():
            return True
        return False

    def __is_char(self):
        return len(self._value) == 1
