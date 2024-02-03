# 22) Using only if-else statements tWrite a Python program that categorizes 
# a student's mark (0-100) into 'A' (90-100), 'B' (80-89), 'C' (70-79), 
# 'D' (60-69), and 'F' (below 60) using only if-else statements.

# Input: Student's mark
mark = float(input("Enter the student's mark (0-100): "))

if mark >= 90:
    grade = "A"
else:
    if mark >= 80:
        grade = "B"
    else:
        if mark >= 70:
            grade = "C"
        else:
            if mark >= 60:
                grade = "D"
            else:
                grade = "F"

# Output the grade
print(f"The student's grade is {grade}.")