from json import loads
from os.path import join
from src.path import PATH
from datetime import date, datetime


DATA = loads(open(join(PATH, 'config.json')).read())


class Employee(object):

    def __init__(self, ci, name, last_name, date_start):
        self.ci = ci
        self.name = name
        self.last_name = last_name
        self.date_start = date_start

    def calculate_salary(self):
        pass

    def __str__(self):
        print(self.date_start)
        print(type(self.date_start))
        print(self.date_start.strftime("%Y"))
        #date_temporal = str(self.date_start.month) + "/" + str(self.date_start.day) + "/" + str(self.date_start.year)
        return '{} {} {} {}'.format("\nCI: " + self.ci,
                                "\nName: " + self.name,
                                "\nLast Name: " + self.last_name,
                                "\nStart Date: " + self.date_start.strftime("%Y/%m/%d"))
        #return "%s %s %s %s" % ("\nCI: " + self.ci,
        #                        "\nName: " + self.name,
        #                        "\nLast Name: " + self.last_name,
        #                        "\nStart Year: " + f"{self.date_start:%Y-%m-%d}")


class Contract(Employee):

    def __init__(self, ci, name, last_name, date_start, salary=0.0):
        super().__init__(ci, name, last_name, date_start)
        self.salary = salary

    def calculate_salary(self):
        today = date.today()
        current_years = today.year - self.date_start.year
        percentage = 0

        if self.date_start.month > today.month or (self.date_start.month == today.month
                                                   and self.date_start.day > today.day):
            current_years -= 1

        if current_years <= 3:
            percentage = float(DATA.get("SALARY_YEAR1_3"))
        elif 3 < current_years <= 7:
            percentage = float(DATA.get("SALARY_YEAR4-7"))
        elif 7 < current_years <= 15:
            percentage = float(DATA.get("SALARY_YEAR8_15"))
        elif current_years >= 16:
            percentage = float(DATA.get("SALARY_YEAR16"))

        if percentage != 0:
            self.salary = float(self.salary + (self.salary * percentage))

        return self.salary

    def __str__(self):
        return "%s %s" % (str(super(Contract, self).__str__()),
                          "\nSalary: " + str(self.calculate_salary()) + " $\n")


class Piecework(Employee):

    def __init__(self, ci, name, last_name,date_start,  client_number=0):
        super().__init__(ci, name, last_name, date_start)
        self.salary = 0.0
        self.client_number = client_number

    def calculate_salary(self):
        piece_percentage_x_client = float(DATA.get("AMOUNT_X_CLIENT"))
        self.salary = float(self.client_number * piece_percentage_x_client)
        return self.salary

    def __str__(self):
        return "%s %s %s" % (str(super(Piecework, self).__str__()),
                             "\nSalary: " + str(self.calculate_salary()) + " $",
                             "\nClient Number: " + str(self.client_number))


class Practitioner(Employee):

    def __init__(self, ci, name, last_name, date_start,  evaluation=0):
        super().__init__(ci, name, last_name, date_start)
        self.evaluation = evaluation
        self.monetary_intensive = 0.0

    def calculate_salary(self):
        intensive_per_month = float(DATA.get("AMOUNT_X_MONTH"))

        if self.evaluation <= 50:
            self.monetary_intensive = intensive_per_month
        elif 50 < self.evaluation <= 80:
            self.monetary_intensive = intensive_per_month * 2
        elif 80 < self.evaluation <= 95:
            self.monetary_intensive = intensive_per_month * 3
        elif self.evaluation >= 96:
            self.monetary_intensive = intensive_per_month * 4

        return self.monetary_intensive

    def __str__(self):
        return "%s %s %s" % (str(super(Practitioner, self).__str__()),
                             "\nMonetary Intensive: " + str(self.calculate_salary()) + " $",
                             "\nEvaluation: " + str(self.evaluation))
