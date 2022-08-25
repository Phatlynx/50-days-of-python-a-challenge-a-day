# write a function called divide_or_square that takes one number as an argument and returns the square root 
# of the number if it is divisible by 5, returns its remainder if it is not divisible by 5.
def divide_or_square(num):
    return num ** 0.5 if num % 5 == 0 else num % 5

print(divide_or_square(10))

# write a function called longest_value that takes a dictionary as an argument and returns the first longest value of the dictionary.
def longest_value(dict):
    return max(dict.values(), key=len)

print(longest_value({'fruit': 'apple', 'color':'green'}))