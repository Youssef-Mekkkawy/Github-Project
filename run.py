# import os
from colorama import Fore

from Class_Converter import Conveter

# To Rest Color.
Rest = Fore.RESET

# Colors
Red = Fore.RED
Green = Fore.GREEN
Yellow = Fore.YELLOW
Cyan = Fore.CYAN

# Decimal, Binary 
decimal = 1000
binary = 1024

# Call class.
convert = Conveter()

""" # Bytes Calulation """

Size_1 = 10
# Decimal
Convert_Byte_To_SomeThing_Decimal = convert.Bytes_Calulation(Size_1, "GB", 1000)
# Binary
Convert_Byte_To_SomeThing_Binary =convert.Bytes_Calulation(Size_1, "GB", 1024)

# Decimal
Convert_Byte_To_SomeThing_Decimal_advanced = convert.Bytes_Calulation_Advanced(Size_1, "GB", 1000)
# Binary
Convert_Byte_To_SomeThing_Binary_advanced =convert.Bytes_Calulation_Advanced(f"{Size_1}GB", Type = 1024)


""" # Size Calulation """
Size_2 = 9897690543
Convert_SomeThing_Binary_To_Byte_Decimal = convert.Size_Calulation(Size_2, 1000)
Convert_SomeThing_Binary_To_Byte_Binary = convert.Size_Calulation(Size_2, 1024)

""" # Decimal Byte """
Decimal_byte = convert.decimal_byte(Size_2)

""" # Binary Byte """
Binary_byte = convert.binary_byte(Size_2)


print("\n" + "-"*20 + "\n")

print(Green + str(Convert_Byte_To_SomeThing_Decimal))
print(str(Convert_Byte_To_SomeThing_Binary) + Rest)

print("\n" + "-"*20 + "\n")

print(Green + str(Convert_Byte_To_SomeThing_Decimal_advanced))
print(str(Convert_Byte_To_SomeThing_Binary_advanced) + Rest)

print("\n" + "-"*20 + "\n")

print(Yellow + str(Convert_SomeThing_Binary_To_Byte_Decimal))
print(str(Convert_SomeThing_Binary_To_Byte_Binary) + Rest)

print("\n" + "-"*20 + "\n")

print(Cyan + str(Decimal_byte))
print(str(Binary_byte) + Rest)

print("\n" + "-"*20 + "\n")

