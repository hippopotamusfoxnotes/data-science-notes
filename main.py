# example code:

import pandas as pd 

grades = [] # store grades in a list

# ask the user 5 times
for i in range(5):
    # TODO: get user input
    grade = int(input("enter a grade: "))
    grades.append(grade) # add the new grade

df = pd.DataFrame(grades)

print(df.mean())
print(df.median())
print(df.mode())