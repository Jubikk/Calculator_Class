#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.7 |

#Import tkinter, from tkinter import messagebox and simpledialog, and import time
import tkinter as tk
from tkinter import messagebox, simpledialog
from Calculator_Class import MyCalculator
import time

#Create a UserInterface Class
class UserInterface:
    #def init
    def __init__(self, root):
        self.calculator = None
        self.root = root
        self.root.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
    #def Set Calculator
    def set_calculator(self, calculator):
        self.calculator = calculator
    #def message
    def display_message(self, message):
        messagebox.showinfo("Message.", message)
    #def menu
    def display_menu(self):
        self.display_message("Calculator Menu\n"
                             "1. Add\n"
                             "2. Subtract\n"
                             "3. Multiply\n"
                             "4. Divide\n"
                             "5. Exit")
    #def get menu(choices)
    def get_menu_choice(self):
        choice = self.display_input_dialog("Enter your operation(1-5):")
        if choice in ['1', '2', '3', '4', '5']:
            return int(choice)
        else:
            raise UserError("Invalid. Please try again.")    
    #def get integer and operation
    def get_integer_input(self, prompt):
        return int(self.display_input_dialog(prompt))

    def get_operator_input(self, prompt):
        return self.display_input_dialog(prompt)
    #def input dialog
    #def the calculations
    #def display result
    #def exit and close window

#class for UserError
class UserError(Exception):
    pass