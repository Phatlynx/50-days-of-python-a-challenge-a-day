# write a function called odd_even that has one parameter and takes a list of
# numbers as an argument. The function returns the difference between the
# largest even number in the list and the smallest odd number in the list. For
# example, if you pass [1,2,4,6] as an argument the function should return
# 6-1=5.
def odd_even(numbers: list) -> int:
    odd = []
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return max(even) - min(odd)

print(odd_even([1,2,4,6]))

# write a function called prime_numbers. This function asks a user to enter a
# number(int) as an argument and returns a list of all the prime numbers within
# its range. For example, if user enterse 10, function returns [2,3,5,7] as
# prime numbers.
def prime_numbers(n: int) -> list:
    prime_num = []
    # n = int(input('Please enter a number (integer): '))
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_num.append(i)
    return prime_num

"""one line answer"""
    # return [i for i in range(2, number+1) if all(i % j != 0 for j in range(2, i))]

print(prime_numbers(10))