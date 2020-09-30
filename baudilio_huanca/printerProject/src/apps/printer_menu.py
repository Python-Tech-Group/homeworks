import sys
from src.contexts.rectangle import Shape


class Menu:
    def __init__(self, name, options):
        self.name = name
        self.__options = options
        self.__queue_printer = []
        self.__title = self.__build_title(name)

    def display(self):
        exit_option = len(self.__options) - 1
        option_selected = -1
        while option_selected != exit_option:
            self.__display_menu()
            option_selected = self.__get_choice()
            if option_selected == exit_option:
                return
            if option_selected == 3:
                self.__print_queue(option_selected)
            if 3 > option_selected >= 0:
                self.__process_choice(option_selected)

    def __display_menu(self):
        print(self.__title)
        self.__build_options()
        print('-'*len(self.__title))

    def __process_choice(self, option_selected):
        operation_menu = self.__options[option_selected]
        operation_menu.print_sub_menu()
        self.__queue_printer.append(operation_menu.get_operation())

    def __build_title(self, name) -> str:
        return '{}{}{}'.format('-'*10, name, '-'*10)

    def __get_choice(self):
        option_selected = int(input("Enter Option:"))
        return option_selected

    def __build_options(self):
        i = 0
        while i < len(self.__options):
            print('{}. {}'.format(i, self.__options[i].get_label()))
            i = i + 1

    def __print_queue(self, option_selected):
        operation_menu = self.__options[option_selected]
        operation_menu.print_sub_menu()
        printer = operation_menu.get_operation()
        printer.print_shape(self.__queue_printer)
        self.__queue_printer.clear()

