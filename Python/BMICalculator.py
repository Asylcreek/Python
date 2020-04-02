height = int(input("How tall are you? (in pounds): "));

##So, firstly, you would create a variable, in this case, 'height'.
##The variable name can be anything, but it's better if it describes, as closely as possible, the data the variable is gonna hold.
##
##Great, you have created a variable.
##
##The next thing is to collect data from your user, the 'input' keyword would do just that.
##To specify the type of data it is, in this case, a number (an integer), you use the 'int' keyword.


weight = int(input("How much do you weigh? (in inches): ")); ##You should now know why this happened

##For your code, i decided to use a function to calculate the bmi.
##To create a function, you type: "def name_of_the_function (arguments):'
##{def - is for define
## name_of_the_function - is the name you want to call the function, it could literally be anything.
## arguments - you could leave this blank, like BMI_Calculator() or you could put arguments, and you can have as many arguments as you need.
## }

def BMI_Calculator(height, weight) :
    return weight/(height**2) ##the 'return' keyword gives a value and stops the execution of the function

print(' ') ## This prints an empty line
print('Your BMI is ', BMI_Calculator(height, weight))
