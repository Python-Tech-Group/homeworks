class Menu(object):

    def __init__(self):
        print("Welcome to Printed Shares")
        print("=========================================================")
        print("Let's go to start!!")
        print("\n")

    def select_option_number(self, options):
        print("Menu:")
        for key in options:
            print("%d. %s" % (key, options[key]))
        print("--------------------------------------------------------")

        return self.get_input_number("option", 1, 5)

    def exit_menu(self):
        print("You selected Exit option. Bye!!")

    def print_message(self, message):
        print("%s" % message)

    def get_input_number(self, description_input, limit_init, limit_end, odd=False):
        input_number = 0
        try:
            input_number = int(input("Please, introduce a %s(%d - %d) number: " % (description_input, limit_init, limit_end)))
        except ValueError:
            print("You should fill a number(%d - %d)" % (limit_init, limit_end))
            print("Please, try again.")
            self.get_input_number(description_input, limit_init, limit_end, odd)

        if not input_number in range(limit_init, limit_end):
            print("You should fill a number between %d - %d" % (limit_init, limit_end))
            print("Please, try again.")
            self.get_input_number(description_input, limit_init, limit_end, odd)

        if odd:
            if input_number % 2 == 0:
                print("You should fill a odd number between %d to %d" % (limit_init, limit_end))
                print("Please, try again.")
                self.get_input_number(description_input, limit_init, limit_end, odd)

        return input_number

    def get_input_char(self, description_input):
        input_char = ""
        try:
            input_char = str(input("Please, introduce a %s: " % description_input))
        except ValueError:
            print("You should fill a char(e.g.: *, $, ?)")
            print("Please, try again.")
            self.get_input_char(description_input)

        if len(input_char) == 0 or len(input_char) > 1:
            print("You should fill a char(e.g.: *) with a length position 1")
            print("Please, try again.")
            self.get_input_char(description_input)

        return input_char

    def get_input_string(self, description_input):
        input_string = ""
        try:
            input_string = str(input("%s: " % description_input))
        except ValueError:
            print("You should fill a String")
            print("Please, try again.")
            self.get_input_string(description_input)

        if len(input_string) <= 50:
            print("You should fill a String with length limit 50 characters")
            print("Please, try again.")
            self.get_input_string(description_input)

        return input_string

    def print_figure(self, figures):
        for figure in figures:
            print(figure.output_share)
