class Rational(object):
    """This creates a rational number (fraction)"""

    # CREATE!!
    def __init__(self, numerator=0, denominator=1):
        """Constructor for a rational number with a numerator and denominator"""
        # 1a create input variables and create fraction
        self.numerator = numerator
        self.denominator = denominator
        # 1b reduce the fraction
        self.reduce() 




    # CALCULATE!  ----> THESE METHODS REQUIRE TWO OTHER INIT CLASSES OF THE SAME OBJECT CLASS THING
    @staticmethod
    def multiply(r1 , r2 ):
        numerator = r1.numerator * r2.numerator 
        denominator = r1.denominator * r2.denominator
        return Rational(numerator , denominator)

    @staticmethod
    def divide(r1 , r2 ):
        output_numerator = r1.numerator * r2.denominator
        output_denominator = r1.denominator * r2.numerator
        return Rational(output_numerator , output_denominator)



    @staticmethod
    def add(r1 , r2 ):
        lcd = r1.denominator *  r2.denominator
        output_numerator = (r1.numerator *  r2.denominator)  +  (r2.numerator * r1.denominator)
        output_denominator = lcd
        output = Rational(output_numerator , output_denominator)
        return output
        

    @staticmethod
    def subtract(r1 , r2 ):
        lcd = r1.denominator *  r2.denominator
        output_numerator = (r1.numerator *  r2.denominator)  -  (r2.numerator * r1.denominator)
        output_denominator = lcd
        output = Rational(output_numerator , output_denominator)
        return output




    # AUTOMATE!
    def getOriginal(self):
        """returns a string representation of the original rational number"""
        return f"{self.numerator}/{self.denominator}" 

    def getDecimal(self):
        """returns a string representatin of the rational number in decimal form"""
        return str(   float(int(self.numerator) / int(self.denominator))   ) 
    
    def getRational(self):
        """return a string representation of the reduced rational number"""
        return f"{self.reducedNumerator}/{self.reducedDenominator}"  




    # REDUCE!
    def reduce( self ):
        """reduces the rational number & creates 2 __init__ (constructor) variables """

        # get greatest common denominator
        gcf = self.__getGCF(self.numerator , self.denominator) 

        # make the init variables
        self.reducedNumerator = self.numerator // gcf
        self.reducedDenominator = self.denominator // gcf

    def __getGCF(self,num1:int, num2:int):
        """returns the greatest common factor of 2 integer values"""
        rem = None
        gcf = None
        while (rem != 0):
            rem = num1 % num2
            if (rem == 0):
                gcf = num2
            else:
                num1 = num2
                num2 = rem
        return gcf




    # OUTPUT!
    def displayData(self):
        print()
        print(self.getOriginal() + " equals "+ self.getDecimal())
        print(self.getOriginal() + " reduces to "+ self.getRational())
        print()





