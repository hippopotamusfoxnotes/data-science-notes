# xs = {'a': 1, 'b': 2, 'c': 3} # dictionary

# xs['b']

# xs['b'] = 5
# xs['d']

# # note: {'a': 1, 'b': 5, 'c': 3,} 
# y = xs['b']

# for key in xs:
#     value = xs[key]
#     print(key, value)


# students = {} # key: name, value: age


# for_in range(3):
#     student_name = input("input your name")
#     student_age = int(input("input your age"))

#     students[student_name] = student_age




# for name, age in  students.items():
#     if age < 15:
#         print(f"{archie} is a teenager")
#     if age >= 13 and age <=17:
#         print(f"{archie} is a child")
#     if age >=3 and age <=5 :
#         print(f"{archie} is a pre-teen")
#     if age >=10 and age <=12 :
#          print(f"{archie} is a young adult")
#     if age >=18 and age <=26 :
#          print(f"{archie} is an adult")
#     if age >=40 and age <=59 :
#     # child 3-5
#     # pre-teen 10-12
#     # teenager 13-17
#     # young adult 18-26
#     # adult 40-59

# xs = {'a': 1, 'b': 2, 'c': 3} # dictionary

# x = xs['b']

# xs['b'] = 5
# xs['d'] = 8

# # note: {'a': 1, 'b': 5, 'c': 3, 'd': 8}
# y = xs['b']

# for key in xs:
#     value = xs[key]
#     print(key, value)

# students = {} # key: name, value: age

# for _ in range(3):
#     student_name = input("input your name: ")
#     student_age = int(input("input your age: "))
#     students[student_name] = student_age

# for name, age in students.items():
#     if age <= 2:
#         print(f"{name} is an infant")
#     elif age >= 3 and age <= 5:
#         print(f"{name} is a toddler")
#     # child
#     # pre-teen
#     # teenager
#     # young adult
#     # adult

# Given a string: letters
# - count how many of each letter is in the string
# - return the letters with their counts in a dictionary
# example: count_letters("aaabb") -> {'a': 3, 'b': 2}
# example: count_letters("xyzz") -> {'x': 1, 'y': 1, 'z': 2}

def count_letters(letters):
    counts = {} # use a dict to easily store each letter
    # Hint 1:
    # How do we access each letter in our letters
    # string? Can we use a For-loop with strings?

    for letter in letters:
        if counts.get(letter):
            counts[letter] += 1
        else:
            counts[letter] = 1

    # Hint 2:
    # You might want to see if a letter has already been counted
    # or not. Here is a code snippit that will help:
    # if counts.get(letter):
    #   # the letter exists in the dictionary already
    # else:
    #   # the letter does not exist in the dictionary yet

    return counts

print(count_letters("She sells sea shells by the Sea Shore"))


    