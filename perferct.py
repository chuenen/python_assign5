def factors(n):
    return [i for i in range (2, n/2 + 1) if n % i == 0]
def perfect(n):
    print  sum (factors(6)) + 1 == n
