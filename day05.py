# Create a function called my_discount. The function takes no
# arguments but asks the user to input the price and the
# discount (percentage) of the product. Once the user inputs the
# price and discount, it calculates the price after the discount.
# The function should return the price after the discount. For
# example, if the user enters 150 as price and 15% as the discount,
# your function should return 127.5.
def my_discount():
    price = int(input("Enter the price: "))
    discount = int(input("Enter the discount: "))
    return price - (price * discount / 100)

print(my_discount())

# Create a function called count_students that takes a list as arguments. Convert each
# string in the list to lowercase, then count the number of 'male' and 'female'
# strings in the list. The function should return a list of tuples.

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

def count_students(arr: list) -> list:
# create an empty list to append lowercase strings
    new_list = []
    student_count = []
    # converting names to lowercase and appending to new_list
    for names in students:
        new_list.append(names.lower())
    # Finding and counting all males in the list and putting it in a tuple
    for sex in new_list:
        if sex == 'male':
            student_count.append((sex, new_list.count(sex)))
            break
    # Finding and counting all females in the list and putting it in a tuple
    for j in new_list:
        if j == 'female':
            student_count.append((j, new_list.count(j)))
            break
    # returning a tuple of students
    return student_count
print(count_students(students))