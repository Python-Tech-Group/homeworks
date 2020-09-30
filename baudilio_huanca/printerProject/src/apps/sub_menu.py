from abc import ABC, abstractmethod
from src.contexts.rectangle import Rectangle
from src.contexts.rectangle import Triangle
from src.contexts.rectangle import Rhombus
from src.contexts.rectangle import Printer


class SubMenu(ABC):
    def __init__(self, name_operation):
        self._label = name_operation
        self._title = None
        self._operation = None
        self._char = None

    def print_sub_menu(self) -> None:
        self.__print_title()
        self._print_arguments()
        self._instance_operation()

    def __print_title(self):
        self._title = '{}{}{}'.format('-' * 10, self._label, '-' * 10)
        print(self._title)
        print('-' * len(self._title))

    def get_label(self):
        return self._label

    def get_operation(self):
        return self._operation

    @abstractmethod
    def _print_arguments(self) -> None:
        pass

    @abstractmethod
    def _instance_operation(self) -> None:
        pass


class RectangleMenu(SubMenu):
    def __init__(self, name_operation):
        super(RectangleMenu, self).__init__(name_operation)
        self.__width = None
        self.__height = None

    def _print_arguments(self) -> None:
        self.__width = int(input("width:"))
        self.__height = int(input("height:"))
        self._char = input("char:")
        print('-' * len(self._title))

    def _instance_operation(self) -> None:
        self._operation = Rectangle(self.__width, self.__height, self._char)


class TriangleMenu(SubMenu):
    def __init__(self, name_operation):
        super(TriangleMenu, self).__init__(name_operation)
        self.__height = None

    def _print_arguments(self) -> None:
        self.__height = int(input("height:"))
        self._char = input("char:")
        print('-' * len(self._title))

    def _instance_operation(self) -> None:
        self._operation = Triangle(self.__height, self._char)


class RhombusMenu(SubMenu):
    def __init__(self, name_operation):
        super(RhombusMenu, self).__init__(name_operation)
        self.__height = None

    def _print_arguments(self) -> None:
        self.__height = int(input("height:"))
        self._char = input("char:")

    def _instance_operation(self) -> None:
        self._operation = Rhombus(self.__height, self._char)


class PrinterMenu(SubMenu):
    def __init__(self, name_operation):
        super(PrinterMenu, self).__init__(name_operation)

    def _print_arguments(self) -> None:
        pass

    def _instance_operation(self) -> None:
        self._operation = Printer()


class ExitMenu(SubMenu):
    def __init__(self, name_operation):
        super(ExitMenu, self).__init__(name_operation)

    def _print_arguments(self) -> None:
        pass

    def _instance_operation(self) -> None:
        pass


