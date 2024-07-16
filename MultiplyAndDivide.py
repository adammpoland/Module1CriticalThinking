num1 = int(input("Please provide a number "))
num2 = int(input("Please provide another number "))
print(f"The product of the two numbers is: {num1*num2}")
if num2 == 0:
    print("the quotient is undefined")
elif num1 == 0:
    print("The quotient is 0")
else:
    print(f"The quotient of the two numbers is : {num1/num2}")