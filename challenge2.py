# Two numbers are positive
# Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.

def count_positive_numbers (a, b, c):
      # Initialize a variable to count the number of positive numbers.

    num = 0 

    # Check if each parameter is positive and increase the count if it is true
    if a > 0:
        num += 1
    if b > 0:
        num += 1
    if c > 0:
        num += 1

    # Check if the exactly two numbers are positive, and return true 
    if num == 2:
        return True

    #if the count is not 2, return false.
    return False

result = count_positive_numbers(3, -2, 5)
print(result)  
