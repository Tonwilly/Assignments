num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def calculate():
  add = 0
  sub = 0
  product = 0
  quotient  = 0
  add = num1 + num2
  sub = num1 - num2
  product = num1 * num2
  quotient = num1 / num2

  print("Addition: " + str(num1) + " + " + str(num2) + " = " + str(add))
  print("Substraction: " + str(num1) + " - " + str(num2) + " = " + str(sub))
  print("Product: " + str(num1) + " * " + str(num2) + " = " + str(product))
  print("Division: " + str(num1) + " / " + str(num2) + " = " + str(quotient))


calculate()
