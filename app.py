from validator import Validator


class App:
    def __init__(self):
        print("Hello World")

    def add_cargo(self):
        print("Add Cargo")

    def remove_cargo(self):
        print("Remove Cargo")

    def find_cargo(self):
        print("Print Cargo")

    def show_total_weight(self):
        print("Show Total Weight")

    def run(self):

        option = ""
        while (option != 'exit'):
            option = int(input('Choose an option: '))

            if option == 1:
                self.add_cargo()