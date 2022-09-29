#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: September 28, 2022
# This program calculates and displays the cost of a pizza
# based on the input for the diameter.


import constants


def main():
    # Gets user input for the size of the pizza
    diameter = float(input("Enter the diameter of your pizza (inches): "))

    # Calculates the cost (subtotal and tax) of the Pizza
    subtotal = (
        diameter * constants.INGREDIENTS_COST
        + constants.RENTAL_COST
        + constants.LABOUR_COST
    )
    tax = subtotal * constants.HST

    # Calculates total to be displayed to the user
    total = subtotal + tax

    # Displays the total cost of the pizza to the user
    print("\nThe total cost for the pizza: ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
