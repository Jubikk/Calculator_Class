#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.7 |

#Import tkinter, from tkinter import messagebox and simpledialog, and import time
import tkinter as tk
from tkinter import messagebox, simpledialog
from Calculator_Class import NewCalculator
import time

#Create a UserInterface Class
class UserInterface:
    #def init
    def __init__(self, root, calculator):
        self.calculator = calculator
        self.root = root
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
                             "5. Power\n"
                             "5. Exit")
        
    #def get menu(choices)
    def get_menu_choice(self):
        choice = self.display_input_dialog("Enter your operation(1-5):")
        if choice in ['1', '2', '3', '4', '5', '6']:
            return int(choice)
        else:
            raise UserError("Invalid. Please try again.")    
        
    #def get integer and operation
    def get_integer_input(self, prompt):
        return int(self.display_input_dialog(prompt))
    
    def get_operator_input(self, prompt):
        return self.display_input_dialog(prompt)
    
    #def input dialog
    def display_input_dialog(self, prompt):
        dialog_window = tk.Toplevel(self.root)
        dialog_window.withdraw()
        result = simpledialog.askstring("Input", prompt, parent=dialog_window)
        dialog_window.destroy()
        if result is None:
            self.confirm_exit()
        return result
    
    #def the calculations
    def perform_calculation(self):
        self.display_message("Welcome to the Calculator.")
        self.display_menu()

        calculator = NewCalculator()
        while True:
            try:
                choice = self.get_menu_choice()

                if choice == 1:
                    int1 = self.get_integer_input("Enter your first number:")
                    int2 = self.get_integer_input("Enter your second number:")
                    result = self.calculator.add(int1, int2)
                    self.display_result(result)
                elif choice == 2:
                    int1 = self.get_integer_input("Enter your first number:")
                    int2 = self.get_integer_input("Enter your second number:")
                    result = self.calculator.subtract(int1, int2)
                    self.display_result(result)
                elif choice == 3:
                    int1 = self.get_integer_input("Enter your first number:")
                    int2 = self.get_integer_input("Enter your second number:")
                    result = self.calculator.multiply(int1, int2)
                    self.display_result(result)
                elif choice == 4:
                    int1 = self.get_integer_input("Enter your first number:")
                    int2 = self.get_integer_input("Enter your second number:")
                    result = self.calculator.divide(int1, int2)
                    self.display_result(result)
                elif choice == 5:
                    int1 = self.get_integer_input("Enter the base number:")
                    int2 = self.get_integer_input("Enter the exponent:")
                    result = self.calculator.power(int1, int2)
                    self.display_result(result)
                elif choice == 6:
                    self.display_message("Thank you for using the program!")
                    break

                time.sleep(0.5)

            except UserError as error:
                self.display_message(str(error))

    #def display result
    def display_result(self, result):
        self.display_message("The result is: " + str(result))

    #def exit and close window
    def confirm_exit(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to exit?"):
            self.root.destroy()

    def close_window(self):
        self.confirm_exit()

#class for UserError
class UserError(Exception):
    pass



#End