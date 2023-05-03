# No arguments
def say_my_name():
    print("hello justin")
    print("hello leta")
    print("hello david")

# say_my_name()

# One argument 
def say_my_name_again(name):
    print(name)

# say_my_name_again("hello again justin")

# Multiple arguments
def greeting(greet, name):
    '''
    greeting takes in 2 arguments (greet and name)
    '''
    print(greet, name)

# positional arguments
# greeting("aloha","justin")

# named arguments
# greeting(greet="hello", name="david")


'''
Takes two integers and, returns their sum
'''
def sum(a: int,b: int):
    return a + b
num = sum(3,4)
# print(num)
# print(sum(6,2))

'''
Tip Calculator PT.2
'''
def foodTotal(amount: float, tip: int):
    tip_amount = amount*(tip/100)
    # print(tip_amount)
    total = tip_amount+amount
    # print(total)
    return total
# print(foodTotal(amount=100,tip=20))
# print(foodTotal(100,20))

'''
Weather PT.2
'''
def what_to_wear(weather: str):
    if weather == "rain":
        print("umbrella")
    elif weather == "cloudy":
        print("hat")
    else:
        print("sunglasses")

# what_to_wear("rain")

'''
Bigger Guy
Write a function that takes in two numbers and chooses the bigger one
'''
def bigger(a:int,b:int):
    if a > b:
        return a
    else:
        return b
print(bigger(3,6))



