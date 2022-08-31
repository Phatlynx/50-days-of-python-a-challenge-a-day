# write a function called string_range that takes a single number and returns a
# string of its range. The string characters should be spearted by dots(.). For
# example, if you pass 6 as an argument, your function should return
# '0.1.2.3.4.5'.
def string_range(num: int) -> str:
    return '.'.join(map(str, range(num)))

print(string_range(6))

# Given a list of names, write a function that returns all the names that start
# with 'S'. Return a dictionary of all the names that start with 'S' and number
# of times they appear in the dictionary.
def s_finder(names: list) -> dict:
    return {name: names.count(name) for name in names if name.startswith('S')}

names = ["Joseph","Nathan", "Sasha", "Kelly",
"Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

print(s_finder(names))