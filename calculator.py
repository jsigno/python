# TIP CALCULATOR APP
food_amount = float(input("enter food amount: "))
tip_percentage = float(input("enter how much you want to tip: "))/100
tip_amount = food_amount * tip_percentage
total = (food_amount + tip_amount)
print(tip_amount)
print("$" + str(total)) 
# ^ changed the total to a string using the str function 

print(f"Tip Amount: {tip_amount}")
print(f"Food Amount: {food_amount}")
print(f"Total Amount: {total}")
# ^ this is called string formatting (f-strings let you embed strings when ran)



#  MATH OPERATORS
# + Addition
# - Subtraction
# / Division
# // (2 symbols is known as Float Division, it also rounds down)
# * Multiplication
# * * (2 is known for Exponential)
# % Modulo (gives the remainders)
