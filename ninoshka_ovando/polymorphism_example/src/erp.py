from src.menu import Menu
from src.human_resources import Contract, Piecework, Practitioner
from datetime import date


class Management(object):

    def __init__(self):
        self.menu = Menu("Employee Manage Program")
        self.options = {
            1: "Insert a Contract Employee",
            2: "Insert a Piecework Employee",
            3: "Insert a Practitioner",
            4: "Print Employee Salaries List",
            5: "Exit"
        }
        self.employees = []

    def insert_a_contract_employee(self):
        ci = self.menu.input_string("CI")
        name = self.menu.input_string("Name")

        last_name = self.menu.input_string("Last Name")
        start_day = self.menu.input_number("Start Day", 1, 31)
        start_month = self.menu.input_number("Start Month[1-12]", 1, 12)

        current_year = str(date.today().year)
        start_year = self.menu.input_number("Start Year", 2000, int(current_year))
        date_start = date(start_year, start_month, start_day)

        salary_base = self.menu.input_number("Salary Base", 1, 20000)

        contract = Contract(ci, name, last_name, date_start, salary_base)
        self.employees.append(contract)

    def insert_a_piecework_employee(self):
        ci = self.menu.input_string("CI")
        name = self.menu.input_string("Name")
        last_name = self.menu.input_string("Last Name")
        start_day = self.menu.input_number("Start Day", 1, 31)
        start_month = self.menu.input_number("Start Month[1-12]", 1, 12)
        current_year = str(date.today().year)
        start_year = self.menu.input_number("Start Year", 2000, int(current_year))
        date_start = date(start_year, start_month, start_day)

        client_number = self.menu.input_number("How many Clients does he manage? ", 1, 10000)

        piecework = Piecework(ci, name, last_name, date_start, client_number)
        self.employees.append(piecework)

    def insert_a_practitioner(self):
        ci = self.menu.input_string("CI")
        name = self.menu.input_string("Name")
        last_name = self.menu.input_string("Last Name")
        start_day = self.menu.input_number("Start Day", 1, 31)
        start_month = self.menu.input_number("Start Month[1-12]", 1, 12)
        current_year = str(date.today().year)
        start_year = self.menu.input_number("Start Year", 2000, int(current_year))
        date_start = date(start_year, start_month, start_day)

        evaluation = self.menu.input_number("Last Evaluation", 1, 100)

        practitioner = Practitioner(ci, name, last_name, date_start, evaluation)
        self.employees.append(practitioner)


    def start_program(self):

        continue_running = True

        while continue_running:
            option = self.menu.select_option_number(self.options)

            if self.options[option] == "Exit":
                self.menu.exit_menu()
                continue_running = False
            elif self.options[option] == "Print Employee Salaries List":
                if len(self.employees) > 0:
                    self.menu.print_employees(self.employees)
                else:
                    self.menu.print_message("There are not any employee registered")
            elif self.options[option] == "Insert a Contract Employee":
                self.insert_a_contract_employee()
            elif self.options[option] == "Insert a Piecework Employee":
                self.insert_a_piecework_employee()
            elif self.options[option] == "Insert a Practitioner":
                self.insert_a_practitioner()

    def restart_management(self):
        self.menu = Menu("Employee Manage Program")
        self.employees = []
        self.start_program()
