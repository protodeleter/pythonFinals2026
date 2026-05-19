from cargo_item import CargoItem
from db import Db
from validator import Validator


class App:
    def __init__(self):
        print("Hello World")


    def _cut_the_process(self , value):
        if value == "**":
            return False
        return None

    def add_cargo(self):

        procceed = input("Add Cargo Item? Y/N: ")
        if procceed == "N" or procceed == "n":
            return False


        cname = input("Enter Cargo Name: (Enter ** to exit)")
        if self._cut_the_process(cname):
            return False

        while cname == "" or not Validator.minimum_length(cname, 2) :
            cname = input("Enter Cargo Name: (Enter ** to exit)")
            if self._cut_the_process(cname):
                return False

        cweight = input("Enter Cargo Weight: (Enter ** to exit)")
        if  self._cut_the_process(cweight):
            return False

        while cweight == "" or not Validator.validate_positive_numbers(cweight) and not cweight == "**":
            print("Cargo weight must be a positive number. (Enter ** to exit)")
            cweight = input("Enter Cargo Weight: ")
            if  self._cut_the_process(cweight):
                return False

        cweight = float(cweight)


        cplanet = input("Enter Cargo Planet: (Enter ** to exit)")
        if  self._cut_the_process(cplanet):
            return False
        while not Validator.minimum_length(cplanet, 1) and not cplanet == "**":
            cplanet = input("Cargo Planet cannot be empty: (Enter ** to exit)")
            if  self._cut_the_process(cplanet):
                return False

        ci = CargoItem(cname, cweight, cplanet)

        db = Db()
        if db.insert_item({ "itemid" : str(ci.item_id), "name":ci.cargo_name, "weight" : ci.cargo_weight, "planet" : ci.cargo_origin_planet}):
            print("****Item Added****")
        else:
            print("Something went wrong")


    def remove_cargo(self):
        print("Remove Cargo")

    def find_cargo(self):
        print("Print Cargo")

    def show_total_weight(self):
        print("Show Total Weight")

    def run(self):

        option = ""
        while option != 'exit':

            option = int(input('Choose an option: \n 1: Add cargo item \n 2: Remove cargo item \n 3: Find cargo item \n 4: Show total weight \n 5: Exit \n'))

            if option == 1:
                self.add_cargo()