def perfect(n):
    return sum ([i for i in range (2, n/2 + 1) if n % i == 0]) + 1 == n
