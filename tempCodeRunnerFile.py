# Task 1: Start
# Begin by setting up a simple user input loop that asks
# the user to enter the temperature in Fahrenheit.

# Ensure that your program only accepts numerical input and provides
# a friendly error message if the user enters something that can't be converted to a number.
temps = []
def collectTemps():
    again = 'T'
    while again == 'T':
        try: 
            temp = int(input("Enter temperature in Fahrenheit: "))
            temps.append(temp)
            again = input("To enter another temperature, type 'T'. To discontinue, press any other key. ")   
        except ValueError:
            print("Enter temperatures only in the form of numbers.")
    print(f"List of Temperatures in Fahrenheit: {temps}")
    return temps
print()
temps = collectTemps()

# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius.
# Remember that the formula is (Fahrenheit - 32) * 5/9.

# Use a try block to catch any potential errors during the conversion process,
# such as division by zero or overflow errors.

# Task 3: User Experience
# Implement an else block that prints the converted 
# temperature in a user-friendly format.

# Add a finally block that thanks the user for using the weather forecast application,
# ensuring that this message is displayed regardless of whether an exception was caught or not.

celsiusTemps = []
def convertTemps():
    try:
        for temp in temps:
            celsius = round((temp - 32) * (5/9), 2)
            celsiusTemps.append(celsius)
    except ValueError:
        print("Non-numeric value entered.")
    except ZeroDivisionError:
        print("Please enter number less than infinity.")
    except OverflowError:
        print("Try entering a smaller number.")
    else:
        print(f"List of Temperatures in Celsius: {celsiusTemps}") 
    finally:
        print("Thank you for using the weather app!")
convertTemps()
print()

# The Recipe Ratio Adjuster
# Task 1: Start
# Ask the user for the number of servings the recipe is
# originally for and the number of servings they wish to make.

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.

# Use a try block to catch any arithmetic errors that may occur during the calculation.

# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.

# Use a finally block to print a message encouraging the user to enjoy their cooking,
# regardless of the outcome of the calculation.

def recipeAdj():
    tryAgain = 1
    while tryAgain == 1:
        try:
            originServings = float(input("Original Number of Servings: "))
            break
        except ValueError:
            if Exception:
                print("Please input valid number or measurement.")
                tryAgain = int(input("To try again, press 1. Press 2 to quit: "))
        
    tryAgain = 1
    while tryAgain == 1:
        try:
            desiredServings = float(input("Desired Number of Servings: "))
            break
        except ValueError:
            if Exception:
                print("Please input valid number or measurement.")
                tryAgain = int(input("To try again, press 1. Press 2 to quit: "))

    try:
        adjFactor = round(desiredServings / originServings, 2)
        if adjFactor < 0:
            raise ValueError("Adjustment Factor cannot be negative.")
    except ZeroDivisionError:
        print("Origin servings cannot be zero.")
    except Exception as e:
        if adjFactor == 0:
            print("No adjustments are necessary!")
    else:
        print(f"Recipe Adjustment Factor: {adjFactor}")
    finally:
        print("Enjoy your cooking!")
recipeAdj()





