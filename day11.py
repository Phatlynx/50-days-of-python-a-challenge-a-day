# write a function called equal_strings. The function takes two string as
# argument and compares them. If the strings are equal (if they have the same
# characters and have equal length), it should return True, if they are not, it
# should return False. For example, 'love' and 'evol' should return True.
def equal_strings(string1: str, string2: str) -> bool:
    return sorted(string1) == sorted(string2)

print(equal_strings('love', 'evol'))

# write a function called swap_values. This function takes a list of numbers and
# swaps the first element with the last element. For example, [2,4,67,7] as a
# parameter, your function should return [7,4,67,2].
def swap_values(list1:list) -> list:
    return list1[-1:] + list1[1:-1] + list1[:1]

print(swap_values([2,4,67,7]))