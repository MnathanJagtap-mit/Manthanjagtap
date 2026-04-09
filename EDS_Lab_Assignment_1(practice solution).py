#EDS_Lab_Assignment_01(solved)

#1. Student Result and Grade

m1 = int(input("Enter marks for course 1: "))
m2 = int(input("Enter marks for course 2: "))
m3 = int(input("Enter marks for course 3: "))
m4 = int(input("Enter marks for course 4: "))
m5 = int(input("Enter marks for course 5: "))

if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    print("Percentage:", percentage)

    if percentage > 75:
        print("Grade: Distinction")
    elif percentage >= 60:
        print("Grade: First Division")
    elif percentage >= 50:
        print("Grade: Second Division")
    elif percentage >= 40:
        print("Grade: Third Division")
else:
    print("Result: Fail")

#2. Fibonacci Sequence

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("How many terms? "))

for i in range(terms):
    print(fibonacci(i))

#3. Pattern Printing

    rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
