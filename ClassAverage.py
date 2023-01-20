# Program calculates class average

grade_sum = 0

# Assume we have 15 students

for i in range(5):
    grade = float(input("Please give your grade: "))
    grade_sum = grade_sum + grade

average = grade_sum/5
print("Class average: ", average)
