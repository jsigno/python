# BOOLEAN
# if then else 

# Weather App
# if it is raining grab an umbrella -> otherwise grab a pair of sunglasses

weather = input("What is the weather: ")

if weather == "rain": 
    print("umbrella") 
elif weather == "cloudy":
    print("hat")
elif weather == "thunderstorm":
    print("shield")
else:
    print("sunglasses")

# boolean is only (true, false)

# = is an assignment
# == is a comparison

# comparison operators
# ( == , < , > , <= , >= )

# Grades App
# > 90 = A
# > 80 = B
# > 70 = C
# > 60 = D
# < 60 = F

score = 87

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else: 
    print("F")

# passing or failing grade or HELLA PASS
# HELLA PASS is 100

if score >= 60 and score <  100:
    print("passing")
elif score == 100:
    print("hella pass")
else:
    print("failed homie")


# PYTHONIC CODE
if 60 <= score <= 100:
    print("passing")