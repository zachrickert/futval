#futval.py
# A program to compute the future value of an investment
# 10 years in the future.

def main():
    print("This program will calculate the future value of an investment")

    principal = input("Enter the initial investment: ")
    apr = input ("Enter the annual rate: ")

    if (apr > 1.0):
        apr = apr / 100.0

    balance = principal
    for i in range(10):
        balance = balance * (1 + apr)

    print ("The value in 10 years will be $" + str(balance))

main()