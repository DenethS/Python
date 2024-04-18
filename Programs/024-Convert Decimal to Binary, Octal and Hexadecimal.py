#Binary - divided by 2, remainder is 1 or 0, reading bottom to top
#Octal - divided by 8, note the remainder
#Hexadecimal - divided by 16, note the remainder

dec_num = int(input("Enter a decimal number: "))

print("The decimal value of", dec_num, "is")
print(bin(dec_num), "in binary")
print(oct(dec_num), "in octal")
print(hex(dec_num), "in hexadecimal")