# Convert from decimal to octal
# by using a recursive function

def deci_to_oct(decimal: int)-> None:
    if decimal > 0:
        deci_to_oct(int(decimal/8))
        print(decimal % 8, end="")

def main():
    num: int = int(input("Enter a decimal number: "))

    print("The number in octal: ", end = "")
    deci_to_oct(num)

if __name__ == "__main__":
    main()