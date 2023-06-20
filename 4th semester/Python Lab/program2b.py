def binary_to_decimal(n):
    decimal = 0
    i = 0
    while n > 0:
        d = n % 10
        decimal = decimal + (d * (2 ** i))
        n = n // 10
        i = i + 1
    print("Decimal value is:", decimal)


def octal_to_hexadecimal(n):
    decimal = 0
    i = 0
    while n > 0:
        d = n % 10
        decimal = decimal + (d * (8 ** i))
        n = n // 10
        i = i + 1

    hexa = hex(decimal)
    print("Hexadecimal value is:", hexa)


bi = int(input("Enter binary number:"))
binary_to_decimal(bi)
oct = int(input("Enter octal number:"))
octal_to_hexadecimal(oct)
