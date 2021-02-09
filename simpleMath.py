'''
This file does all of the string processing and math necessary for calculator.py.
'''

# This function determines what operation is necessary, and calls the appropriate function.
def detect(expression):     # The expression variable is the text of the QLabel.
    expression = expression[:-3]    # Removes the last three characters " = "
    if "÷" in expression:
        divide(expression)
    elif "×" in expression:
        multiply(expression)
    elif "−" in expression:
        subtract(expression)
    elif "+" in expression:
        add(expression)
    else:
        same(expression)

def divide(expression):
    exList = expression.split("÷")  # Gets the numbers being divided in a list
    global result   # Makes it global so the variable can be imported to calculator.py
    try:
        result = float(exList[0]) / float(exList[1])
        if (str(result).split("."))[1] == "0":
            result = int(result)    # Makes numbers ending with ".0"
    except ZeroDivisionError:
        result = "No."

def multiply(expression):
    exList = expression.split("×")
    global result
    result = float(exList[0]) * float(exList[1])
    if (str(result).split("."))[1] == "0":
        result = int(result)

def subtract(expression):
    exList = expression.split("−")
    global result
    result = float(exList[0]) - float(exList[1])
    if (str(result).split("."))[1] == "0":
        result = int(result)

def add(expression):
    exList = expression.split("+")
    global result
    result = float(exList[0]) + float(exList[1])
    if (str(result).split("."))[1] == "0":
        result = int(result)

# If the equal sign is pressed after only one number, the same number will be returned
def same(expression):
    global result
    result = str(int(float(expression)))
