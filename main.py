def ag():
    """Asks the user if they want to perform another calculation."""
    print("Would you like to do another calculation? Y/N")
    chos = input()
    if chos == "Y" or chos == "y":
        numin()  # Restart the process
    else:
        end()  # Exit the program

def end():
    """Displays a thank-you message when the program ends."""
    print("Thank you for using my calculator!")

def bin2dec(valin1):
    """Converts an 8-bit binary string to a decimal number."""
    x = valin1.strip()  # Remove any leading/trailing spaces
    dec = 0
    for i in range(len(x)):
        dec += int(x[i]) * 2 ** abs((i - (len(x) - 1)))  # Convert each bit to its decimal equivalent
    return dec

def dec2bin(valin1):
    """Converts a decimal number to an 8-bit binary string."""
    bin = ""
    if valin1 == 0:
        return "0"  # Return "0" for decimal zero
    while valin1 > 0:
        remainder = valin1 % 2
        bin = str(remainder) + bin  # Build the binary string from the right
        valin1 //= 2
    return bin

def bin2hex(valin1):
    """Converts an 8-bit binary string to a hexadecimal string."""
    decimal = bin2dec(valin1)  # Convert binary to decimal first
    hex_digits = "0123456789ABCDEF"
    hex = ""
    while decimal > 0:
        hex = hex_digits[decimal % 16] + hex  # Convert decimal to hexadecimal
        decimal //= 16
    return hex

def hex2dec(valin1):
    """Converts a hexadecimal string to a decimal number."""
    dec = 0
    hex_digits = "0123456789ABCDEF"
    for i, d in enumerate(valin1):
        value = hex_digits.index(d)  # Get decimal value of hex digit
        power = (len(valin1) - (i + 1))  # Calculate power of 16
        dec += (value * 16 ** power)
    return dec

def hex2bin(valin1):
    """Converts a hexadecimal string to an 8-bit binary string."""
    return dec2bin(hex2dec(valin1))

def dec2hex(valin1):
    """Converts a decimal number to a hexadecimal string."""
    return bin2hex(dec2bin(valin1))

def binplusbin(valin1, valin2):
    """Adds two 8-bit binary numbers and returns the result in decimal and binary."""
    num1 = int(bin2dec(valin1))
    num2 = int(bin2dec(valin2))
    ans = num1 + num2
    bans = dec2bin(ans)
    if ans >= 255:  # Prevents overflow
        print("BIT OVERFLOW")
        return "----- Error -----"
    else:
        return ans, bans

def bincheck(value):
    """Checks if the given string is a valid binary number (contains only 0s and 1s)."""
    return all(char in '01' for char in value.upper())

def hexcheck(value):
    """Checks if the given string is a valid hexadecimal number."""
    return all(char in '0123456789ABCDEF' for char in value)

def add():
    """Handles binary addition of two 8-bit numbers."""
    print("Enter first binary number:")
    valin1 = input()
    print("Enter second binary number:")
    valin2 = input()
    if len(valin1) == 8 and len(valin2) == 8 and bincheck(valin1) and bincheck(valin2):
        print("In decimal and binary:", binplusbin(valin1, valin2))
        ag()
    else:
        print("Invalid input. Accepted values are 8-bit binary numbers.")
        if input("Try again? (Y/N): ").lower() == "y":
            add()
        else:
            numin()

def binchos():
    """Handles conversion from binary to decimal or hexadecimal."""
    print("Convert to (Hexadecimal/Decimal)?")
    form2 = input()
    print("Enter an 8-bit binary number:")
    valin1 = input()
    if len(valin1) == 8 and bincheck(valin1):
        if form2 == "Hexadecimal":
            print("Hexadecimal:", bin2hex(valin1))
        elif form2 == "Decimal":
            print("Decimal:", bin2dec(valin1))
        else:
            print("Invalid choice.")
        ag()
    else:
        print("Invalid input. Accepted values are 8-bit binary numbers.")
        if input("Try again? (Y/N): ").lower() == "y":
            binchos()
        else:
            numin()

def hexchos():
    """Handles conversion from hexadecimal to binary or decimal."""
    print("Enter a 2-digit hexadecimal number:")
    valin1 = input()
    if len(valin1) == 2 and hexcheck(valin1):
        print("Convert to (Binary/Decimal)?")
        form2 = input()
        if form2 == "Binary":
            print("Binary:", hex2bin(valin1))
        elif form2 == "Decimal":
            print("Decimal:", hex2dec(valin1))
        else:
            print("Invalid choice.")
        ag()
    else:
        print("Invalid input. Accepted values are 2-digit hexadecimal numbers.")
        if input("Try again? (Y/N): ").lower() == "y":
            hexchos()
        else:
            numin()

def decchos():
    """Handles conversion from decimal to binary or hexadecimal."""
    print("Enter a decimal number (0-225):")
    try:
        valin1 = int(input())
        if 0 <= valin1 <= 255:
            print("Convert to (Binary/Hexadecimal)?")
            form2 = input()
            if form2 == "Binary":
                print("Binary:", dec2bin(valin1))
            elif form2 == "Hexadecimal":
                print("Hexadecimal:", dec2hex(valin1))
            else:
                print("Invalid choice.")
            ag()
        else:
            print("Invalid input. Enter a number between 0 and 225.")
            decchos()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        decchos()

def convert():
    """Asks the user what type of conversion they want to perform."""
    print("Convert from (Binary/Hexadecimal/Decimal)?")
    form1 = input()
    if form1 == "Binary":
        binchos()
    elif form1 == "Hexadecimal":
        hexchos()
    elif form1 == "Decimal":
        decchos()
    else:
        print("Invalid input. Choose from Binary, Hexadecimal, or Decimal.")
        convert()

def numin():
    """Main menu asking the user whether to add numbers, convert numbers, or exit."""
    print("Would you like to add, convert, or stop?")
    choice = input().lower()
    if choice == "add":
        add()
    elif choice == "convert":
        convert()
    elif choice == "stop":
        end()
    else:
        print("Invalid choice.")
        numin()

numin()  # Start the program
