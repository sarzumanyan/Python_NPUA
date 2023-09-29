exp = input("Enter any expression: ")
op = ["*", "+", "-", "/", "^"]

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
    result = float(result[0]) / float(result[1])
# elif "^" in exp:
#     result = exp.split("^")
#     result = float(result[0]) ** float(result[1])
else:
    result = "This calculator does not support that expression))\nYet"
print(result)

