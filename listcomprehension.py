def sub():
    odd = sum(map(lambda odd : odd ** 2, [odd for odd in range (1, 11) if odd % 2 != 0]))
    even = sum(map(lambda even : even ** 2, [even for even in range (1, 11) if even % 2 == 0]))
    return odd-even
