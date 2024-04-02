#Display the Fibonacci sequence

def recur_fibo(n):
    if n<= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
nterms = int(input("Enter the number of terms (greater than 0): "))

#Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a valid number")
else:
    print ("Fibonacci sequence: ")
    for i in range(nterms):
        print(recur_fibo(i))