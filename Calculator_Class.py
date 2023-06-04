#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.7 |

class MyCalculator:
    def add(self, integer1, integer2):
        return integer1 + integer2
    def subtract(self, integer1, integer2):
        return integer1 - integer2
    def multiply(self, integer1, integer2):
        return integer1 * integer2
    def divide(self, integer1, integer2):
        if integer2 != 0:
            return integer1 / integer2
        else:
            return "Cannot Divide by zero!"
        
class NewCalculator(MyCalculator):
    def power(self, base, exponent):
        return base ** exponent
#End
