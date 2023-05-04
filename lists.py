# LISTS / ARRAYS

fruits = ["apple", "orange", "berry"]
print(fruits)
fruits.append("pear")
print(fruits)
fruits.append("strawberry")
print(fruits)

# methods vs functions
# append() is a method and print() is a function

'''
INDEXING
'''
print(fruits[0]) 
# this will get me "apple"

print(fruits[2]) 
# this will get me "berry"

print(fruits[-1])
# this will ALWAYS get me the last one in the array

'''
SLICING
'''
print(fruits[0:2])
# this will give me 0 and 1 (stops before 2)

print(len(fruits))
# tells me the length of the array

print(fruits[0: len(fruits)-1])
# this will print everything but the last one of the array

print("hello my name is Justin Signo" [0:10])
# slicing strings!

print(fruits[0:5:1])
# to from by 

print(fruits[0:5:2])
# this will get me the 2nd one

print(fruits[::-1])
# this will reverse the array 


