#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.7 |

#Import the the classes from the other files
from Calculator_Class import MyCalculator
from UserInterface_Class import UserInterface

#def the performing calculation
def PERFORM_CALCULATION():
    calculator = MyCalculator
    ui = UserInterface
    ui.set_calculator(calculator)
    ui.perform_calculation

PERFORM_CALCULATION()

#end