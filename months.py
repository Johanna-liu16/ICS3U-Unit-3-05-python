#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program identifies a month


def main():
    # this function identifies a month

    # input
    print("This program converts a number to the corresponding month.")
    user_month = input("Enter the number of a month: ")

    # process
    match user_month:
        case "1":
            print("This month is January.")
        case "2":
            print("This month is February.")
        case "3":
            print("This month is March.")
        case "4":
            print("This month is April.")
        case "5":
            print("This month is May.")
        case "6":
            print("This month is June.")
        case "7":
            print("This month is July.")
        case "8":
            print("This month is August.")
        case "9":
            print("This month is September.")
        case "10":
            print("This month is October.")
        case "11":
            print("This month is November.")
        case "12":
            print("This month is December.")
        case _:
            print("Invalid month")

    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
