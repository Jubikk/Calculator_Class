#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.7 |

#Import tkinter, from tkinter import messagebox and simpledialog, and import time
import tkinter as tk
from tkinter import messagebox, simpledialog
from Calculator_Class import MyCalculator
import time

#Create a UserInterface Class
class UserInterface:
    def __init__(self, root):
        self.calculator = None
        self.root = root
        self.root.withdraw()
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
    #def init
    #def Set Calculator
    #def message
    #def menu
    #def get menu(choices)
    #def get integer and operation
    #def input dialog
    #def the calculations
    #def display result
    #def exit and close window
#class for UserError