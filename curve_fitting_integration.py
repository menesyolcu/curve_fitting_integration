#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def fit_polynomial(x, y, degree):
    """
    Fits a polynomial to the given x and y data using least squares method.
    
    Parameters:
        x (numpy array): Array of x values.
        y (numpy array): Array of y values.
        degree (int): Degree of the polynomial.
    
    Returns:
        poly1d object: Polynomial equation.
    """
    coefficients = np.polyfit(x, y, degree)  # Calculate polynomial coefficients using the least squares method
    polynomial_equation = np.poly1d(coefficients)  # Create a polynomial function using the coefficients
    return polynomial_equation

def calculate_y(polynomial, x_value):
    """
    Calculates the y value for a given x using the polynomial equation.
    
    Parameters:
        polynomial (poly1d object): Polynomial equation.
        x_value (float): The x value to compute y for.
    
    Returns:
        float: The corresponding y value.
    """
    return polynomial(x_value)

def calculate_integral(polynomial, a, b, num_points=1000):
    """
    Calculates the definite integral of the polynomial between two limits.
    
    Parameters:
        polynomial (poly1d object): Polynomial equation.
        a (float): Lower bound of the integral.
        b (float): Upper bound of the integral.
        num_points (int): Number of points for numerical integration. Default is 1000.
    
    Returns:
        float: The result of the integral.
    """
    x_values = np.linspace(a, b, num_points)  # Generate x values over the specified range
    y_values = polynomial(x_values)  # Calculate y values using the polynomial function
    integral_result = np.trapz(y_values, x_values)  # Calculate area under the curve using the trapezoidal rule
    return integral_result

# Get user input
while True:
    try:
        num_points = int(input("How many x, y pairs will you enter? "))
        if num_points < 1:
            raise ValueError("You must enter at least one data pair.")
        break
    except ValueError as e:
        print(e)

x = np.zeros(num_points)
y = np.zeros(num_points)

for i in range(num_points):
    while True:
        try:
            x[i] = float(input(f"Enter the {i + 1}th x value: "))
            y[i] = float(input(f"Enter the {i + 1}th y value: "))
            break  # Exit the loop if valid input is provided
        except ValueError:
            print("Please enter a valid number.")

# Ask the user to choose the fitting type
while True:
    fit_type = input("Do you want to perform linear (L) or nonlinear (E) fitting? (L/E): ").strip().upper()
    if fit_type in ['L', 'E']:
        break
    else:
        print("Invalid selection. Please enter 'L' or 'E'.")

# Determine polynomial degree
if fit_type == 'L':
    degree = 1  # Degree 1 for linear fitting
else:
    while True:
        try:
            degree = int(input("Enter the degree of the polynomial to be created: "))
            if degree < 1 or degree >= num_points:
                raise ValueError(f"Please enter a degree between 1 and {num_points-1}.")
            break
        except ValueError as e:
            print(e)

# Create polynomial
polynomial = fit_polynomial(x, y, degree)

# Print the polynomial function
print("\nThe generated polynomial function is:")
print(polynomial)

# Get x value from user and calculate y value
while True:
    try:
        x_value = float(input("\nEnter an x value to evaluate: "))
        y_value = calculate_y(polynomial, x_value)
        print(f"Result: {y_value}")
        break  # Exit the loop if valid input is provided
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

# Calculate definite integral
while True:
    try:
        a = float(input("\nEnter the lower limit for the integral: "))
        b = float(input("Enter the upper limit for the integral: "))
        integral_result = calculate_integral(polynomial, a, b)
        print(f"Definite integral result: {integral_result}")
        break  # Exit the loop if valid input is provided
    except ValueError:
        print("Invalid input. Please enter numerical values for the limits.")

