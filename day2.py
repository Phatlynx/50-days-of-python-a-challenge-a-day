# write a function called convert_add that takes a list of strings as an argument and converts it to integers and sums the list.
def convert_add(list):
    return sum(map(int, list))

print(convert_add(['1', '3', '5']))

# write a function called check_duplicates that takes a list of strings as an argument. The function should check if the list has any duplicates. If there are duplicates, the function should return the duplicates. If there are no duplicates, the function should return "No Duplicates".
def check_duplicates(list):
    duplicates = set()
    return "No Duplicates" if len(list) == len(set(list)) else [x for x in list if x in duplicates or duplicates.add(x)]

print(check_duplicates(['apple', 'orange', 'banana', 'apple']))
print(check_duplicates(['Yoda', 'Moses', 'Joshua', 'Yoda']))