# write a function called only_floats, which takes two parameters a and b, and
# returns 2 if both arguments are floats, returns 1 if only one argument is a
# float, and returns 0 if neither argument is a float.
def only_floats(a, b):
    return 2 if type(a) == float and type(b) == float else 1 if type(a) == float or type(b) == float else 0

print(only_floats(12.1, 23))

# write a function called word_index that takes one argument, a list of strings
# and returns the index of the longest word in the list. If there is no longest
# word(if all the strings are of the same length), the function should return 0.
def word_index(list):
    return list.index(max(list, key = len))

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

print(word_index(words1))
print(word_index(words2))