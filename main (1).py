#1.1 implement a recursive function to calculate the factorial of a given number.


def factorial (n):
  if (n <= 1):
    return 1
  else:
    return (n*factorial  (n-1))
n=int(input ("Enter number:"))
print ("The factorial of",n,"is", factorial (n))