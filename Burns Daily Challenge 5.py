"""Title: Electronics Master Calculator.
Class: TPRG 2131
Week 3, Assignment 5
Author: Alex Burns
Student ID: 100885375
Date: September 20th, 2023

In the previous challenge, you modified the program to offer the added option to 
calculate the resonant frequency of a series RLC circuit. Today's task is to expand
the program a bit more to give the user the Q (quality factor) of the series RLC 
circuit. No additional inputs are required, the bandwidth and Q are just additional
results to be calculated and printed. Depending on the user's choices, ask for the 
necessary input values, then calculate and print the expected result. The program 
quits gracefully when the user enters "q" or "Q".
"""
import math # taken from https://www.w3schools.com/python/python_math.asp

def calculate_series_resistance(r1, r2): # https://learn.parallax.com/tutorials/language/python/electrical-measurements/measure-resistance/series-vs-parallel
    return r1 + r2

def calculate_parallel_resistance(r1, r2): # https://learn.parallax.com/tutorials/language/python/electrical-measurements/measure-resistance/series-vs-parallel
    return 1 / ((1 / r1) + (1 / r2))

def calculate_rc_time_constant(r, c): # https://www.linquip.com/blog/rc-time-constant-calculator/#:~:text=An%20RC%20time%20constant%2C%20denoted%20by%20%CF%84%20%28tau%29%2C,of%20the%20circuit%3A%20%CF%84%20%3D%20R%20%C3%97%20C
    return r * c

def calculate_resonant_frequency(l, c): # https://www.geeksforgeeks.org/resonant-frequency-formula/
    return 1 / (2 * math.pi * math.sqrt(l * c))

def calculate_quality_factor(r, l, c): # https://testbook.com/physics/quality-factor-of-lcr-circuit
    return (1 / r) * math.sqrt(l / c)

try:
    while True: # https://stackoverflow.com/questions/11758029/try-block-inside-while-statement
        print("Choose an option:")
        print("1. Calculate series resistance")
        print("2. Calculate parallel resistance")
        print("3. Calculate RC time constant")
        print("4. Calculate resonant frequency of a series RLC circuit")
        print("5. Calculate quality factor (Q) of a series RLC circuit")
        print("6. Press q to quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ") # https://stackoverflow.com/questions/23440326/python-choices-and-input

        if choice == '1':
            try:
                r1 = float(input("Enter the value of resistor 1 (in ohms): ")) # https://stackoverflow.com/questions/60369566/how-to-make-python-read-input-as-a-float
                r2 = float(input("Enter the value of resistor 2 (in ohms): "))
                result = calculate_series_resistance(r1, r2)
                print(f"Total series resistance: {result} ohms")
            except ValueError: # https://www.w3schools.com/python/python_try_except.asp
                print("Invalid input. Please enter valid resistor values.")

        elif choice == '2':
            try:
                r1 = float(input("Enter the value of resistor 1 (in ohms): ")) # https://stackoverflow.com/questions/60369566/how-to-make-python-read-input-as-a-float
                r2 = float(input("Enter the value of resistor 2 (in ohms): "))
                result = calculate_parallel_resistance(r1, r2)
                print(f"Total parallel resistance: {result} ohms")
            except ValueError: # https://www.w3schools.com/python/python_try_except.asp
                print("Invalid input. Please enter valid resistor values.")

        elif choice == '3':
            try:
                r = float(input("Enter the value of the resistor (in ohms): "))
                c = float(input("Enter the value of the capacitor (in farads): "))
                result = calculate_rc_time_constant(r, c)
                print(f"RC time constant: {result} seconds")
            except ValueError: # https://www.w3schools.com/python/python_try_except.asp
                print("Invalid input. Please enter valid values.")

        elif choice == '4':
            try:
                l = float(input("Enter the value of the inductor (in henrys): "))
                c = float(input("Enter the value of the capacitor (in farads): "))
                result = calculate_resonant_frequency(l, c)
                print(f"Resonant frequency of the series RLC circuit: {result} Hz")
            except ValueError: # https://www.w3schools.com/python/python_try_except.asp
                print("Invalid input. Please enter valid values.")
                
        elif choice == '5': # https://stackoverflow.com/questions/10499941/how-can-i-solve-equations-in-python
            try:
                r = float(input("Enter the value of the resistor (in ohms): "))
                l = float(input("Enter the value of the inductor (in henrys): "))
                c = float(input("Enter the value of the capacitor (in farads): "))
                result = calculate_quality_factor(r, l, c)
                print(f"Quality factor (Q) of the series RLC circuit: {result}")
            except ValueError:
                print("Invalid input. Please enter valid values.")

        elif choice.lower() == 'q': # https://stackoverflow.com/questions/47337872/how-would-i-code-q-to-quit-python-3-6
            print("Exiting the program.")
            break # https://www.w3schools.com/python/ref_keyword_break.asp

except KeyboardInterrupt: # Code completed by ChatGPT on September 20th, 2023. Prompted by asking "Complete code for working calculator with 5 different calculation options and pressing q to quit"
    print("\nProgram terminated by user (q).") 