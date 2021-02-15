
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def Sumprimes(rangeX):
    print("Hello Prime numbers problem")
    x=0
    for i in range(1, rangeX):
        if (is_prime(i)):
            x=x+i
    return x

n = int(input("Enter number of elements : ")) 
Sumofnumbers=Sumprimes(n)
print ("Sum of all prime numbers upto ",n, " is ", Sumofnumbers)


