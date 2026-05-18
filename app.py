from cargo_item import CargoItem
from validator import Validator


class App:
    def __init__(self):
        print("Hello World")

    def add_cargo(self):

        print("Add Cargo Itme")

        cname = input("Enter Cargo Name: ")

        while cname == "" or not Validator.minimum_length(cname, 2):
            cname = input("Enter Cargo Name: ")

        cweight = input("Enter Cargo Weight: ")
        # check if int

        try:
            cweight = int(cweight)
        except ValueError:
            print("Invalid Cargo Weight")

        while Validator.validate_positive_numbers(cweight):
            cweight = int(input("Enter Correct Cargo Weight( not empty andbigger then zero ) : "))


        cplanet = input("Enter Cargo Planet: ")

        ci = CargoItem(cname,cweight,cplanet)

        print(ci)


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