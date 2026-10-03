#PRINT:
print("Hello, World!")
print("This is a basic Python script.")
print(10)

#COMMENTS:
# This is a comment in Python. Comments are ignored by the interpreter.
print("Hello again!") 

# VARIABLES:
name = "Bibash"
age = 20
price = 99.99

print("Name:", name)
print("Age:", age)  
print("Price:", price)

# DATA TYPES:
name = "Bibash"  # String
age = 20         # Integer  
price = 99.99     # Float
passed = True     # Boolean

print("Name:", name)
print("Age:", age)
print("Price:", price)
print("Passed:", passed)    

# INPUT:
user_name = input("Enter your name: ")
print("Name:", user_name)

#1. INTEGER INPUT:
age = int(input("Enter your age: "))
print("Age:", age)

#2. FLOAT INPUT:
price = float(input("Enter the price: "))
print("Price:", price)

#Arithmetic Operations:
a = 10
b = 5
#Addition
print(a + b) 
#Subtraction
print(a - b)
#Multiplication
print(a * b)
#Division
print(a / b)
#Floor Division
print(a // b)
#Modulus
print(a % b)

#f-STRING:
name = "Bibash"
age = 20
print(f"Name: {name}, Age: {age}")
print(f"I am {age} years old.")

print(f"Sum = {a + b}, Difference = {a - b}, Product = {a * b}, Quotient = {a / b}")

#COMPARISION OPERATORS:
a = 10
b = 5
print(a == b)  # Equal to   
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a <= b)  # less or equal to
print(a >= b)  # greater pr equal to

#IF CONDITION.
age = 20
if age >= 18:
    print("You are eligible")

#IF-ELSE:
age = 19
if age >= 19:
    print("Adult")
else:
    print("Minor")

#IF -ELIF-ELSE:
marks = 75
marks = int(input("Enter a marks:"))
if marks >= 70:
    print("A")
elif marks >= 65:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")

#EVEN OR ODD:
num = int(input("Enter a number:"))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# positive negative or zero:
num = int(input("Enter a number:"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#LOGICAL OPERATORS:
#AND:
age = 20
fee = "paid"

if age >= 19 and fee == "paid":
    print("Eligible")

#OR:
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Holiday")

#NOT:
passed = False

if not passed:
    print("You need to improve better than before on your study.")

# MEMBERSHIP OPERATOR:
name = ""
name = input("Enter your name:")

if "B" in name:
    print("B is present")

text = "Python"

if "p" in text:
    print("Found")

# For loop:
for i in range(1, 11):
    print(i)

# print BIBASH in 100 words.
for i in range(100):
    print("BIBASH")

#print numbers.
for i in range(1,50):
    print(i)

#while loop.
i = 0

while i <= 5:
    print(i)
    i = i + 1

# break:
for i in range(1,11):

    if i == 5:
        break
    print(i)

#CONTINUE:
for i in range(1, 6):

    if i == 3:
        continue

    print(i)

#STAR PATTERN:
for i in range(1, 11):
    print("*" * i)

#STRING LOOP:
word = "HELLO"

for letter in word:
    print(letter)


#ASCII CHARACTERS.
#CHARACTER--> ASCII
#USE ORD().
print(ord("A"))
print(ord("a"))

#ASCII-->CHARACTER.
#use chr().
print(chr(65))
print(chr(97))

#BUILD IN FUNCTIONS.
#sum()
numbers = [10, 20, 30]
print(sum(numbers))

#max()
num = [10, 20, 30]
print(max(num))

#min()
num = [10, 20, 30]

#abs()
print(abs(-10))

#round:
print(round(10.56778))

#power:
import math
print(math.pow(2, 3))

# Functions:
def hello():
    print("Hello World")

hello()

#Function with parameter.
def hello(name):
    print("Hello", name)

hello("Bibash")

#Function with two parameters.
def add(a, b):
    print(a + b)

add(10, 20)

#ATM USING WHILE + IF/ELSE:
balance = 10000

while True:

    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Balance = Rs. {balance}")

    elif choice == "2":

        amount = int(input("Enter amount: "))

        if amount > balance:
            print("Insufficient balance")

        elif amount <= 0:
            print("Invalid amount")

        else:
            balance = balance - amount
            print(f"Remaining balance = Rs. {balance}")

    elif choice == "3":
        print("Thank you")
        break

    else:
        print("Invalid choice")

#CELCIUS TO FAHRENHEIT:
celcius = float(input("Enter Celcius:"))
fahrenheit = (celcius * 9 / 5) + 32
print(f"Fahrenheit = {fahrenheit}")


# TEMPERATURE CHECKER:
celcius = float(input("Enter temperature:"))

if celcius < 20:
    print("Cold")

elif celcius <= 30:
    print("Normal")

else:
    print("Hot")

#Student pass/ fail:
marks = int(input("Enter a marks:"))

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Four Subjects-Pass Only if all are 50+:
math = int(input("Math:"))
english = int(input("English:")) 
computer = int(input("Computer:"))
nepali = int(input("Nepali:"))

if math >= 50 and english >= 50 and computer >= 50 and nepali >= 50:
    print("PASS")
else:
    print("FAIL")

#NUMBER CONVERSION:
# DECIMAL --> BINARY
num = int(input("Enter a number:"))
print(f"Binary = {bin(num)}")

#decimal-->octal:
num = int(input("Enter a number:"))
print(f"Octal = {oct(num)}")

#decimal to hexa decimal:
num = int(input("Enter a number:"))
print(f"Hexadecimal = {hex(num)}")

#binary --> decimal:
num = input("Enter a number:")

print(f"Decimal = {int(num)}")

#binary --> octal:
num = int(input("Enter a number:"))
print(f"Octal = {oct(num)}")

#binary -->hexadecimal:
num = int(input("Enter a number:"))
print(f"Hexadecimal = {hex(num)}")

#octal -->binary:
num = input("Enter a number:")
decimal = int(num, 8)
print(f"Binary= {bin(decimal)}")

#octal-->decimal:
num = input("Enter a number:")
print(f"Decimal = {int(num, 8)}")

#octal to hexadecimal
num = input("Enter a number:")
print(f"Hexadecimal = {int(num, 8)}")

#hexadecimal to binary:
num = input("Enter a number:")
decimal = int(num, 16)

print(f"Binary = {bin(decimal)}")

#HEXADECIMAL TO DECIMAL:
num = input("Enter a number:")
print(f"Decimal = {int(num, 16)}")

#hexadecimal to octal:
num = input("Enter a number:")
print(f"Octal = {int(num, 16)}")

