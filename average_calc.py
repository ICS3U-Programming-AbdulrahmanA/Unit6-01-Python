#!/usr/bin/env python3
# Created by: Abdul
# Created on: December 15th, 2025
# This program generates random numbers, calculates their sum, and computes the average

import random


def main():
    # Initialize sum to 0 for accumulating values
    sum = 0
    # Maximum number of random values to generate
    MAX_NUM_OF_VALUES = 10
    # Maximum value for random number generation
    MAX_NUM = 100
    # Minimum value for random number generation
    MIN_NUM = 0
    # List to store the generated random numbers
    num_list = []

    # Generate random numbers and add them to the list
    for loop_counter in range(0, MAX_NUM_OF_VALUES, 1):
        # Generate a random number between MIN_NUM and MAX_NUM
        random_number = random.randint(MIN_NUM, MAX_NUM)
        # Append the random number to the list
        num_list.append(random_number)

    # Iterate through the list and sum all the numbers
    for loop_counter in range(0, MAX_NUM_OF_VALUES, 1):
        # Reference to the list of numbers
        number_added = num_list
        # Print each number as it's processed
        print(f"{number_added[loop_counter]}")
        # Add the current number to the running sum
        sum = sum + number_added[loop_counter]

    # Calculate the average by dividing the sum by the count of numbers
    average = sum / MAX_NUM_OF_VALUES
    # Display the calculated average
    print(f"The average is: {average}")


if __name__ == "__main__":
    main()
