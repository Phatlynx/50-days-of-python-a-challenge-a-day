# Create a function called biggest_odd that takes a string of numbers and return
# the biggest odd number in the list. For example, if you pass '23569' as an
# argument, your function should return 9. Use list comprehension.
def biggest_odd(string1: str) -> int:
    return [x for x in string1 if int(x) % 2 == 1][-1]

print(biggest_odd('23569'))

# Write a function called zeros_last. This function takes a list as argument. If
# a list has zeroes(0), it will move them to the front of the list and maintain
# the order of the other numbers in the list. If there are no zeroes in the
# list, the function should return the original list sorted in ascending order.
# For example, if you pass [1,4,6,0,7,0,9] as an argument, your function should
# return [1,4,7,9,0,0]. If you pass [2,1,4,7,6] as an argument, your function
# should return [1,2,4,6,7].
def zeros_last(list1:list) -> list:
    zero = []
    non_zero = []
    for i in list1:
        if i == 0:
            zero.append(i)
        else:
            non_zero.append(i)
    return sorted(non_zero) + zero

print(zeros_last([1,4,6,0,7,0,9]))
print(zeros_last([2,1,4,7,6]))