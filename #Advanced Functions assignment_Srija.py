# Srija Belide
# Advanced Functions assignment
# It gives the product of all the numbers inputted
#this line of code converts the string of numbers into list of integers
nums = list(map(int, input().split()))
# this is a multiply function that takes in 2 numbers and multiply them
def multiply(x, y):
    return x * y
# the reduce function is used to multiply all the numbers and get the product
# multiply acts as an argument where the nums acts as an iterator
# so the first two numbers in the list are multiplied together 
#and that product is further multiplied by the following number in the list
# this is an iterable process which occurs until we get the final prodcut
result = reduce(multiply, nums)
print(result)
    
