# Module 7
#   Programming Assignment 10
#     Prob-3.py

# Filipp Kopytyuk

def main():
    numbersSum = 0
    x = float(input("Enter a number (negative to quit) >> "))

    while True:
        print(x)
        if x <= 0:
            break
        numbersSum = numbersSum + x
        x = float(input("Enter a number (negative to quit) >> "))
    print("\nThe sum of the numbers is", numbersSum)
main()    