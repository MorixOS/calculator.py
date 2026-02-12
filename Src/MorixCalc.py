import time
import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

on = True
while on == True:
    clear_console()
    print("Welcome to MorixOS Calculator!")
    operator = input("Which operator do you wanna use?: ")
    if operator == "+":
        num_amount = int(input("How much numbers to add?: "))

        numbers = []

        for i in range(num_amount):
            num = int(input(f"Number {i+1}: "))
            numbers.append(num)

        result = sum(numbers)
        print("Result:", result)
        end = input("Do you wanna end the calculator?: ")
        if end == "yes" or end == "Yes":
            print("ending...")
            time.sleep(1)
            on = False
        elif end == "no" or end == "No":
            print("Going back to home menu...")
            time.sleep(1)
        else:
            print("type yes or no!")

    elif operator == "-":
        num_amount = int(input("How much numbers to subtract?: "))

        numbers = []

        for i in range(num_amount):
            num = int(input(f"Number {i+1}: "))
            numbers.append(num)

        result = numbers[0]
        for number in numbers[1:]:
            result -= number

        print("Result:", result)
        end = input("Do you wanna end the calculator?: ")
        if end == "yes" or end == "Yes":
            print("ending...")
            time.sleep(1)
            on = False
        elif end == "no" or end == "No":
            print("Going back to home menu...")
            time.sleep(1)
        else:
            print("Type yes or no!")
    elif operator == "*":
        num_amount = int(input("How much numbers to multiply?: "))

        numbers = []

        for i in range(num_amount):
            num = int(input(f"Number {i+1}: "))
            numbers.append(num)

        result = numbers[0]
        for number in numbers[1:]:
            result *= number

        print("Result:", result)
        end = input("Do you wanna end the calculator?: ")
        if end == "yes" or end == "Yes":
            print("ending...")
            time.sleep(1)
            on = False
        elif end == "no" or end == "No":
            print("Going back to home menu...")
            time.sleep(1)
        else:
            print("Type yes or no!")

    elif operator == "/" or operator == ":":
        num_amount = int(input("How much numbers to divide?: "))

        numbers = []

        for i in range(num_amount):
            num = int(input(f"Number {i+1}: "))
            numbers.append(num)

        result = numbers[0]
        for number in numbers[1:]:
            result /= number

        print("Result:", result)

        end = input("Do you wanna end the calculator?: ")

        if end == "yes" or end == "Yes":
            print("ending...")
            time.sleep(1)
            on = False

        elif end == "no" or end == "No":
            print("Going back to home menu...")
            time.sleep(1)

        else:
            print("Type yes or no!")

    else:
        print("This operator doesnt exist!")
