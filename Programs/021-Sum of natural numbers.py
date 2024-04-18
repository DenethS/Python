limit = int(input("Enter the limit: "))
sum = 0

#Using for loop for the sum of natural numbers
for i in range(1,limit+1):
    sum += i

print("The sum of naturals numbers up to ", limit, "is", sum)
