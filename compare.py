def compare(n):
    num = map(int, n.split(','))
    array = []
    for _ in range (3):
        Max = num[0]
        for i in range (len(num)):
            if num[i] > Max:
                Max = num[i]
        num.remove(Max)
        array.append(Max)
    return array
