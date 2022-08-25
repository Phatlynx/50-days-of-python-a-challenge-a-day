# write a function called register_check that checks how many students are in
# school. The function take a dictionary as a parameter. If the stuent is in
# school, the dictionary says 'yes'. If the student is not in school, the
# dictionary says 'no'. Function should return the number of students in school.
def register_check(dict):
    return sum(1 for x in dict.values() if x == 'yes')

register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(register))

# Task is to write code that will return a tuple of all the names in the list
# that have only lowercase letters. Tuple should have the names sorted
# alphabetically in descending order.
def lowercase_names(list):
    return tuple(sorted((x for x in list if x.islower()), reverse = True))

names = ["kerry", "dickson", "John", "Mary",
"carol", "Rose", "adam"]

print(lowercase_names(names))