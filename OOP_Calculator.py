#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.7 |

#Import the the classes from the other files
import tkinter as tk
from Calculator_Class import MyCalculator
from UserInterface_Class import UserInterface

#def the performing calculation
def PERFORM_CALCULATION():
    calculator = MyCalculator()
    root = tk.Tk()
    ui = UserInterface(root, calculator)
    ui.perform_calculation()
    root.mainloop()

PERFORM_CALCULATION()

#End
