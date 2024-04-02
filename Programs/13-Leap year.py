year = int(input("Please enter the year: "))

#Divided by 100 means century year (ending with 00)
#Century year divided by 400 is Leap year
if (year %400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

#Not divided by 100 means not a century year
#Year divided by 4 is a Leap year
elif (year %4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

#If not divided by both 400 (century year) and 4 (not century year)
#Year is not Leap Year
else:
    print("{0} is not a leap year".format(year))