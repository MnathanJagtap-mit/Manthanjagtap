#Practice Lab Assignments:

#1. Momentum Calculation

mass = float(input("Enter mass in kilograms: "))
velocity = float(input("Enter velocity in meters per second: "))
momentum = mass * (velocity ** 2)
print(momentum)

#2. Number Conditions

n_text = input("Enter a number: ")
n = int(n_text)

if n >= 0 and n <= 9:
    ans = n * n
    print(ans)

if n >= 10 and n <= 99:
    ans = n ** 0.5
    print(ans)

if n >= 100 and n <= 999:
    ans = n ** (1/3)
    print(ans)

#3. Employee Data Transformation

def calculate_age(birth_year):
    age = 2026 - birth_year
    print(age)

def calculate_dollars(rupees):
    dollars = rupees / 83
    print(dollars)

birth_year = int(input("Enter birth year: "))
salary = int(input("Enter salary in rupees: "))

calculate_age(birth_year)
calculate_dollars(salary)

#4. Reverse Number

n = int(input("Enter number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = (reverse * 10) + digit
    n = n // 10

print(reverse)
