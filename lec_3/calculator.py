exp = input("Enter any expression: ")
op = ["*", "+", "-", "/", "^"]

def calculator():
    if "+" in exp:
        result = exp.split("+")
        result = float(result[0]) + float(result[1])
    elif "-" in exp:
        result = exp.split("-")
        result = float(result[0]) - float(result[1])
    elif "*" in exp:
        result = exp.split("*")
        result = float(result[0]) * float(result[1])
    elif "/" in exp:
        result = exp.split("/")
        try:
            result = float(result[0]) / float(result[1])
        except ZeroDivisionError:
           return "Cannot divide by zero."
    else:
        result = "This calculator does not support that expression))\nYet"
    return result

if __name__=="__main__":
    print(calculator())

