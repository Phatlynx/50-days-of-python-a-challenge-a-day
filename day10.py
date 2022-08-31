# write a function called hide_password that takes no parameters. The function
# takes an input (a password) from a user and returns a hidden password. For
# example if the user enters 'hello' as a password the function should return
# '****' as a password and tells the user that the password is 4 characters
# long.
def hide_password() -> str:
    pwd = input('Enter your password: ')
    return '*' * len(pwd), f"Password is {len(pwd)} characters long."

print(hide_password())

# Your new company has a list of figures saved in a list. THe issue is that
# these numbers have no separator. The numbers are saved in teh following
# format: [1000000, 2356989, 2354672, 9878098]. Write a function called
# convert_numbers for readability that takes the numbers in a list and
# convert them into a string. The returned list should be [ '1,000,000',
# '2,356,989', '2,354,672', '9,878,098’].
def convert_numbers(list1: list) -> list:
    return [('{:,}'.format(x)) for x in list1]

print(convert_numbers([1000000, 2356989, 2354672, 9878098]))