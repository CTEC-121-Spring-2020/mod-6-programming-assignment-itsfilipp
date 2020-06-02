# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Filipp Kopytyuk

def main():
    numbersSum = 0
    x = float(input("Enter a number (negative to quit) >> "))
    while x >= 0:
        numbersSum = numbersSum + x
        x = float(input("Enter a number (negative to quit) >> "))
    print("\nThe sum of the numbers is", numbersSum)

main()