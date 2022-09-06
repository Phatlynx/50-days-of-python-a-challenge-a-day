# Write a function called count_dots. This function take a string separated by
# dots as a parameter and counts how many dots are in the string. For example,
# 'h.e.l.p.' should return 4 dots, and 'he.lp.' should return 2 dots.
def count_dots(string1:str) -> int:
    return string1.count('.')

print(count_dots('h.e.l.p.'))
print(count_dots('he.lp.'))

# Write a function called age_in_minutes that tells a user how old they are in
# minutes. Your code should ask the user to enter their year of birth, and it
# should return their age in minutes (by subtracting their year of birth to the
# current year). The user can only input a 4 digit year (e.g. 1990, 2000, 2010)
# with no spaces. If the user inputs a year that is not 4 digits, notify the
# user to input a four digit number. If a user enters a year before 1900, your
# code should tell the user that input is invalid. If the user enters the year
# after the current year, the code should tell the user that input is invalid.
# The code should run until the user inputs a valid year.
def age_in_minutes() -> int:
    currentYear = 2022
    while (birthYear := int(input('Enter your year of birth: '))) not in range(1900, currentYear):
        print("Enter a valid year between 1900 and 2021.")
    else:
        return (currentYear - birthYear) * 365 * 24 * 60

print(age_in_minutes())