from src.apps.printer_menu import Menu
from src.apps.sub_menu import RectangleMenu
from src.apps.sub_menu import TriangleMenu
from src.apps.sub_menu import RhombusMenu
from src.apps.sub_menu import PrinterMenu
from src.apps.sub_menu import ExitMenu


options = [
    RectangleMenu("Rectangle"),
    TriangleMenu("Triangle"),
    RhombusMenu("Rhombus"),
    PrinterMenu("Print!"),
    ExitMenu("Exit")
]

menu = Menu("Printer Menu", options)
menu.display()

