def sub(a, b):
    odd = sum(map(lambda odd : odd ** 2, [odd for odd in range (a, b+1) if odd % 2 != 0]))
    even = sum(map(lambda even : even ** 2, [even for even in range (a, b+1) if even % 2 == 0]))
    return odd-even
